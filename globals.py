from pathlib import Path

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------
APP_VERSION = "0.0.1"

window = None
scheduler = None
scheduler_thread = None

# ------------------------------------------------------------------------
# Path to the UI file
# ------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
IMG_LOGO = BASE_DIR / "images" / "logo.png"
UI_MAIN  = BASE_DIR / "Forms" / "TikTak.ui"
UI_ABOUT = BASE_DIR / "Forms" / "about.ui"

USE_GPIO = False #False

if USE_GPIO:
    import os
    os.environ['GPIOZERO_PIN_FACTORY'] = 'mock' #'lgpio'
    from gpiozero import LED, Button