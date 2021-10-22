from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt, QRect


class PyLeftButton(QPushButton):
    def __init__(
            self,
            text="",
            height=45,
            minimum_width=60,
            text_padding=65,
            text_color="#E0E1E3",
            icon_name="",
            icon_color="#c3ccdf",
            btn_color="#44475a",
            btn_hover="#233547",
            btn_pressed="#282a36",
            is_active=False
    ):
        super().__init__()

        # Set default parametros
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # Custom parameters
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_name = icon_name
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active

        """QPushButton {
              color: #E0E1E3;
              border-radius: 4px;
              padding: 5px;
              outline: none;
              border: none;
            }"""
        # # Set style
        self.set_style(
            text_padding=self.text_padding,
            text_color=self.text_color,
            btn_color=self.btn_color,
            btn_hover=self.btn_hover,
            btn_pressed=self.btn_pressed,
            is_active=self.is_active
        )

    def set_active(self, is_active_menu):
        self.set_style(
            text_padding=self.text_padding,
            text_color=self.text_color,
            btn_color=self.btn_color,
            btn_hover=self.btn_hover,
            btn_pressed=self.btn_pressed,
            is_active=is_active_menu
        )

    def set_style(
            self,
            text_padding=65,
            text_color="#E0E1E3",
            btn_color="#44475a",
            btn_hover="#233547",
            btn_pressed="#282a36",
            is_active=False
    ):
        style = f"""
        QPushButton {{
            color: {text_color};
            padding-left: {text_padding}px;
            text-align: left;
            border-radius: none;
        }}
        QPushButton:hover {{
            background-color: {btn_hover};
        }}
        QPushButton:pressed {{
            background-color: {btn_pressed};
        }}
        """

        active_style = f"""
        QPushButton {{
            border: 27px solid #c43128;
        }}
        """
        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)

    def paintEvent(self, event):
        QPushButton.paintEvent(self, event)
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)
        rect = QRect(0, 0, self.minimum_width, self.height())
        self.draw_icon(qp, self.icon_name, rect, self.icon_color)
        qp.end()

    def draw_icon(self, qp, image, rect, color):
        icon = QPixmap(image)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), Qt.lightGray)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()
