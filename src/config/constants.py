"""
====================================================
VisionWork AI
Constants
====================================================
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = ROOT / "data"

IMAGE_DIR = DATA_DIR / "images"

VIDEO_DIR = DATA_DIR / "videos"

LABEL_DIR = DATA_DIR / "labels"

DATASET_DIR = DATA_DIR / "datasets"

OUTPUT_DIR = ROOT / "outputs"

LOG_DIR = ROOT / "logs"

ASSET_DIR = ROOT / "assets"

WEIGHT_DIR = ROOT / "weights"

DOC_DIR = ROOT / "docs"

TEST_DIR = ROOT / "tests"

CONFIG_DIR = ROOT / "configs"

for folder in [

OUTPUT_DIR,

LOG_DIR,

ASSET_DIR,

WEIGHT_DIR,

DOC_DIR,

CONFIG_DIR,

]:

    folder.mkdir(exist_ok=True)