from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, Property, QSequentialAnimationGroup
from PySide6.QtWidgets import QCheckBox
from PySide6.QtGui import QColor, QBrush, QPen, QPainter


class AnimatedToggle(QCheckBox):

    _transparent_pen = QPen(Qt.transparent)
    _light_grey_pen = QPen(Qt.lightGray)

    def __init__(
        self,
        parent=None,
        bar_color=Qt.gray,
        checked_color="#ff9725",
        handle_color=Qt.white,
        pulse_unchecked_color="#44999999",
        pulse_checked_color="#4400B0EE",
        locked_bar_color = "#860000",
        locked_handle_color = "#BD0000"
    ):
        super().__init__(parent)

        self._bar_brush = QBrush(bar_color)
        self._bar_checked_brush = QBrush(QColor(checked_color).lighter())
        self._handle_brush = QBrush(handle_color)
        self._handle_checked_brush = QBrush(QColor(checked_color))
        self._pulse_unchecked_animation = QBrush(QColor(pulse_unchecked_color))
        self._pulse_checked_animation = QBrush(QColor(pulse_checked_color))
        self._locked_bar_brush = QBrush(QColor(locked_bar_color))
        self._locked_handle_brush = QBrush(QColor(locked_handle_color))
        self._locked = False

        self.setContentsMargins(8, 0, 8, 0)
        self._handle_position = 0
        self._pulse_radius = 0

        self.animation = QPropertyAnimation(self, b"handle_position", self)
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setDuration(100)

        self.pulse_anim = QPropertyAnimation(self, b"pulse_radius", self)
        self.pulse_anim.setDuration(200)
        self.pulse_anim.setStartValue(10)
        self.pulse_anim.setEndValue(20)

        self.animations_group = QSequentialAnimationGroup()
        self.animations_group.addAnimation(self.animation)
        self.animations_group.addAnimation(self.pulse_anim)

        self.stateChanged.connect(self.setup_animation)

    def setLocked(self, locked):
        if self._locked != locked:
            self._locked = locked
            self.update()   # Neuzeichnen anstoßen

    def isLocked(self):
        return self._locked

    def sizeHint(self):
        return QSize(58, 45)

    def hitButton(self, pos):
        return self.contentsRect().contains(pos)

    def setup_animation(self, value):
        self.animations_group.stop()
        if value:
            self.animation.setEndValue(1)
        else:
            self.animation.setEndValue(0)
        self.animations_group.start()

    def paintEvent(self, e):
        contRect = self.contentsRect()
        handleRadius = round(0.24 * contRect.height())

        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        p.setPen(self._transparent_pen)
        barRect = contRect.adjusted(handleRadius, 0.35 * contRect.height(), -handleRadius, -0.35 * contRect.height())
        rounding = barRect.height() / 2

        trailLength = contRect.width() - 2 * handleRadius
        xPos = contRect.x() + handleRadius + trailLength * self._handle_position

        if self.pulse_anim.state() == QPropertyAnimation.Running:
            p.setBrush(self._pulse_checked_animation if self.isChecked() else self._pulse_unchecked_animation)
            p.drawEllipse(int(xPos - self._pulse_radius), int(barRect.center().y() - self._pulse_radius), int(2 * self._pulse_radius), int(2 * self._pulse_radius))

        if self._locked:
            p.setBrush(self._locked_bar_brush)
            p.drawRoundedRect(barRect, rounding, rounding)
            p.setBrush(self._locked_handle_brush)
        elif self.isChecked():
            p.setBrush(self._bar_checked_brush)
            p.drawRoundedRect(barRect, rounding, rounding)
            p.setBrush(self._handle_checked_brush)
        else:
            p.setBrush(self._bar_brush)
            p.drawRoundedRect(barRect, rounding, rounding)
            p.setPen(self._light_grey_pen)
            p.setBrush(self._handle_brush)

        if self.isChecked():
            p.setBrush(self._bar_checked_brush)
            p.drawRoundedRect(barRect, rounding, rounding)
            p.setBrush(self._handle_checked_brush)
        else:
            p.setBrush(self._bar_brush)
            p.drawRoundedRect(barRect, rounding, rounding)
            p.setPen(self._light_grey_pen)
            p.setBrush(self._handle_brush)

        p.drawEllipse(int(xPos - handleRadius), int(barRect.center().y() - handleRadius), int(2 * handleRadius), int(2 * handleRadius))

        p.end()

    @Property(float)
    def handle_position(self):
        return self._handle_position

    @handle_position.setter
    def handle_position(self, pos):
        self._handle_position = pos
        self.update()

    @Property(float)
    def pulse_radius(self):
        return self._pulse_radius

    @pulse_radius.setter
    def pulse_radius(self, pos):
        self._pulse_radius = pos
        self.update()


from PySide6.QtCore import QSize