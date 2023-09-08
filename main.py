import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from intro_dialog import Ui_Dialog
import qdarkstyle
from qt_sketch import Ui_jp_typer_srs
import csv_lookup
from flashcard_srs import Flashcard, SRS

# TODO? Implement an audio and type
# mode would improve listening i guess


class SRS_Style_frame(QWidget):
    def __init__(self, flashcard: Flashcard):
        super().__init__()
        self.ui = Ui_jp_typer_srs()
        central_widget = QFrame(self)
        self.ui.setupUi(central_widget)

        self.grab_hiragana = ""
        self.grab_english = ""
        self.correct_count = 0
        self.correct_without_lookup = 0
        self.remain_lbl = "Remaining quotes: - "

        self.flashcard = flashcard
        self.ui.input_phrase.setText(self.flashcard.question)
        # print(type(self.flashcard.question))
        self.flashcard_collect = self.return_list_flash
        # self.remain_lbl = len(flash_obj)

        self.ui.user_output.returnPressed.connect(self.compare_output)

    def return_list_flash(self):
        self.flashcard_collect = csv_lookup.access_flashcard()
        return self.flashcard_collect

    def show_flashcard(self, flashcard_lists):
        srs = SRS(flashcard_lists)
        counter = 0
        review_limit = len(flashcard_lists)
        self.flash_Card = flashcard
        while counter < review_limit:
            flashcard = srs.review()
            self.show()

    def compare_output(self):
        def flashing_event(widget_in):
            flash_index = 0
            flash_timer = QTimer(self, interval=90)

            flash_colors = [
                "color: red",
                "color: green",
                "color: white",
            ]

            def flashing():
                nonlocal flash_index
                widget_in.setStyleSheet(flash_colors[flash_index])
                flash_index = (flash_index + 1) % 3
                if flash_index == 0:
                    flash_timer.stop()

            flash_timer.timeout.connect(flashing)
            flash_timer.start()

        answer = self.ui.user_output.text()
        if answer == self.flashcard.answer:
            if self.ui.show_kana_check.isChecked() == False:
                self.correct_without_lookup += 1
                flashing_event(self.ui.no_hiragana_lbl)

            self.show_flashcard(self.flashcard)
            self.flashcard.update_interval(3)
            self.correct_count += 1
        else:
            self.flashcard.update_interval(1)
        # self.accept()


class Random_quote_frame(QWidget):  # This can't be QMainWindow
    def __init__(self):
        super().__init__()
        # self.sub_inherit = sub_inherit

        self.ui = Ui_jp_typer_srs()
        central_widget = QFrame(self)
        self.ui.setupUi(central_widget)

        # TODO: Set icon here
        # Are these correct scoping?
        self.attribute = []
        self.grab_hiragana = ""
        self.grab_english = ""
        self.correct_count = 0
        self.correct_without_lookup = 0
        self.remain_lbl = "Remaining quotes: - "
        # self.setWindowTitle("日本語の練習")

    def compare_output(self, *event):
        def flashing_event(widget_in):
            flash_index = 0
            flash_timer = QTimer(self, interval=90)

            flash_colors = [
                "color: red",
                "color: green",
                "color: white",
            ]

            def flashing():
                nonlocal flash_index
                widget_in.setStyleSheet(flash_colors[flash_index])
                flash_index = (flash_index + 1) % 3
                if flash_index == 0:
                    flash_timer.stop()

            flash_timer.timeout.connect(flashing)
            flash_timer.start()

        # global correct_count
        # global correct_without_lookup

        if self.ui.input_phrase.text() == self.ui.user_output.text():
            # Unfortunately not registering if unchecked after
            # Needed something like "Pressed before unchecked".
            if self.ui.show_kana_check.isChecked() == False:
                self.correct_without_lookup += 1
                flashing_event(self.ui.no_hiragana_lbl)

            self.call_next_quote()
            self.correct_count += 1
            # TODO: Make it flash red, then flash green
            self.ui.elapsed_lbl.clear()
            flashing_event(self.ui.elapsed_lbl)
            self.ui.elapsed_lbl.setText(f"Elapsed: {self.correct_count}")
            self.ui.elapsed_lbl.repaint()  # update() ?
            self.ui.no_hiragana_lbl.clear()
            self.ui.no_hiragana_lbl.setText(
                f"No Hiragana: {self.correct_without_lookup}"
            )
            self.ui.no_hiragana_lbl.repaint()  # update() ?

        else:
            self.ui.status_color.setStyleSheet(
                "background-color: rgb(255, 0, 4)"
            )  # red

    def show_hiragana_box_toggled(self):
        if self.ui.show_kana_check.isChecked() == True:
            self.ui.hiragana_input.setText(self.grab_hiragana)

        else:
            self.ui.hiragana_input.clear()

    def show_english_box_toggled(self):
        if self.ui.show_english_transl.isChecked() == True:

            self.ui.english_translate.setText(self.grab_english)
        else:
            self.ui.english_translate.clear()

    def call_next_quote(self):
        self.ui.input_phrase.clear()
        self.ui.user_output.clear()
        self.ui.hiragana_input.clear()
        self.ui.english_translate.clear()
        self.ui.show_kana_check.setChecked(False)
        self.ui.show_english_transl.setChecked(False)

        self.ui.remain_lbl.clear()
        self.ui.remain_lbl.setText(str(self.remain_lbl))
        self.ui.remain_lbl.repaint()

        list_items = self.return_next_value()

        self.ui.input_phrase.setText(list_items[0])
        self.grab_english = str(list_items[1])
        self.grab_hiragana = str(list_items[2])

    def return_next_value(self):
        self.attribute = csv_lookup.random_quote()
        return self.attribute

    def display_main(self):
        # print(f"Attribute: {self.sub_inherit.attribute}")
        self.call_next_quote()
        self.ui.show_kana_check.toggled.connect(self.show_hiragana_box_toggled)
        self.ui.show_english_transl.toggled.connect(self.show_english_box_toggled)
        self.ui.user_output.returnPressed.connect(self.compare_output)

        self.show()


