# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

window = None
scheduler = None
scheduler_thread = None

# ------------------------------------------------------------------------
# Path to the UI file
# ------------------------------------------------------------------------

UI_MAIN = "Forms/TikTak.ui"
UI_ABOUT = "Forms/about.ui"

USE_GPIO = False

if USE_GPIO:
    import os
    os.environ['GPIOZERO_PIN_FACTORY'] = 'mock'
    from gpiozero import LED, Button