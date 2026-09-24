import globals as g
from PySide6 import QtCore

class InputChannel(QtCore.QObject):
    countChanged = QtCore.Signal(int, int)          # Scheduler Coutner
    stateChanged = QtCore.Signal(int, bool)         # Scheduler: LED
    manualStateChanged = QtCore.Signal(int, bool)   # Manual: LED

    def __init__(self, number, gpio):
        super().__init__()

        self.number = number
        self.gpio = gpio
        self.counter = 0
        self.manual = False

        # pull_up=False:
        # inactive = LOW
        # active   = HIGH
        # when_pressed is therefore triggered on LOW -> HIGH
        if g.USE_GPIO:
            # Cathode, 50 ms debounce time
            self.button = g.Button(gpio, pull_up=False, bounce_time=0.05)
            # Called on the rising/active edge
            self.button.when_pressed = self._rising_edge
            self.button.when_released = self._falling_edge
        else:
            print(f"Init InputChannel GPIO {self.gpio}")

    def set_manual(self, on: bool):
        if on:
            self.manual = True
    
        self.manualStateChanged.emit(self.number, False)

    def _rising_edge(self):
        if self.manual:
            self.manualStateChanged.emit(self.number, True)
            return
        
        self.counter += 1
        # print(f"Input GPIO {self.gpio}: rising edge, count = {self.counter}")
        # Notify Qt
        # label = getattr(state.window, f"l_CntInVal{self.number}")
        # label.setText(str(self.counter))
        self.countChanged.emit(self.number, self.counter)
        self.stateChanged.emit(self.number, True)

    def _falling_edge(self):
        if self.manual:
            self.manualStateChanged.emit(self.number, False)
            self.manual = False
            return
        
        self.stateChanged.emit(self.number, False)

    def update(self):
        # Nothing required here.
        # gpiozero handles the edge detection asynchronously.
        pass

    def clear(self):
        self.counter = 0
        self.countChanged.emit(self.number, self.counter)

    def close(self):
        if g.USE_GPIO:
            self.button.close()
        else:
            print(f"Close InputChannel GPIO {self.gpio}")
        pass