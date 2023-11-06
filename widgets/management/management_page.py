
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
class ManagementPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUI()
    
    def setupUI(self):
        self.layout_page = QVBoxLayout(self)
        self.frame_event = QFrame(self)
        #  event table
        self.layout_event = QHBoxLayout(self.frame_event)
        self.label_event = QLabel(self)
        self.label_event.setText("Events: ")
        self.label_event.setStyleSheet("font:bold 22px; color:rgb(255,255,255); border-radius:10px")
        self.btn_add_event = QPushButton(self)
        self.btn_add_event.setText(" + ")
        self.btn_add_event.setObjectName("btn_add_event")
        self.btn_add_event.setStyleSheet("font:bold 22px; color:rgb(255,255,255); border-radius:10px; padding-bottom: 5px")
        
        self.btn_add_event.setMinimumWidth(50)
        self.layout_event.addWidget(self.label_event)
        self.layout_event.addWidget(self.btn_add_event)
        self.layout_event.addStretch()

        self.table_event = QTableWidget(self)
        self.table_event.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_event.setColumnCount(5)
        self.table_event.verticalHeader().setDefaultSectionSize(50)
        self.table_event.horizontalHeader().setStretchLastSection(True)
        self.table_event.verticalHeader().setVisible(False)
        self.table_event.setHorizontalHeaderLabels(["EventID", "Keyword", "Since", "Untill", ""])
        self.table_event.setColumnWidth(0,100)
        self.table_event.setColumnWidth(1,200)
        self.table_event.setColumnWidth(2,200)
        self.table_event.setColumnWidth(3,200)
                                        
        # self.setup_events()
        self.layout_page.addWidget(self.frame_event)
        self.layout_page.addWidget(self.table_event)

        # Pin list table

        # self.table_event
    
    def setup_events(self, events):
        self.table_event.setRowCount(0)
        # print(events)
        for idx, event in enumerate(events):
            self.table_event.insertRow(self.table_event.rowCount())

            self.table_event.setItem(idx, 0, QTableWidgetItem(f"{event.ID}"))
            self.table_event.setItem(idx, 1, QTableWidgetItem(f"{event.keyword}"))
            self.table_event.setItem(idx, 2, QTableWidgetItem(f"{event.since}"))
            self.table_event.setItem(idx, 3, QTableWidgetItem(f"{event.until}"))

            widget_btn2 = QWidget()
            layout_btn = QVBoxLayout(widget_btn2)
            btn2 = QPushButton()
            # btn2.setText("Edit")
            btn2.setStyleSheet("font:22px; color:rgb(255,255,255); border-radius:10px; padding-top: 5px; background-image: url(:/icons/images/icons/cil-loop-circular.png); background-repeat: no-repeat;")
            btn2.setObjectName(f"btn_edit_event_{event.ID}")

            # btn2.clicked.connect(openCloseLeftBox(self, True))
            layout_btn.addWidget(btn2)
            self.table_event.setCellWidget(idx, 4, widget_btn2)






