# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from GCS.Util.Util import *
from GCS.Common.CustomLabel import *
from GCS.Common.CustomButton import CustomButton
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QTableWidget, QVBoxLayout, QWidget, QHBoxLayout, QAbstractItemView


class WaypointModule(QWidget):

    # #########################################################################################
    #   initialize
    # #########################################################################################
    def __init__(self):

        super(WaypointModule, self).__init__()

        # 상태 레이아웃(라벨, 버튼, 테이블)
        self.waypoint_layout = QVBoxLayout(self)

        # 라벨(타이틀) 생성
        self.title = CustomLabel(self, width=CONTROL_WIDTH, name="  ▶  DRONE FLIGHT WAY POINT", color="B")

        # way point 관련 버튼 모음 위젯
        self.waypoint_btn_widget = QWidget(self)

        # way point 관련 버튼 모음 레이아웃
        self.waypoint_btn_layout = QHBoxLayout(self.waypoint_btn_widget)

        # table 관련 버튼 모음 위젯
        self.table_btn_widget = QWidget(self)

        # way point 관련 버튼 모음 레이아웃
        self.table_btn_layout = QHBoxLayout(self.table_btn_widget)

        # READ 버튼 생성
        self.btn_read = CustomButton(self.waypoint_btn_widget, 170, 30, "READ")

        # MISSION 버튼을 생성(학생)
        self.btn_mission = CustomButton(self.waypoint_btn_widget, 170, 30, "MISSION")

        # Table 관련 버튼 생성
        self.btn_init = CustomButton(self.table_btn_widget, 90, 30, "INIT")

        # INSERT 버튼 생성을 생성(학생)
        self.btn_insert = CustomButton(self.waypoint_btn_widget, 90, 30, "INSERT")

        # DELETE(학생)
        self.btn_delete = CustomButton(self.waypoint_btn_widget, 90, 30, "DELETE")

        # SAVE(학생)
        self.btn_save = CustomButton(self.waypoint_btn_widget, 90, 30, "SAVE")

        # 하단 테이블 위젯 생성
        self.way_point_list = QTableWidget(self)

        # UI 설정
        self.init_widget()

    # #########################################################################################
    #  Widget 초기화 및 설정 # 배치관련 데이터(위치, 크기, 등등)
    # #########################################################################################
    def init_widget(self):

        # Waypoint 관련 버튼 > 레이아웃 | 위젯-레이아웃 사이즈 옵션 설정
        self.waypoint_btn_layout.addWidget(self.btn_read)

        # self.btn_mission 배치(학생)
        self.waypoint_btn_layout.addWidget(self.btn_mission)

        self.waypoint_btn_widget.setFixedSize(CONTROL_WIDTH, 30)
        self.waypoint_btn_layout.setContentsMargins(0, 0, 0, 0)

        # Table 관련 버튼 > 레이아웃 | 위젯-레이아웃 사이즈 옵션 설정
        self.table_btn_layout.addWidget(self.btn_init)

        # self.btn_insert 배치(학생)
        self.table_btn_layout.addWidget(self.btn_insert)

        # self.btn_delete 배치(학생)
        self.table_btn_layout.addWidget(self.btn_delete)

        # self.btn_save 배치(학생)
        self.table_btn_layout.addWidget(self.btn_save)

        self.table_btn_widget.setFixedSize(CONTROL_WIDTH, 30)
        self.table_btn_layout.setContentsMargins(0, 0, 0, 0)

        # 테이블 위젯 생성
        self.init_table_widget()

        # 레이아웃에 각각 위젯들을 배치(학생)

        # self.title 배치
        self.waypoint_layout.addWidget(self.title)

        # self.waypoint_btn_widget 배치(학생)
        self.waypoint_layout.addWidget(self.waypoint_btn_widget)

        # self.table_btn_widget 배치(학생)
        self.waypoint_layout.addWidget(self.table_btn_widget)

        # self.way_point_list 배치(학생)
        self.waypoint_layout.addWidget(self.way_point_list)

        self.waypoint_layout.setContentsMargins(0, 0, 0, 0)

        # 화면에 display 처리
        self.setLayout(self.waypoint_layout)
        self.setStyleSheet(WAYPOINT_WIDGET_COLOR)
        self.setMinimumSize(CONTROL_WIDTH, WAYPOINT_HEIGHT)

    # #########################################################################################
    #  테이블 옵션 처리
    # #########################################################################################
    def init_table_widget(self):

        # row 단위로 선택 가능
        self.way_point_list.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 테이블 위젯 배경색 및 테두리 두께 지정
        self.way_point_list.setStyleSheet("background-color:rgb(255, 255, 255); border: 0.5px solid gray;")

        # 세로 스크롤바 항상 OFF
        self.way_point_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # 가로 스크롤바 항상 OFF
        self.way_point_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # 각 테이블 요소 간 경계선 View
        self.way_point_list.setShowGrid(True)

        # 초기 row 개수
        self.way_point_list.setRowCount(0)

        # 초기 Column 개수
        self.way_point_list.setColumnCount(5)

        # 테이블 헤더 이름 설정
        table_header = ["NO", "LAT", "LON", "ALT", "HOLD"]

        # 테이블 위젯 수평 헤더 추가
        for i in range(5):
            item = QTableWidgetItem()
            item.setText(table_header[i])
            item.setFlags(Qt.ItemIsEditable)
            self.way_point_list.setHorizontalHeaderItem(i, item)

        # 테이블 위젯 수직 헤더 옵션 설정
        self.way_point_list.verticalHeader().setVisible(False)

        # 컬럼 사이즈 설정
        self.way_point_list.setColumnWidth(0, 30)
        self.way_point_list.setColumnWidth(1, 121)
        self.way_point_list.setColumnWidth(2, 121)
        self.way_point_list.setColumnWidth(3, 78)
        self.way_point_list.setColumnWidth(4, 78)

        # 테이블 로우별 전체 컬럼 색상 처리
        palette = QPalette()
        palette.setColor(QPalette.Highlight, Qt.darkBlue)
        palette.setColor(QPalette.HighlightedText, Qt.white)
        self.way_point_list.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = WaypointModule()
    main.show()
    sys.exit(app.exec_())
