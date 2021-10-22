from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QPushButton
from gui.ui_main import Ui_main_window
from gui.widgets import PyLeftButton


class MainFunctions:
    def __init__(self):
        super().__init__()

        self.ui = Ui_main_window()
        self.ui.setupUi(self)

    def setup_widgets(self):

        self.ui.user_picture.setStyleSheet(
            f"background-image: url(':/myresource/resource/4ktube_small_icon.png'); background-position: center;")

        self.toggle_btn = PyLeftButton(
            "Hide Menu",
            icon_name=":/myresource/resource/icon_menu.png"
        )

        self.home_btn = PyLeftButton(
            "Home",
            icon_name=":/myresource/resource/icon_home.png",
            is_active=True
        )

        self.video = PyLeftButton(
            "Single Video",
            icon_name=":/myresource/resource/play-alt.png",
            is_active=True
        )

        self.playlist = PyLeftButton(
            "Whole Playlist",
            icon_name=":/myresource/resource/film.png",
            is_active=True
        )

        self.downloads = PyLeftButton(
            "Downloads",
            icon_name=":/myresource/resource/download.png",
            is_active=True
        )

        self.system_monitor = PyLeftButton(
            "System Monitor",
            icon_name=":/myresource/resource/pulse.png",
            is_active=True
        )

        self.about = PyLeftButton(
            "About",
            icon_name=":/myresource/resource/info.png",
            is_active=True
        )

        self.account = PyLeftButton(
            "Account",
            icon_name=":/myresource/resource/user.png",
            is_active=True
        )

        self.settings_btn = PyLeftButton(
            "Settings",
            icon_name=":/myresource/resource/icon_settings.png"
        )

        self.toggle_btn.clicked.connect(lambda: MainFunctions.toggle_button(self))
        self.home_btn.clicked.connect(lambda: MainFunctions.show_home(self, self.home_btn))
        self.settings_btn.clicked.connect(lambda: MainFunctions.show_settings(self, self.settings_btn))
        self.video.clicked.connect(lambda: MainFunctions.show_video(self, self.video))
        self.playlist.clicked.connect(lambda: MainFunctions.show_playlist(self, self.playlist))
        self.downloads.clicked.connect(lambda: MainFunctions.show_downloads(self, self.downloads))
        self.system_monitor.clicked.connect(lambda: MainFunctions.show_system_monitor(self, self.system_monitor))
        self.about.clicked.connect(lambda: MainFunctions.show_about(self, self.about))
        self.account.clicked.connect(lambda: MainFunctions.show_account(self, self.account))

        # Add Widgets To Menu
        self.ui.top_menu_layout.addWidget(self.toggle_btn)
        self.ui.top_menu_layout.addWidget(self.home_btn)

        self.ui.top_menu_layout.addWidget(self.video)
        self.ui.top_menu_layout.addWidget(self.playlist)
        self.ui.top_menu_layout.addWidget(self.downloads)
        self.ui.top_menu_layout.addWidget(self.system_monitor)
        self.ui.top_menu_layout.addWidget(self.account)
        self.ui.top_menu_layout.addWidget(self.about)

        self.ui.top_menu_layout.addWidget(self.settings_btn)
        MainFunctions.reset_selection(self)
        self.home_btn.set_active(True)

    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass

    def show_home(self, btn):
        MainFunctions.reset_selection(self)  # Deselect All Buttons
        self.ui.stackedWidget.setCurrentIndex(0)  # Change Page
        btn.set_active(True)  # Set Active Button

    def show_video(self, btn):
        MainFunctions.reset_selection(self)  # Deselect All Buttons
        self.ui.stackedWidget.setCurrentIndex(1)  # Change Page
        btn.set_active(True)  # Set Active Button

    def show_playlist(self, btn):
        MainFunctions.reset_selection(self)  # Deselect All Buttons
        self.ui.stackedWidget.setCurrentIndex(2)  # Change Page
        btn.set_active(True)  # Set Active Button

    def show_downloads(self, btn):
        MainFunctions.reset_selection(self)  # Deselect All Buttons
        self.ui.stackedWidget.setCurrentIndex(3)  # Change Page
        self.show_downloads_page()
        btn.set_active(True)  # Set Active Button

    def show_system_monitor(self, btn):
        MainFunctions.reset_selection(self)  # Deselect All Buttons
        self.ui.stackedWidget.setCurrentIndex(4)  # Change Page
        self.show_net_speed()
        btn.set_active(True)  # Set Active Button

    def show_about(self, btn):
        MainFunctions.reset_selection(self)  # Deselect All Buttons
        self.ui.stackedWidget.setCurrentIndex(6)  # Change Page
        btn.set_active(True)  # Set Active Button

    def show_account(self, btn):
        MainFunctions.reset_selection(self)  # Deselect All Buttons
        self.account_page()
        btn.set_active(True)  # Set Active Button

    def show_settings(self, btn):
        self.open_yt_setting_page()

    def toggle_button(self):
        # Get menu width
        menu_width = self.ui.left_menu.width()
        self.ui.stackedWidget.repaint()

        # Check with
        width = 60
        if menu_width == 60:
            width = 240

        # Start animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")

        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()
