# -*- coding: utf-8 -*-

from GCS.Util.Util import *
from PyQt5.QtWidgets import *
from GCS.Common.CustomLabel import *
from GCS.Common.CustomLabelWhite import *


class StatusModule(QWidget):

    # #########################################################################################
    #   initialize
    # #########################################################################################
    def __init__(self):
        super(StatusModule, self).__init__()

        # 상태 레이아웃(라벨, 상태로그)
        self.status_layout = QVBoxLayout(self)

        # 라벨(타이틀) 생성 하세요(학생)
        self.title = '생성하세요'

        # 상태로그 위젯
        self.status_log_widget = QWidget(self)

        # 상태로그 레이아웃
        self.status_log_layout = QGridLayout(self.status_log_widget)

        # 타이틀 라벨 생성
        self.flight_controller = CustomLabelWhite(self.status_log_widget, name="Flight Controller")
        self.type = CustomLabelWhite(self.status_log_widget, name="Type")
        self.mode = CustomLabelWhite(self.status_log_widget, name="Mode")
        self.main_mode = CustomLabelWhite(self.status_log_widget, name="Main Mode")
        self.sub_mode = CustomLabelWhite(self.status_log_widget, name="Sub Mode")
        self.custom_mode = CustomLabelWhite(self.status_log_widget, name="Custom Mode")
        self.test = CustomLabelWhite(self.status_log_widget, name="Test")
        self.auto = CustomLabelWhite(self.status_log_widget, name="Auto")
        self.guided = CustomLabelWhite(self.status_log_widget, name="Guided")
        self.stabilize = CustomLabelWhite(self.status_log_widget, name="Stabilize")
        self.hil = CustomLabelWhite(self.status_log_widget, name="Hil")
        self.manual_input = CustomLabelWhite(self.status_log_widget, name="Manual Input")
        self.safety = CustomLabelWhite(self.status_log_widget, name="Safety")

        # 타이틀 라벨 Value 생성 하세요

        # UI 설정
        self.init_widget()

    # #########################################################################################
    #  Widget 초기화 및 설정
    # #########################################################################################
    def init_widget(self):

        # 레이아웃(self) 옵션 설정
        self.status_log_layout.setContentsMargins(10, 0, 0, 10)

        # Flight Controller 라벨 및 데이터 배치

        # Type 라벨 및 데이터 배치

        # Mode 라벨 및 데이터 배치

        # Main Mode 라벨 및 데이터 배치

        # Sub Mode 라벨 및 데이터 배치

        # Custom Mode 라벨 및 데이터 배치

        # Test 라벨 및 데이터 배치

        # Auto 라벨 및 데이터 배치

        # Guided 라벨 및 데이터 배치

        # Stabilize 라벨 및 데이터 배치

        # Hil 라벨 및 데이터 배치

        # Manual 라벨 및 데이터 배치

        # Safety 라벨 및 데이터 배치

        # 위젯(타이틀 라벨, 상태로그 위젯) > 레이아웃
        # self.title 을 배치 하세요

        self.status_layout.addWidget(self.status_log_widget)
        self.status_layout.setContentsMargins(0, 0, 0, 0)

        # 화면에 display 처리
        self.setLayout(self.status_layout)
        self.setStyleSheet(STATUS_WIDGET_COLOR)
        self.setMinimumSize(STATUS_WIDTH, STATUS_TEXT_HEIGHT)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = StatusModule()
    main.show()
    sys.exit(app.exec_())