class Linear:
    def __init__(self):
        self.attribute = "Linear"


class Dialog_select(QDialog):
    def __init__(self):
        super().__init__()
        self.ui_d = Ui_Dialog()
        self.setWindowTitle("Choose Dialog")
        self.descr_options = ["Random quotes", "SRS Style", "Linear"]
        self.descr = ""
        self.ui_d.setupUi(self)  # should i call this later at exec?
        self.ui_d.options_mode_cb.addItems(self.descr_options)
        self.ui_d.options_mode_cb.setCurrentIndex(-1)
        self.ui_d.options_mode_cb.currentTextChanged.connect(self.description_updater)

        # self.setFixedWidth(800)
        # self.obj_inherit = None
        # self.secondWindow = Children_frame()

        """ dialog_layout = QFormLayout()
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Random quotes", "SRS Style", "Linear"])
        dialog_layout.addRow("Choose Quote \n Access Mode:", self.combo_box)

        self.qline_descr = QLineEdit()
        self.qline_descr.setText("Choose Description")
        dialog_layout.addRow(self.qline_descr)

        self.submit_button = QPushButton("Submit") """
        # self.submit_button.setStyleSheet("font-size: 30px")
        self.ui_d.buttonBox.accepted.connect(self.call_main)  # launch main from out
        # dialog_layout.addWidget(self.submit_button)

        # self.setLayout(dialog_layout)

    def description_updater(self):
        mode_option = -1

        def update_text(value_in):
            self.descr = ""
            self.descr += value_in
            # Text not properly setting up
            self.ui_d.qline_descr.clear()
            self.ui_d.qline_descr.setText(self.descr)
            self.ui_d.qline_descr.update()
            print(self.descr)

        found_index = self.ui_d.options_mode_cb.currentIndex()
        if found_index == 0:
            mode_option = 0
            update_text("Description: Display quotes in random order.")
        elif found_index == 1:
            mode_option = 1
            update_text("Description: SRS Logic for learning new words.")
        elif found_index == 2:
            mode_option = 2
            update_text("Description: Quotes appear only once.")
        return mode_option

    def call_main(self):
        class_name = self.ui_d.options_mode_cb.currentText()
        if class_name == "Random quotes":
            self.secondWindow = Random_quote_frame()
            self.secondWindow.return_next_value()
            self.secondWindow.display_main()
        elif class_name == "SRS Style":

            # flashcard_list = csv_lookup.access_flashcard()
            flashcard1 = Flashcard(
                question="What is 1+1?",
                answer="2",
                english="One plus one",
                hiragana="いち + いち",
            )
            flashcard2 = Flashcard(
                question="What is 2+2?",
                answer="4",
                english="Two plus two",
                hiragana="に + に",
            )
            flashcard_list = [flashcard1, flashcard2]

            srs_frame = SRS_Style_frame()
            srs_frame.show_flashcard(flashcard_list)
            # srs_frame.show()

            # Nope, i just gave one argument here, not two
            # self.secondWindow.show_flashcard(flashcard)

        else:
            self.obj = Linear()
        # self.secondWindow = Children_frame(self)
        # I could pass data here relevant to filtering
        """ self.secondWindow.input1.setText(str(self.obj.attribute))
        self.secondWindow.input2.setText(str(self.obj.attribute)) """
        # self.secondWindow.setWindowTitle(f"日本語の練習 - {self.obj.attribute}")
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
    demo = Dialog_select()
    demo.show()
    sys.exit(app.exec_())
