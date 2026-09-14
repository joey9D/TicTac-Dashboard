import globals as g
import time

class OutputChannel:

    def __init__(self, gpio, on_time=0.5, off_time=0.5):
        self.gpio = gpio
        self.on_time = on_time
        self.off_time = off_time
        self.running = False
        self.state = False
        self.owner = None
        self.counter = 0
        self.next_change = 0
        if g.USE_GPIO:
            self.led = g.LED(gpio)
        else:
            print(f"Init OutputChannel GPIO {self.gpio}")


    def claim(self, owner):
        if self.owner is None or self.owner == owner:
            self.owner = owner
            return True
        return False
    
    
    def release(self, owner):
        if self.owner == owner:
            self.owner = None
            return True
        return False


    def start(self):
        self.running = True
        self.state = False
        self.next_change = time.monotonic()


    def stop(self):
        self.running = False
        self.state = False
        if g.USE_GPIO:
            self.led.off()


    def clear(self):
        self.counter = 0


    def setTiming(self, on_time, off_time):
        self.on_time = on_time
        self.off_time = off_time


    def update(self):
        if not self.running:
            return None

        now = time.monotonic()

        if now >= self.next_change:
            if self.state:
                # Falling edge
                if g.USE_GPIO:
                    self.led.off()
                self.state = False
                self.next_change = now + self.off_time
            else:
                # Rising edge
                if g.USE_GPIO:
                    self.led.on()
                self.state = True
                self.counter += 1
                self.next_change = now + self.on_time
                return self.counter

        return None


    def close(self):
        if g.USE_GPIO:
            self.led.off()
            self.led.close()
        else:
            print(f"Close OutputChannel GPIO {self.gpio}")
        pass