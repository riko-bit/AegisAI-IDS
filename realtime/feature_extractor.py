def extract(packet):

    try:

        features = []

        # Extract packet length feature
        length = int(packet.length)

        # Encode protocol type as a numeric feature
        protocol = 0
        if hasattr(packet, "tcp"):
            protocol = 6
        elif hasattr(packet, "udp"):
            protocol = 17

        # Add extracted features to feature vector
        features.append(length)
        features.append(protocol)

        # Pad remaining feature positions to match
        # the 52-feature input expected by the model
        while len(features) < 52:
            features.append(0)

        return features

    except:
        # If packet parsing fails, skip packet
        return None