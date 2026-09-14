# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

window = None
scheduler = None
scheduler_thread = None

USE_GPIO = False

if USE_GPIO:
    import os
    os.environ['GPIOZERO_PIN_FACTORY'] = 'mock'
    from gpiozero import LED, Button