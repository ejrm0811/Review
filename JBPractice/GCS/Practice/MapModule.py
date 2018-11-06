# -*- coding: utf-8 -*-


from GCS.Util.Util import *
from PyQt5 import QtCore
from PyQt5.QtWebChannel import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication


class MapModule(QWidget):

    # #########################################################################################
    #   initialize
    # #########################################################################################
    def __init__(self):
        super(MapModule, self).__init__()

        # 레이아웃(구글맵)
        self.map_layout = QVBoxLayout(self)

        # 웹 엔진
        self.engine_view = QWebEngineView()

        # 웹채널(웹페이지 뷰기능)
        self.web_channel = QWebChannel(self.engine_view.page())

        # UI 설정
        self.init_widget()

    # #########################################################################################
    #   Widget 초기화 및 설정
    # #########################################################################################
    def init_widget(self):

        # 현재 디렉토리 패스
        map_path = HTML_PATH+"map.Html"

        # 레이아웃 옵션 설정
        self.map_layout.setSpacing(0)
        self.map_layout.setContentsMargins(0, 0, 0, 0)

        # 웹뷰 > 웹엔진
        self.engine_view.page().setWebChannel(self.web_channel)

        # 엔진뷰 구글맵 페이지 로드 처리
        self.engine_view.load((QtCore.QUrl.fromLocalFile(map_path)))

        # 엔진뷰 > 레이아웃
        self.map_layout.addWidget(self.engine_view)

        # 화면에 display 처리
        self.setLayout(self.map_layout)
        self.setMinimumSize(MAP_WIDTH, CONTENTS_HEIGHT)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MapModule()
    main.show()
    sys.exit(app.exec_())
