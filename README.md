# 🛡️ AI-Based Intrusion Detection System (AI-IDS)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)

An AI-powered Intrusion Detection System that monitors network traffic
in real time and detects anomalous or malicious activity using machine
learning and deep learning techniques.

## Features

-   Real-time network packet monitoring
-   Autoencoder-based anomaly detection
-   Random Forest attack classification
-   FastAPI backend for alerts
-   Modular pipeline architecture

## Architecture

Network Traffic → Packet Capture → Feature Extraction → Feature Scaling
→ Autoencoder → Random Forest → Alert Manager → FastAPI Backend →
Dashboard

## Project Structure

ai_ids/ ├── data/ ├── models/ ├── preprocessing/ ├── training/ ├──
realtime/ ├── backend/ ├── dashboard/ ├── requirements.txt └──
run_pipeline.py

## Installation

1.  Clone the repository
2.  Create virtual environment
3.  Install dependencies
4.  Install Wireshark (TShark + Npcap)

## Training

Train Autoencoder: python training/train_autoencoder.py

Train Classifier: python training/train_classifier.py

## Running the IDS

Start Backend: uvicorn backend.app.main:app --reload

Start Realtime Detection: python -m realtime.traffic_capture

## Dataset

CICIDS2017 Dataset https://www.unb.ca/cic/datasets/ids-2017.html

## Author

AI-Based Intrusion Detection System Project
