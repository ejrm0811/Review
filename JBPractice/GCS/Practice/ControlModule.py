# -*- coding: utf-8 -*-
# 어떤 레이아웃과 위젯을 배치해야 하는가를 결정한다.
from PyQt5.QtWidgets import *
from GCS.Common.CustomImgButton import CustomImgButton
from GCS.Common.CustomLabel import *
from GCS.Util.Util import *


class ControlModule(QWidget):

    # #########################################################################################
    #   initialize
    # #########################################################################################
    def __init__(self):
        super(ControlModule, self).__init__()

        # Controller 레이아웃(라벨,버튼 위젯) - 최종 레이아웃.
        self.control_layout = QVBoxLayout()

        # 라벨(타이틀) 생성 - 위젯 생성.
        self.title = CustomLabel(width=CONTROL_WIDTH, name="  ▶  CONTROLLER", color="B")

        # 컨트롤 위젯
        self.control_btn_widget = QWidget()

        # 컨트롤 레이아웃 - 그리드 레이아웃.(행과 열을 갖는 레이아웃.)
        self.control_btn_layout = QGridLayout(self.control_btn_widget)

        take_off = IMG_PATH + "drone_btn_1.png"

        landing = IMG_PATH + "drone_btn_5.png"

        flight_start = IMG_PATH + "drone_btn_7.png"

        rtl = IMG_PATH + "drone_btn_6.png"

        arming = IMG_PATH + "drone_btn_2.png"

        dis_arming = IMG_PATH + "drone_btn_3.png"

        # 컨트롤 버튼 생성
        self.btn_take_off = CustomImgButton(self.control_btn_widget, 171, 41, "Take Off", take_off)

        self.btn_landing = CustomImgButton(self.control_btn_widget, 171, 41, "   Landing     ", landing)

        self.btn_flight_start = CustomImgButton(self.control_btn_widget, 171, 41, " Flight Start ", flight_start)

        self.btn_rtl = CustomImgButton(self.control_btn_widget, 171, 41, "Return Home", rtl)

        self.btn_arming = CustomImgButton(self.control_btn_widget, 171, 41, "Arming", arming)

        self.btn_dis_arming = CustomImgButton(self.control_btn_widget, 171, 41, "  DisArming  ", dis_arming)

        self.init_widget()

    # #########################################################################################
    #  Widget 초기화 및 설정(실제 레이아웃에 배치)
    # #########################################################################################
    def init_widget(self):

        # 버튼 위젯 > 레이아웃 배치
        self.control_btn_layout.addWidget(self.btn_take_off, 0, 0)

        self.control_btn_layout.addWidget(self.btn_landing, 0, 1)

        self.control_btn_layout.addWidget(self.btn_flight_start, 1, 0)

        self.control_btn_layout.addWidget(self.btn_rtl, 1, 1)

        self.control_btn_layout.addWidget(self.btn_arming, 2, 0)

        self.control_btn_layout.addWidget(self.btn_dis_arming, 2, 1)

        # 위젯(타이틀, 컨트롤 버튼) > 레이아웃
        self.control_layout.addWidget(self.title)

        self.control_layout.addWidget(self.control_btn_widget)

        self.control_layout.setContentsMargins(0, 0, 0, 0)

        # 화면에 display 처리
        self.setLayout(self.control_layout)
        self.setStyleSheet(CONTROL_WIDGET_COLOR)
        self.setMinimumSize(CONTROL_WIDTH, CONTROL_HEIGHT)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    main = ControlModule()
    main.show()
    sys.exit(app.exec_())
