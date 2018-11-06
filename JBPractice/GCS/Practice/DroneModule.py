# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui
from GCS.Common.CustomLabel import *
from GCS.Common.CustomLabelWhite import *
from PyQt5.QtWidgets import *
from GCS.Util.Util import *


class DroneModule(QWidget):

    # #########################################################################################
    #   initialize
    # #########################################################################################
    def __init__(self,):

        super(DroneModule, self).__init__()

        # 상태 레이아웃(라벨, 드론 및 접속 정보)
        self.drone_layout = QVBoxLayout()
        
        # 라벨(타이틀) 생성
        self.title = CustomLabel(width=CONTROL_WIDTH, name="  ▶  DRONE", color="B")

        # 드론 이미지
        self.drone_img = QLabel()

        # 드론 및 접속정보 위젯
        self.drone_widget = QWidget()

        # 드론 및 접속정보 merge 레이아웃
        self.drone_info_layout = QHBoxLayout(self.drone_widget)

        # 접속정보 레이아웃
        self.info_layout = QGridLayout()

        # 타이틀 라벨 생성
        self.flight_control = CustomLabelWhite(self, name="Flight Controller")

        self.flight_status = CustomLabelWhite(self, name="Flight Status")

        self.flight_speed = CustomLabelWhite(self, name="Flight Speed")

        self.connected_port = CustomLabelWhite(self, name="Connected Port")

        self.connected_baud = CustomLabelWhite(self, name="Connected BaudRate")

        self.flight_control_val = CustomLabelWhite(self, name="N/A")

        self.flight_status_val = CustomLabelWhite(self, name="N/A")

        self.flight_speed_val = CustomLabelWhite(self, name="N/A")

        self.connected_port_val = CustomLabelWhite(self, name="N/A")

        self.connected_baud_val = CustomLabelWhite(self, name="N/A")

        # UI 설정
        self.init_widget()

    # #########################################################################################
    #  Widget 초기화 및 설정
    # #########################################################################################
    def init_widget(self):

        # 드론 이미지 설정 및 위치 지정
        self.drone_img.setPixmap(QtGui.QPixmap(IMG_PATH+"drone_off.png"))

        self.info_layout.addWidget(self.flight_control, 0, 0)

        self.info_layout.addWidget(self.flight_control_val, 0, 1)

        self.info_layout.addWidget(self.flight_status, 1, 0)

        self.info_layout.addWidget(self.flight_status_val, 1, 1)

        self.info_layout.addWidget(self.flight_speed, 2, 0)

        self.info_layout.addWidget(self.flight_speed_val, 2, 1)

        self.info_layout.addWidget(self.connected_port, 3, 0)

        self.info_layout.addWidget(self.connected_port_val, 3, 1)

        self.info_layout.addWidget(self.connected_baud, 4, 0)

        self.info_layout.addWidget(self.connected_baud_val, 4, 1)

        # 드론 이미지 및 접속 정보 레이아웃 > Merge 레이아웃
        self.drone_info_layout.addWidget(self.drone_img)
        self.drone_info_layout.setStretchFactor(self.drone_img, 30)
        self.drone_info_layout.addLayout(self.info_layout)
        self.drone_info_layout.setStretchFactor(self.info_layout, 70)

        # 위젯(타이틀 라벨, 드론 및 접속 정보 위젯) > 레이아웃
        self.drone_layout.addWidget(self.title)
        self.drone_layout.addWidget(self.drone_widget)
        self.drone_layout.setContentsMargins(0, 0, 0, 0)

        # 화면에 display 처리
        self.setLayout(self.drone_layout)
        self.setStyleSheet(CONTROL_WIDGET_COLOR)
        self.setMinimumSize(CONTROL_WIDTH, DRONE_HEIGHT)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DroneModule()
    main.show()
    sys.exit(app.exec_())
