from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QGraphicsDropShadowEffect
)
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QTimer, QSize, pyqtSignal, QObject
import threading

from pilot import main


class SizeAnimator(QObject):
    sizeChanged = pyqtSignal(QSize)

    def animate(self, size, delay=0):
        QTimer.singleShot(
            delay,
            lambda: self.sizeChanged.emit(size)
        )


class PilotUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Pilot AI")
        self.setGeometry(80, 80, 400, 400)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Microphone animation
        self.mic_label = QLabel(self)

        self.add_gif_to_label(
            self.mic_label,
            "cbe227_fb70e39e9dd94e30bbe30c48b2367dd8~mv2.gif",
            size=(720, 220),
            alignment=Qt.AlignCenter
        )

        self.mic_label.setAlignment(Qt.AlignCenter)
        self.mic_label.mousePressEvent = self.start_listening

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(
            self.mic_label,
            alignment=Qt.AlignCenter
        )

        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        self.is_listening = False

        self.size_animator = SizeAnimator()
        self.size_animator.sizeChanged.connect(
            self.mic_label.setFixedSize
        )

    def add_gif_to_label(
        self,
        label,
        gif_path,
        size=None,
        alignment=None
    ):
        movie = QMovie(gif_path)

        label.setMovie(movie)

        self.movie = movie
        movie.start()

        if size:
            label.setFixedSize(*size)

        if alignment:
            label.setAlignment(alignment)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)

        label.setGraphicsEffect(shadow)

    def start_listening(self, event):
        if self.is_listening:
            return

        self.is_listening = True

        worker = threading.Thread(
            target=self.run_pilot,
            daemon=True
        )

        worker.start()

    def run_pilot(self):
        try:
            main()

        except Exception as error:
            print(f"Pilot AI error: {error}")

        finally:
            self.is_listening = False


def UI():
    app = QApplication([])

    pilot_ui = PilotUI()
    pilot_ui.showFullScreen()

    app.exec_()


if __name__ == "__main__":
    UI()