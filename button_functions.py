# import app_state as state
from PySide6.QtCore import QObject, QTimer, Slot, Signal

# ------------------------------------------------------------------------
# Button functions
# ------------------------------------------------------------------------
class SlotController(QObject):
    output_toggled = Signal(int, bool)
    
    def __init__(self, window, outputs):
        super().__init__()
        self.window = window
        self.outputs = outputs

        # Timer anlegen und starten -> ruft update_toggle_locks() periodisch auf
        self.lock_timer = QTimer(self)
        self.lock_timer.setInterval(150)  # alle 150ms, Wert nach Bedarf anpassen
        self.lock_timer.timeout.connect(self.update_toggle_locks)
        self.lock_timer.start()

    def update_toggle_locks(self):
        for i, output in enumerate(self.outputs, start=1):
            toggle = getattr(self.window, f"toggle_Button{i}")
            locked = output.owner == "scheduler"
            toggle.setEnabled(not locked)
            toggle.setLocked(locked)

    def toggle_all_manual(self, checked):
        for i in range(1, len(self.outputs) + 1):
            toggle = getattr(self.window, f"toggle_Button{i}")
            if toggle.isEnabled():
                toggle.setChecked(checked)

    @Slot(int, bool)
    def toggle_Button_manual(self, value, checked):
        idx = value - 1
        output = self.outputs[idx]
              
        if checked:
            if not output.claim("manual"):
                toggle = getattr(self.window, f"toggle_Button{value}")
                toggle.blockSignals(True)
                toggle.setChecked(False)
                toggle.blockSignals(False)
                return
            
            # output.start()
            output.set_manual(True)
            getattr(self.window, f"lbl_ManualLed_Out{value}").setStyleSheet("background-color: red;")
            getattr(self.window, f"l_RunState{value}").setStyleSheet("background-color: #ff9725; color: black")
            getattr(self.window, f"l_RunState{value}").setText("Manual")
            getattr(self.window, f"lbl_OutputLed{value}").setStyleSheet("background-color: #ff9725;")
            self.output_toggled.emit(value, True)
            
        else:
            if output.owner != "manual":
                return
            
            # output.stop()
            output.set_manual(False)
            output.release("manual")
            getattr(self.window, f"lbl_ManualLed_Out{value}").setStyleSheet("background-color: green;")
            getattr(self.window, f"l_RunState{value}").setStyleSheet("background-color: green; color: black")
            getattr(self.window, f"l_RunState{value}").setText("Stopped")
            getattr(self.window, f"lbl_OutputLed{value}").setStyleSheet("background-color: green;")
            self.output_toggled.emit(value, False)


    @Slot(int, list)
    def start_Button(self, value, outputs):
        if 1 <= value <= len(outputs):
            output = self.outputs[value-1]
            
            if not output.claim("scheduler"):
                return
            
            on_time = getattr(self.window, f"sB_OnTime{value}").value() / 1000
            off_time = getattr(self.window, f"sB_OffTime{value}").value() / 1000
            output.setTiming(on_time, off_time)
            output.start()
            getattr(self.window, f"l_RunState{value}").setStyleSheet("background-color: red; color: black")
            getattr(self.window, f"l_RunState{value}").setText("Running")
            getattr(self.window, f"lbl_OutputLed{value}").setStyleSheet("background-color: red;")
            getattr(self.window, f"lbl_ManualLed_Out{value}").setStyleSheet("background-color: #ff9725;")


    @Slot(int, list)
    def stop_Button(self, value, outputs):
        if 1 <= value <= len(outputs):
            output = self.outputs[value-1]
            
            if output.owner == "manual":
                return
            
            output.stop()
            output.release("scheduler")
            getattr(self.window, f"l_RunState{value}").setStyleSheet("background-color: green; color: black")
            getattr(self.window, f"l_RunState{value}").setText("Stopped")
            getattr(self.window, f"lbl_OutputLed{value}").setStyleSheet("background-color: green;")
            getattr(self.window, f"lbl_ManualLed_Out{value}").setStyleSheet("background-color: green;")


    @Slot(int, list)
    def clear_Button(self, value, outputs):
        if 1 <= value <= len(outputs):
            self.outputs[value-1].clear()
            getattr(self.window, f"lbl_OutputCnt{value}").setText("0")
            getattr(self.window, f"l_CntOutVal{value}").setText("0")
            getattr(self.window, f"lbl_InputCnt{value}").setText("0")
            getattr(self.window, f"l_CntInVal{value}").setText("0")


    @Slot(int,int)
    def update_output_counter(self, number, count):
        label = getattr(self.window, f"l_CntOutVal{number}")
        label_led = getattr(self.window, f"lbl_OutputCnt{number}")
        label.setText(str(count))
        label_led.setText(str(count))
        diffVal = getattr(self.window, f"sB_DiffAbort{number}").value()
        inVal = int(getattr(self.window, f"l_CntInVal{number}").text())
        
        iodiff = count - inVal
        if diffVal != 0 and iodiff > diffVal:
            self.stop_Button(number, self.outputs)


    @Slot(list)
    def start_all(self, outputs):
        for i in range(1, (len(outputs)+1)):
            self.start_Button(i, outputs)


    @Slot(list)
    def stop_all(self, outputs):
        for i in range(1, (len(outputs)+1)):
            self.stop_Button(i, outputs)


    @Slot(list, list)
    def clear_all(self, outputs, inputs):
        # Clear output counters
        for i, output in enumerate(outputs, start=1):
            output.clear()
            getattr(self.window, f"lbl_OutputCnt{i}").setText("0")
            getattr(self.window, f"l_CntOutVal{i}").setText("0")

        # Clear input counters
        for i, input_channel in enumerate(inputs, start=1):
            input_channel.clear()
            getattr(self.window, f"l_CntInVal{i}").setText("0")
            getattr(self.window, f"lbl_InputCnt{i}").setText("0")



    @Slot(int, int)
    def update_input_counter(self, number, count):
        labelLed = getattr(self.window, f"l_RunState{number}")
        labelLed.setText(str(count))
        label = getattr(self.window, f"l_CntInVal{number}")
        label.setText(str(count))
        label_led = getattr(self.window, f"lbl_InputCnt{self.number}")
        label_led.setText(str(count))
        
    @Slot(int, int)
    def goto_tab(self, tab_index):
        self.window.tabWidget.setCurrentIndex(tab_index)