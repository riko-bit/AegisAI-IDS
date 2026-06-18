from collections import defaultdict
import time

class BehaviorTracker:
    # Tracks IP behavior patterns (UEBA)
    def __init__(self):
        self.data = defaultdict(lambda: {
            "count": 0,
            "last": time.time(),
            "avg_interval": 0
        })

    def update(self, ip):
        now = time.time()
        d = self.data[ip]

        interval = now - d["last"]
        d["avg_interval"] = (d["avg_interval"] + interval) / 2
        d["last"] = now
        d["count"] += 1

        return d

    def score(self, ip):
        d = self.data[ip]

        if d["count"] > 100:
            return 0.9
        if d["avg_interval"] < 0.05:
            return 0.7
        return 0.2