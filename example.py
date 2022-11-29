import sys

from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton,
                             QHBoxLayout, QListWidget, QLineEdit, QTextEdit,
                             QLabel)


class MainWindow(QWidget):
    """Основная форма"""
    def __init__(self):
        """Элементы формы"""
        super().__init__()
        self.tasks_list = QListWidget(self)
        self.button_all_tasks = QPushButton("Все задачи", self)
        self.button_active_tasks = QPushButton("Активные задачи", self)
        self.button_done_tasks = QPushButton("Выполненные задачи", self)
        self.task_name = QLineEdit(self)
        self.task_description = QTextEdit(self)
        self.button_add_task = QPushButton("Добавить задачу", self)
        self.button_edit_task = QPushButton("Изменить задачу", self)
        self.button_delete_task = QPushButton("Удалить задачу", self)
        self.categories_list = QListWidget(self)
        self.category_name = QLineEdit(self)
        self.button_add_category = QPushButton("Добавить категорию", self)
        self.button_edit_category = QPushButton("Изменить категорию", self)
        self.button_delete_category = QPushButton("Удалить категорию", self)
        # ...
        self.init_ui()
        # здесь подключим наши будущие функции

    def init_ui(self):
        """Размещение элементов"""
        self.resize(400, 500)
        self.setWindowTitle("Список задач")
        vbox = QVBoxLayout()
        self.name1 = QLabel('Список задач:', self)
        vbox.addWidget(self.name1)
        vbox.addWidget(self.tasks_list)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button_all_tasks)
        hbox.addWidget(self.button_active_tasks)
        hbox.addWidget(self.button_done_tasks)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        self.name2 = QLabel('Название задачи:', self)
        hbox.addWidget(self.name2)
        hbox.addWidget(self.task_name)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        self.name3 = QLabel('Описание задачи:', self)
        hbox.addWidget(self.name3)
        hbox.addWidget(self.task_description)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        self.name4 = QLabel('Категория:', self)
        hbox.addWidget(self.name4)
        hbox.addWidget(self.category_name)
        vbox.addLayout(hbox)

        self.name5 = QLabel('Список категорий:', self)
        vbox.addWidget(self.name5)
        vbox.addWidget(self.categories_list)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button_add_task)
        hbox.addWidget(self.button_edit_task)
        hbox.addWidget(self.button_delete_task)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button_add_category)
        hbox.addWidget(self.button_edit_category)
        hbox.addWidget(self.button_delete_category)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def create_db(self):
        pass
        # ...
        # здесь будет функция создания таблиц

    def load_categories(self):
        pass
        # ...
        # здесь будет функция загрузки задач

    # ...
    # здесь будут другие функции


if __name__ == '__main__':
    # Подключение базы данных
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("tasks.sqlite")

    if not con.open():
        print("Database Error: %s" % con.lastError().databaseText())
        sys.exit(1)

    # Запуск приложения
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
