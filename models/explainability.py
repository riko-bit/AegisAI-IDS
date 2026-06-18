import numpy as np

def explain(features):
    # simple feature importance (fast alternative to SHAP)
    return np.argsort(np.abs(features))[::-1][:5].tolist()