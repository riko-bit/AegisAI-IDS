import torch
import joblib
import pandas as pd
import numpy as np

from models.autoencoder import Autoencoder
from models.classifier import IDSClassifier
from models.explainability import explain

from realtime.risk_scoring import RiskScorer
from realtime.behavior_tracker import BehaviorTracker
from realtime.temporal_buffer import TemporalBuffer

INPUT_DIM = 22

# load models
ae = Autoencoder(INPUT_DIM)
ae.load_state_dict(torch.load("models/saved/autoencoder.pth"))
ae.eval()

clf = joblib.load("models/saved/classifier.pkl")

scaler = joblib.load("models/saved/scaler.pkl")

# modules
risk_scorer = RiskScorer()
tracker = BehaviorTracker()
temporal = TemporalBuffer()

THRESHOLD = 0.01

def detect(features, ip="unknown"):
    # scale features
    df = pd.DataFrame([features], columns=scaler.feature_names_in_)
    features = scaler.transform(df)[0]

    # AE anomaly score
    x = torch.tensor(features).float().unsqueeze(0)
    with torch.no_grad():
        out = ae(x)

    loss = torch.mean((x - out) ** 2).item()

    # classifier prediction
    pred = clf.predict([features])[0]
    conf = max(clf.predict_proba([features])[0])

    # UEBA
    tracker.update(ip)
    behavior_score = tracker.score(ip)

    # temporal
    temporal.add(features)
    temporal_score = temporal.score()

    # final risk
    risk = risk_scorer.compute(loss, conf, behavior_score, temporal_score)
    level = risk_scorer.level(risk)

    # explain
    top_features = explain(features)

    return {
        "prediction": pred,
        "confidence": conf,
        "anomaly_score": loss,
        "risk_score": risk,
        "risk_level": level,
        "top_features": top_features
    }