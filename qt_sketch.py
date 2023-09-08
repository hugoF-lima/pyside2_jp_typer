# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_sketch.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_jp_typer_srs(object):
    def setupUi(self, jp_typer_srs):
        if not jp_typer_srs.objectName():
            jp_typer_srs.setObjectName("jp_typer_srs")
        jp_typer_srs.resize(953, 464)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(jp_typer_srs.sizePolicy().hasHeightForWidth())
        jp_typer_srs.setSizePolicy(sizePolicy)
        jp_typer_srs.setWindowTitle("\u65e5\u672c\u8a9e\u306e\u7df4\u7fd2")
        self.gridLayout_2 = QGridLayout(jp_typer_srs)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.jp_groupbox = QGroupBox(jp_typer_srs)
        self.jp_groupbox.setObjectName("jp_groupbox")
        self.jp_groupbox.setMinimumSize(QSize(935, 446))
        font = QFont()
        font.setFamily("Yu Mincho")
        font.setPointSize(14)
        self.jp_groupbox.setFont(font)
        self.jp_groupbox.setCheckable(False)
        self.gridLayout = QGridLayout(self.jp_groupbox)
        self.gridLayout.setObjectName("gridLayout")
        self.user_output = QLineEdit(self.jp_groupbox)
        self.user_output.setObjectName("user_output")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(50)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.user_output.sizePolicy().hasHeightForWidth())
        self.user_output.setSizePolicy(sizePolicy1)
        self.user_output.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamily("Yu Mincho")
        font1.setPointSize(28)
        self.user_output.setFont(font1)

        self.gridLayout.addWidget(self.user_output, 6, 1, 1, 4)

        self.status_color = QLabel(self.jp_groupbox)
        self.status_color.setObjectName("status_color")
        self.status_color.setAutoFillBackground(False)
        self.status_color.setStyleSheet("")

        self.gridLayout.addWidget(self.status_color, 6, 5, 1, 1)

        self.output_lbl = QLabel(self.jp_groupbox)
        self.output_lbl.setObjectName("output_lbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.output_lbl.sizePolicy().hasHeightForWidth())
        self.output_lbl.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamily("Yu Mincho")
        font2.setPointSize(12)
        self.output_lbl.setFont(font2)
        self.output_lbl.setLineWidth(0)
        self.output_lbl.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.output_lbl.setWordWrap(False)
        self.output_lbl.setMargin(0)
        self.output_lbl.setIndent(-1)

        self.gridLayout.addWidget(self.output_lbl, 6, 0, 1, 1)

        self.remain_lbl = QLabel(self.jp_groupbox)
        self.remain_lbl.setObjectName("remain_lbl")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.remain_lbl.sizePolicy().hasHeightForWidth())
        self.remain_lbl.setSizePolicy(sizePolicy3)
        self.remain_lbl.setFont(font2)
        self.remain_lbl.setAutoFillBackground(False)
        self.remain_lbl.setLineWidth(0)
        self.remain_lbl.setTextFormat(Qt.AutoText)
        self.remain_lbl.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.remain_lbl.setWordWrap(False)
        self.remain_lbl.setMargin(0)
        self.remain_lbl.setIndent(-1)

        self.gridLayout.addWidget(self.remain_lbl, 2, 0, 1, 1)

        self.input_lbl = QLabel(self.jp_groupbox)
        self.input_lbl.setObjectName("input_lbl")
        sizePolicy2.setHeightForWidth(self.input_lbl.sizePolicy().hasHeightForWidth())
        self.input_lbl.setSizePolicy(sizePolicy2)
        self.input_lbl.setFont(font2)
        self.input_lbl.setLineWidth(0)
        self.input_lbl.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.input_lbl.setWordWrap(False)
        self.input_lbl.setMargin(0)
        self.input_lbl.setIndent(-1)

        self.gridLayout.addWidget(self.input_lbl, 4, 0, 1, 1)

        self.show_english_transl = QCheckBox(self.jp_groupbox)
        self.show_english_transl.setObjectName("show_english_transl")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.show_english_transl.sizePolicy().hasHeightForWidth()
        )
        self.show_english_transl.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setFamily("Yu Mincho")
        font3.setPointSize(8)
        self.show_english_transl.setFont(font3)

        self.gridLayout.addWidget(self.show_english_transl, 5, 0, 1, 1)

        self.show_kana_check = QCheckBox(self.jp_groupbox)
        self.show_kana_check.setObjectName("show_kana_check")
        sizePolicy4.setHeightForWidth(
            self.show_kana_check.sizePolicy().hasHeightForWidth()
        )
        self.show_kana_check.setSizePolicy(sizePolicy4)
        self.show_kana_check.setFont(font3)

        self.gridLayout.addWidget(self.show_kana_check, 1, 0, 1, 1)

        self.english_translate = QLineEdit(self.jp_groupbox)
        self.english_translate.setObjectName("english_translate")
        sizePolicy1.setHeightForWidth(
            self.english_translate.sizePolicy().hasHeightForWidth()
        )
        self.english_translate.setSizePolicy(sizePolicy1)
        self.english_translate.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.english_translate, 5, 1, 1, 4)

        self.input_phrase = QLineEdit(self.jp_groupbox)
        self.input_phrase.setObjectName("input_phrase")
        sizePolicy1.setHeightForWidth(
            self.input_phrase.sizePolicy().hasHeightForWidth()
        )
        self.input_phrase.setSizePolicy(sizePolicy1)
        self.input_phrase.setMinimumSize(QSize(0, 0))
        font4 = QFont()
        font4.setFamily("Yu Mincho")
        font4.setPointSize(18)
        self.input_phrase.setFont(font4)

        self.gridLayout.addWidget(self.input_phrase, 4, 1, 1, 4)

        self.hiragana_input = QLineEdit(self.jp_groupbox)
        self.hiragana_input.setObjectName("hiragana_input")
        sizePolicy1.setHeightForWidth(
            self.hiragana_input.sizePolicy().hasHeightForWidth()
        )
        self.hiragana_input.setSizePolicy(sizePolicy1)
        self.hiragana_input.setMinimumSize(QSize(0, 0))
        self.hiragana_input.setFont(font2)

        self.gridLayout.addWidget(self.hiragana_input, 1, 1, 1, 4)

        self.no_hiragana_lbl = QLabel(self.jp_groupbox)
        self.no_hiragana_lbl.setObjectName("no_hiragana_lbl")
        sizePolicy3.setHeightForWidth(
            self.no_hiragana_lbl.sizePolicy().hasHeightForWidth()
        )
        self.no_hiragana_lbl.setSizePolicy(sizePolicy3)
        self.no_hiragana_lbl.setFont(font2)
        self.no_hiragana_lbl.setAutoFillBackground(False)
        self.no_hiragana_lbl.setTextFormat(Qt.AutoText)
        self.no_hiragana_lbl.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.no_hiragana_lbl.setWordWrap(False)

        self.gridLayout.addWidget(self.no_hiragana_lbl, 2, 3, 1, 1)

        self.elapsed_lbl = QLabel(self.jp_groupbox)
        self.elapsed_lbl.setObjectName("elapsed_lbl")
        sizePolicy3.setHeightForWidth(self.elapsed_lbl.sizePolicy().hasHeightForWidth())
        self.elapsed_lbl.setSizePolicy(sizePolicy3)
        self.elapsed_lbl.setFont(font2)
        self.elapsed_lbl.setAutoFillBackground(False)
        self.elapsed_lbl.setTextFormat(Qt.AutoText)
        self.elapsed_lbl.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.elapsed_lbl.setWordWrap(False)

        self.gridLayout.addWidget(self.elapsed_lbl, 2, 2, 1, 1)

        self.gridLayout_2.addWidget(self.jp_groupbox, 0, 0, 1, 1)

        self.retranslateUi(jp_typer_srs)

        QMetaObject.connectSlotsByName(jp_typer_srs)

    # setupUi

    def retranslateUi(self, jp_typer_srs):
        self.jp_groupbox.setTitle(
            QCoreApplication.translate("jp_typer_srs", "Japanese Typer", None)
        )
        self.status_color.setText("")
        self.output_lbl.setText(
            QCoreApplication.translate("jp_typer_srs", "Your Output:", None)
        )
        self.remain_lbl.setText(
            QCoreApplication.translate("jp_typer_srs", "Remaining quotes:", None)
        )
        self.input_lbl.setText(
            QCoreApplication.translate("jp_typer_srs", "Input Phrase:", None)
        )
        self.show_english_transl.setText(
            QCoreApplication.translate("jp_typer_srs", "Show English", None)
        )
        self.show_kana_check.setText(
            QCoreApplication.translate("jp_typer_srs", "Show Hiragana", None)
        )
        self.no_hiragana_lbl.setText(
            QCoreApplication.translate("jp_typer_srs", "No Hiragana:", None)
        )
        self.elapsed_lbl.setText(
            QCoreApplication.translate("jp_typer_srs", "Elapsed:", None)
        )
        pass

    # retranslateUi
