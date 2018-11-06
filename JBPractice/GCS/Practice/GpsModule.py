# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from GCS.Common.CustomLabel import *
from GCS.Common.CustomLabelWhite import *


class GpsModule(QWidget):

    # #########################################################################################
    #   initialize
    # #########################################################################################
    def __init__(self):
        
        super(GpsModule, self).__init__()

        # 상태 레이아웃(라벨, 상태로그)
        self.status_layout = QVBoxLayout(self)

        # 라벨(타이틀) 생성
        self.title = CustomLabel(self, width=CONTROL_WIDTH, name="  ▶  GPS", color="G")

        # 상태로그 위젯
        self.gps_widget = QWidget(self)

        # 상태로그 레이아웃
        self.gps_layout = QGridLayout(self.gps_widget)

        # 타이틀 라벨 생성
        self.fix = CustomLabelWhite(self.gps_widget, name="Fix")

        self.count = CustomLabelWhite(self.gps_widget, name="Count")

        self.alt = CustomLabelWhite(self.gps_widget, name="Altitude")

        self.lng = CustomLabelWhite(self.gps_widget, name="Longitude")

        self.h_dop = CustomLabelWhite(self.gps_widget, name="HDOP")

        self.v_dop = CustomLabelWhite(self.gps_widget, name="VDOP")

        # 타이틀 라벨 생성(타이틀 라벨을 가지고 value 라벨을 생성)

        # UI 설정
        self.init_widget()

    # #########################################################################################
    #  Widget 초기화 및 설정
    # #########################################################################################
    def init_widget(self):

        # 레이아웃(self) 옵션 설정
        self.gps_layout.setContentsMargins(10, 0, 0, 10)

        #  Fix 라벨 및 데이터 배치(학생)

        # Count 라벨 및 데이터 배치(학생)

        # Alt 라벨 및 데이터 배치(학생)

        # Lng 라벨 및 데이터 배치(학생)

        # H-dop 라벨 및 데이터 배치(학생)

        # V-dop 라벨 및 데이터 배치(학생)

        # 위젯(타이틀 라벨, 상태로그 위젯) > 레이아웃
        self.status_layout.addWidget(self.title)

        # self.gps_widget 배치하세요(학생)

        self.status_layout.setContentsMargins(0, 0, 0, 0)

        # 화면에 display 처리
        self.setLayout(self.status_layout)

        # 위젯 색상 입력하세요(학생)

        self.setMinimumSize(STATUS_WIDTH, GPS_HEIGHT)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = GpsModule()
    main.show()
    sys.exit(app.exec_())
