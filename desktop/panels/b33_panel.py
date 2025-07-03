# desktop/panels/b33_panel.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
import requests

BACKEND_URL = "http://localhost:8000"  # Passe ggf. Port an

class B33Panel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.info = QLabel("B33 KI-Panel")
        self.train_btn = QPushButton("Trainieren")
        self.predict_btn = QPushButton("Vorhersage")
        self.output = QTextEdit()

        self.train_btn.clicked.connect(self.train_b33)
        self.predict_btn.clicked.connect(self.predict_b33)

        layout.addWidget(self.info)
        layout.addWidget(self.train_btn)
        layout.addWidget(self.predict_btn)
        layout.addWidget(self.output)
        self.setLayout(layout)

    def train_b33(self):
        data = {
            "X": [[1,2],[2,3],[3,4]],
            "y": [10, 20, 30],
            "params": {"window": 14}
        }
        try:
            r = requests.post(f"{BACKEND_URL}/api/ml/b33/train", json=data, timeout=5)
            self.output.append(f"Train: {r.json()}")
        except Exception as e:
            self.output.append(f"Fehler beim Training: {e}")

    def predict_b33(self):
        data = {"X": [[5,6],[6,7]]}
        try:
            r = requests.post(f"{BACKEND_URL}/api/ml/b33/predict", json=data, timeout=5)
            self.output.append(f"Predict: {r.json()}")
        except Exception as e:
            self.output.append(f"Fehler bei Vorhersage: {e}")
