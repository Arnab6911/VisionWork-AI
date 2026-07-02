"""
====================================================
VisionWork AI
Settings
====================================================
"""

import torch
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

PROJECT_NAME = "VisionWork AI"

VERSION = "2.0"

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

MODEL_NAME = "yolo11n.pt"

MODEL_PATH = ROOT / "weights" / "yolo11n.pt"

CONFIDENCE_THRESHOLD = 0.45

IOU_THRESHOLD = 0.50

CAMERA_INDEX = 0

WINDOW_NAME = "VisionWork AI"

SHOW_FPS = True

SHOW_CONFIDENCE = True

BOX_THICKNESS = 2

FONT_SCALE = 0.6

FONT_THICKNESS = 2