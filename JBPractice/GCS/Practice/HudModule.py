# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from GCS.Util.Util import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebChannel import *
from GCS.Common.CustomLabel import *
from PyQt5.QtWebEngineWidgets import *


class FlightModule(QWidget):

    # #########################################################################################
    #   initialize
    # #########################################################################################
    def __init__(self):

        super(FlightModule, self).__init__()
        
        # 허드 레이아웃
        self.flight_layout = QVBoxLayout(self)

        # 라벨(타이틀) 생성
        self.title = CustomLabel(self, width=CONTROL_WIDTH, name="  ▶  HUD", color="G")

        # 웹 엔진
        self.hud_view = QWebEngineView(self)

        # 웹채널
        self.web_channel = QWebChannel(self.hud_view.page())

        # UI 설정
        self.init_widget()

    # #########################################################################################
    #  Widget 초기화 및 설정
    # #########################################################################################
    def init_widget(self):

        # 로컬 경로 패스
        hud_path = HUD_HTML_PATH + "hud.Html"

        # 레이아웃 옵션
        self.flight_layout.setSpacing(0)
        self.flight_layout.setContentsMargins(0, 0, 0, 0)

        # HUD 웹 페이지 설정 및 호출
        self.hud_view.page().setWebChannel(self.web_channel)
        self.hud_view.load(QtCore.QUrl.fromLocalFile(hud_path))

        # 웹페이지(허드) > 레이아웃(self)
        self.flight_layout.addWidget(self.title)
        self.flight_layout.addWidget(self.hud_view)

        # 화면에 display 처리
        self.setLayout(self.flight_layout)
        self.setStyleSheet(HUD_WIDGET_COLOR)
        self.setMinimumSize(STATUS_WIDTH, FLIGHT_HEIGHT)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = FlightModule()
    main.show()
    sys.exit(app.exec_())
