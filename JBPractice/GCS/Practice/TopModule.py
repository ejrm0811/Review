# -*- coding: utf-8 -*-
# 위젯 배치부터 생각하기.
#
from GCS.Util.Util import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtSerialPort import QSerialPortInfo
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QWidget, QApplication
from GCS.Common.CustomButton import CustomButton
from GCS.Common.CustomComboBox import CustomComboBox
from GCS.Serial.SerialConfig import SerialConfig


# 해당 OS 추출
__platform__ = sys.platform


class TopModule(QWidget):

    def __init__(self):

        super(TopModule, self).__init__()

        # 위젯들(로고,포트,보드레이트,접속버튼) > 레이아웃
        self.top_layout = QHBoxLayout()

        # 로고 위젯
        self.logo = QLabel()

        # 접속 포트 콤보박스
        self.port_name = CustomComboBox(self, 300, 35)

        # 접속 보드레이트 콤보박스
        self.baud_rate = CustomComboBox(self, 200, 35)

        # 시리얼 접속 버튼 위젯
        self.btn_connect = CustomButton(self, 130, 35, "Connect")

        # PORT 새로고침 버튼 위젯
        self.btn_refresh = CustomButton(self, 130, 35, "ReFresh")

        # UI 설정
        self.init_widget()

    def init_widget(self):

        # 로고 이미지 설정 옵션
        self.logo.setPixmap(QPixmap(IMG_PATH + "logo.png"))

        # 포트,보드레이트,접속 버튼 데이터(콤보박스) 설정
        self._fill_serial_info()

        # 위젯 배치(로고,포트,보드레이트,접속버튼)
        self.top_layout.addWidget(self.logo)
        self.top_layout.addWidget(self.port_name)
        self.top_layout.addWidget(self.baud_rate)
        self.top_layout.addWidget(self.btn_connect)
        self.top_layout.addWidget(self.btn_refresh)

        # 화면에 display 처리
        self.setLayout(self.top_layout) # setlayout : 최종적으로 화면에 도출
        self.setStyleSheet(TOP_WIDGET_COLOR)
        self.setMinimumSize(WIN_WIDTH, LOGO_HEIGHT)

    # 시리얼 상수 값들을 포트, 보드레이트에 값을 넣고 접속 버튼은 시그널 처리
    def _fill_serial_info(self):

        # 시리얼 포트 및 보드레이터 초기화
        self.port_name.clear()
        self.baud_rate.clear()

        # 포트 및 보드레이터 설정
        self.port_name.insertItems(0, self._get_available_port())
        self.baud_rate.insertItems(0, [str(x) for x in SerialConfig.BAUDRATES])

        # port 맨 마지막 인덱스로 설정
        self.port_name.setCurrentIndex(self.port_name.count() - 1)

        # default boud rate 설정(115200)
        self.baud_rate.setCurrentIndex(7)

    # 사용가능한 포트 조회
    def _get_available_port(self):
        result = []

        for port in QSerialPortInfo().availablePorts():

            result.append(port.portName() if __platform__.startswith('win') else "/dev/" + port.portName())

        return result


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TopModule()
    main.show()
    sys.exit(app.exec_())
