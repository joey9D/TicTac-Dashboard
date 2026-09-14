


class AppState:
    def __init__(self):
        self.window = None
        self.scheduler = None
        self.scheduler_thread = None

# ------------------------------------------------------------------------
# singleton instance of AppState
# ------------------------------------------------------------------------
state = AppState()