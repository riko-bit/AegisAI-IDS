import numpy as np
from collections import defaultdict

flows = defaultdict(list)

def flow_id(packet):
    try:
        src = packet.ip.src
        dst = packet.ip.dst
        proto = packet.transport_layer
        sport = packet[proto].srcport
        dport = packet[proto].dstport
        return (src, dst, sport, dport, proto)
    except:
        return None

def is_forward(packet, fid):
    try:
        return packet.ip.src == fid[0]
    except:
        return True

def extract_features(packets, fid):
    fwd_lengths, bwd_lengths = [], []
    times = []

    for p in packets:
        try:
            length = int(p.length)
            t = float(p.sniff_timestamp)

            times.append(t)

            if is_forward(p, fid):
                fwd_lengths.append(length)
            else:
                bwd_lengths.append(length)

        except:
            continue

    if len(times) < 2:
        return None

    duration = times[-1] - times[0]
    iat = np.diff(times)

    def stats(arr):
        if len(arr) == 0:
            return [0,0,0,0]
        return [
            max(arr),
            min(arr),
            np.mean(arr),
            np.std(arr)
        ]

    fwd_stats = stats(fwd_lengths)
    bwd_stats = stats(bwd_lengths)

    features = []

    # 🔹 Flow
    features.append(duration)

    # 🔹 Packet counts
    features.append(len(fwd_lengths))
    features.append(len(bwd_lengths))

    # 🔹 Length stats
    features += fwd_stats
    features += bwd_stats

    # 🔹 Flow bytes
    total_bytes = sum(fwd_lengths) + sum(bwd_lengths)
    total_packets = len(packets)

    features.append(total_bytes)
    features.append(total_packets)

    # 🔹 Rates
    features.append(total_bytes / (duration + 1e-6))
    features.append(total_packets / (duration + 1e-6))

    # 🔹 IAT stats
    if len(iat) > 0:
        features += [
            np.mean(iat),
            np.std(iat),
            np.max(iat),
            np.min(iat)
        ]
    else:
        features += [0,0,0,0]

    # 🔹 Packet length overall
    all_lengths = fwd_lengths + bwd_lengths
    features += [
        np.mean(all_lengths),
        np.std(all_lengths)
    ]

    # 🔹 TCP Flags (approx)
    fin = psh = ack = 0
    for p in packets:
        try:
            flags = int(p.tcp.flags, 16)
            fin += flags & 0x01
            psh += (flags >> 3) & 1
            ack += (flags >> 4) & 1
        except:
            continue

    features += [fin, psh, ack]

    return features

def update_flow(packet):
    fid = flow_id(packet)
    if fid is None:
        return None, None

    flows[fid].append(packet)

    # emit when flow grows
    if len(flows[fid]) >= 20:
        packets = flows[fid]
        features = extract_features(packets, fid)
        flows[fid] = []

        return features, fid[0]

    return None, None