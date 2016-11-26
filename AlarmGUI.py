from PyQt5 import QtWidgets, QtGui, QtCore
import sys, signal, os
import AlarmEventHandler
import AudioModule
########################## START BUILDING THE CLASS##########################


class GUI(QtWidgets.QWidget):
    def __init__(self):
        super(GUI, self).__init__()
        self.setWindowTitle('Alarm Clock')
        self.setGeometry(100, 100, 300, 210)
        self.setWindowIcon(QtGui.QIcon('alarm-clock-icon.png'))
        self.setStyleSheet('background-color: #00b300')
        self.setFixedSize(300, 210)
        self.show()
        self.all_widgets = []

    def add_time(self, from_time, to_time, x, y):
        time_ = QtWidgets.QComboBox(self)
        time_.setGeometry(x, y, 50, 50)
        time_.setStyleSheet('border: 2px solid black;'
                            'background-color: #33ccff;'
                            'border-radius: 5px;'
                            'font-size: 18px')
        for i in range(from_time, to_time):
            time_.addItem(format_with_zero(i))
        time_.show()
        self.all_widgets.append(time_)

    def add_label(self, name_, x, y, width=50):
        label = QtWidgets.QLabel(name_, self)
        label.setGeometry(x, y, width, 20)
        label.setStyleSheet('border: 2px solid black;'
                            'background-color: lightgreen;'
                            'border-radius: 5px;'
                            'font-size: 15px')
        label.show()
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.all_widgets.append(label)

    def add_button(self,icon_path, text, x, y):
        btn = QtWidgets.QPushButton(self)
        btn.setGeometry(x, y, 50, 50)
        btn.setIcon(QtGui.QIcon(icon_path))
        btn.setIconSize(QtCore.QSize(40, 40))
        btn.show()
        btn.setStyleSheet('border-radius: 10px;\
                           border: 2px solid black;')

        self.all_widgets.append(btn)

    def add_button_event(self, btn, signal):
        btn.clicked.connect(signal)

    def add_ringtone_list(self):
        dd = QtWidgets.QComboBox(self)
        dd.setGeometry(95, 180, 110, 20)
        dd.addItem('Bird')
        dd.addItem('Bird 2')
        dd.addItem('Mario')
        dd.addItem('Rooster')
        dd.addItem('None')
        dd.setStyleSheet('border: 2px solid black;'
                            'background-color: #33ccff;'
                            'border-radius: 5px;'
                            'font-size: 15px')
        dd.show()
        self.all_widgets.append(dd)

    def closeEvent(self, QCloseEvent):
        pid = os.getpid()
        os.kill(pid, signal.SIGKILL)

def format_with_zero(str_):
    result = str(str_)
    if len(result) is 1:
        result = '0' + result
    return result


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a_clock = GUI()
    a_clock.add_time(from_time=0, to_time=24, x=95, y=35)
    a_clock.add_time(from_time=0, to_time=60, x=155, y=35)

    a_clock.add_label(name_='HH' , x=95, y=10)
    a_clock.add_label(name_='MM', x=155, y=10)


    a_clock.add_button(icon_path='./Icon/play.png', text='Start', x=95, y=90)
    a_clock.add_button(icon_path='./Icon/stop.png', text='Stop', x=155, y=90)

    a_clock.add_label('Alarm Tone', 95, 150, width=110)
    a_clock.add_ringtone_list()

    a_clock.all_widgets[5].setEnabled(False)

    am = AudioModule.PlayTone(a_clock.all_widgets[7])
    a_clock.all_widgets[7].currentIndexChanged.connect(am.play)

    # Create Signals
    cm = AlarmEventHandler.ControllerMenu(a_clock)
    play = cm.play
    pause = cm.stop

    a_clock.add_button_event(a_clock.all_widgets[4], play)
    a_clock.add_button_event(a_clock.all_widgets[5], pause)

    sys.exit(app.exec_())