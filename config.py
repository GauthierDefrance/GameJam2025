# Sources/config.py

from pathlib import Path

# Dossier racine du projet (Sources)
BASE_DIR = Path(__file__).parent.resolve()

# Dossier Assets
ASSETS_DIR = BASE_DIR / 'assets'


# Constant

PLAYER_SPEED = 4
DEFAULT_PLAYER_DIRECTION = "right"
