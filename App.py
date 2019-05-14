from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from BlendProblem import BlendProblem


class BlendProblemApp(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.blend_data = BlendProblem()
        self.createInterface()

    def createInterface(self):
        # K O N F I G U R A C J A
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        self.setWindowTitle("Problem mieszanki")

        # B U D O W A O K N A
        var_name_label = QLabel("Nazwa zmiennej;wlasciwosc")
        var_value_label = QLabel("Wartosc zmiennej")
        self.var_name = QLineEdit()
        self.var_value = QLineEdit()
        add_var = QPushButton("Dodaj zmienną")


        condition_var_label = QLabel("Zmienna")
        condition_label = QLabel("Warunek;wartosc")
        self.cond_var = QLineEdit()
        self.cond = QLineEdit()
        add_cond = QPushButton("Dodaj warunek")


        result_button = QPushButton("Oblicz")
        self.result_label = QLabel()

        main_box = QVBoxLayout()
        insert_label_box = QHBoxLayout()
        insert_box = QHBoxLayout()
        cond_label_box = QHBoxLayout()
        cond_box = QHBoxLayout()
        operations_box = QHBoxLayout()

        # INSERT
        insert_label_box.addWidget(var_name_label)
        insert_label_box.addWidget(var_value_label)
        insert_box.addWidget(self.var_name)
        insert_box.addWidget(self.var_value)
        insert_box.addWidget(add_var)

        # COND
        cond_label_box.addWidget(condition_var_label)
        cond_label_box.addWidget(condition_label)
        cond_box.addWidget(self.cond_var)
        cond_box.addWidget(self.cond)
        cond_box.addWidget(add_cond)

        # RESULT
        operations_box.addWidget(result_button)
        operations_box.addWidget(self.result_label)

        # MAIN
        main_box.addLayout(insert_label_box)
        main_box.addLayout(insert_box)
        main_box.addLayout(cond_label_box)
        main_box.addLayout(cond_box)
        main_box.addLayout(operations_box)
        main_box.addStretch(1)

        # B I N D I N G
        add_var.clicked.connect(self.add_variable)
        add_cond.clicked.connect(self.add_condition)
        result_button.clicked.connect(self.solver)

        self.setLayout(main_box)
        self.show()

    def add_variable(self):
        return None

    def add_condition(self):
        return None

    def solver(self):
        return None


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = BlendProblemApp()
    sys.exit(app.exec_())
