def extract(packet):
    try:
        length = int(packet.length)

        # protocol encoding
        protocol = 0
        if hasattr(packet, "tcp"):
            protocol = 6
        elif hasattr(packet, "udp"):
            protocol = 17

        # ✅ 22 features (must match training)
        features = [
            length,                 # Flow Duration (approx)
            1,                      # Total Fwd Packets
            0,                      # Total Backward Packets

            length, length, length, 0,   # Fwd Packet stats
            length, length, length, 0,   # Bwd Packet stats

            length,                # Flow Bytes/s
            1,                     # Flow Packets/s

            0, 0, 0, 0,            # IAT stats

            length,                # Packet Length Mean
            0,                     # Packet Length Std

            0,                     # FIN
            0,                     # PSH
            0                      # ACK
        ]

        return features

    except:
        return None