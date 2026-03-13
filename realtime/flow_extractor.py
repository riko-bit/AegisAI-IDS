import time
from collections import defaultdict

# Dictionary storing packets belonging to each flow
flows = defaultdict(list)

def flow_id(packet):

    try:
        # Extract flow identifiers
        src = packet.ip.src
        dst = packet.ip.dst
        proto = packet.transport_layer

        sport = packet[proto].srcport
        dport = packet[proto].dstport

        # Flow defined by 5-tuple
        return (src,dst,sport,dport,proto)

    except:
        return None


def update_flow(packet):
    fid = flow_id(packet)

    if fid is None:
        return None

    # Append packet to the corresponding flow
    flows[fid].append(packet)

    # When enough packets collected, compute features
    if len(flows[fid]) > 20:
        packets = flows[fid]

        # Extract flow-level features
        features = extract_features(packets)

        # Reset flow buffer
        flows[fid] = []

        return features

    return None