import ThreadHandler
import AudioModule


class ControllerMenu:
    def __init__(self, a_clock):
        self.a_clock = a_clock
        self.thread1 = None
        self.audio = AudioModule.PlayTone(a_clock.all_widgets[7])

    def play(self):
        self.thread1 = ThreadHandler.MyThread(int(self.a_clock.all_widgets[0].currentText()),
                                              int(self.a_clock.all_widgets[1].currentText()),
                                              self.audio)
        self.thread1.start()
        self.a_clock.all_widgets[4].setEnabled(False) # Disable Play Button
        self.a_clock.all_widgets[5].setEnabled(True)  # Enable Stop Button
        self.a_clock.all_widgets[0].setEnabled(False) # Disable Hour Drop Down
        self.a_clock.all_widgets[1].setEnabled(False) # # Disable Minute Drop Down

    def stop(self):
        self.a_clock.all_widgets[4].setEnabled(True)
        self.a_clock.all_widgets[5].setEnabled(False)
        self.a_clock.all_widgets[0].setEnabled(True)
        self.a_clock.all_widgets[1].setEnabled(True)
        self.audio.stop()