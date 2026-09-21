# This Python file uses the following encoding: utf-8
import sys
import time
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice, QObject, QThread, Signal
from functools import partial
from animated_toggle import AnimatedToggle

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------
import globals as g

# ------------------------------------------------------------------------
# window state of the application
# ------------------------------------------------------------------------
import app_state as state

# ------------------------------------------------------------------------
# Input Channel
# ------------------------------------------------------------------------
import inputchannel as ic

# ------------------------------------------------------------------------
# Output Channel
# ------------------------------------------------------------------------
import outputchannel as oc

# ------------------------------------------------------------------------
# Scheduler
# ------------------------------------------------------------------------

class OutputScheduler(QObject):
    countChanged = Signal(int, int)


    def __init__(self, outputs):
        super().__init__()
        self.outputs = outputs
        self.running = True


    def run(self):
        while self.running:
            for index, output in enumerate(self.outputs):
                if output.owner == "manual":
                    continue
                
                cnt = output.update()
                if cnt is not None:
                    self.countChanged.emit(index + 1, cnt)

            # sleep 1 msec
            time.sleep(0.001)

    def stop(self):
        self.running = False
        for output in self.outputs:
            output.close()


# ------------------------------------------------------------------------
# Button functions
# ------------------------------------------------------------------------
import button_functions as bf


# ------------------------------------------------------------------------
# Main Function
# ------------------------------------------------------------------------
import mainwindow as mw


if __name__ == "__main__":

    app = QApplication(sys.argv)

    state.window = mw.MainWindow(g.UI_MAIN)
    state.window.show()

    # ------------------------------------------------------------
    # Create Outputs
    # ------------------------------------------------------------

    for i in range(1, 9):
        getattr(state.window, f"sB_OnTime{i}").setValue(300)
        getattr(state.window, f"sB_OffTime{i}").setValue(200)

    outputs = [
        oc.OutputChannel(17),
        oc.OutputChannel(27),
        oc.OutputChannel(22),
        oc.OutputChannel(10),

        oc.OutputChannel(9),
        oc.OutputChannel(11),
        oc.OutputChannel(5),
        oc.OutputChannel(6)
    ]

    # ------------------------------------------------------------------------
    # Create Input
    # ------------------------------------------------------------------------
    inputs = [
        ic.InputChannel(1, 18),
        ic.InputChannel(2, 23),
        ic.InputChannel(3, 24),
        ic.InputChannel(4, 25),

        ic.InputChannel(5, 8),
        ic.InputChannel(6, 7),
        ic.InputChannel(7, 12),
        ic.InputChannel(8, 16)
    ]

    # ------------------------------------------------------------
    # Start scheduler thread
    # ------------------------------------------------------------
    controller = bf.SlotController(state.window, outputs)
    
    scheduler_thread = QThread()
    scheduler = OutputScheduler(outputs)
    scheduler.moveToThread(scheduler_thread)
    scheduler_thread.started.connect(scheduler.run)
    scheduler.countChanged.connect(controller.update_output_counter)
    
    for input in inputs:
        input.countChanged.connect(controller.update_input_counter)
        input.stateChanged.connect(controller.update_input_led)
    
    scheduler_thread.start()

    state.window.tabWidget.setCurrentIndex(0)

    # Reset all values
    # clear_all()

    # Tab Allgemein
    state.window.pB_StartAll.clicked.connect(lambda: controller.start_all(outputs))
    state.window.pB_StopAll.clicked.connect(lambda: controller.stop_all(outputs))
    state.window.pB_ClearAll.clicked.connect(lambda: controller.clear_all(outputs, inputs))
    
    for i in range(1, 9):
        getattr(state.window, f"pB_ButtonSettings{i}").clicked.connect(
            partial(controller.goto_tab, i)
        )

    # Tab Manuell
    state.window.toggle_All.toggled.connect(lambda checked: controller.toggle_all_manual(checked))

    # ------------------------------------------------------------------------
    # Connect output channels (Taster 1-8)
    # ------------------------------------------------------------------------
    for i in range(1, 9):
        getattr(state.window, f"toggle_Button{i}").toggled.connect(
                    partial(controller.toggle_Button_manual, i)
        )
        getattr(state.window, f"pB_Start{i}").clicked.connect(
            partial(controller.start_Button, i, outputs)
        )
        getattr(state.window, f"pB_Stop{i}").clicked.connect(
            partial(controller.stop_Button, i, outputs)
        )
        getattr(state.window, f"pB_Clear{i}").clicked.connect(
            partial(controller.clear_Button, i, outputs)
        )

    # ------------------------------------------------------------------------
    # Clean shutdown
    # ------------------------------------------------------------------------
    def shutdown():
        scheduler.stop()
        scheduler_thread.quit()
        scheduler_thread.wait()

        for input_channel in inputs:
            input_channel.close()

    app.aboutToQuit.connect(shutdown)

    sys.exit(app.exec())
