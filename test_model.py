from realtime.inference import detect
import numpy as np

# must match your feature count (22)
sample = np.random.rand(22)

result = detect(sample, "test_ip")

print(result)