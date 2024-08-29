from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTreeWidgetItem
from PyQt5.QtCore import QThread, pyqtSignal
from collections import defaultdict
from app_ui import Ui_MainWindow
from typing import List, Generator
import sys
import os
import subprocess
import platform
import hashlib


class FileHasher(QThread):
    file_hashed = pyqtSignal(str, str, str)
    hashing_finished = pyqtSignal(str)

    def __init__(self, sources: List[str], recursive: bool = False):
        super().__init__()
        self.__sources = sources

        self.__is_recursive = recursive

    def get_files_count(self) -> int:

        files_count = 0

        for _ in self.list_files():

            files_count += 1

        return files_count

    def list_files(self) -> Generator[str, None, None]:

        for source in self.__sources:

            if self.__is_recursive:

                if self.is_path_valid(source):

                    for root, _, filenames in os.walk(source):

                        for filename in filenames:

                            yield os.path.join(root, filename)

            else:
                for filename in os.listdir(source):
                    if os.path.isfile(os.path.join(source, filename)):

                        yield os.path.join(source, filename)

    def is_path_valid(self, path: str) -> bool:
        return os.path.exists(path) and os.path.isdir(path)

    def get_file_hash(self, filename: str) -> str:

        file_hash = hashlib.sha256()

        try:
            with open(filename, "rb") as file:

                while True:
                    file_chunk = file.read(1024)

                    if not file_chunk:
                        break

                    file_hash.update(file_chunk)
        finally:
            return file_hash.hexdigest()

    def run(self):

        for filename in self.list_files():
            if os.path.exists(filename):
                file_hash = self.get_file_hash(filename=filename)

            self.file_hashed.emit("Files checked ", filename, file_hash)

        self.hashing_finished.emit("Duplicates search is finished!")


class Duplicated(QMainWindow):
    def __init__(self) -> None:
        super(Duplicated, self).__init__()

        self.duplicates = defaultdict(list)

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.addSourceButton.clicked.connect(self.addSourceButtonClicked)
        self.ui.removeSourceButton.clicked.connect(self.removeSourceButtonClicked)
        self.ui.clearSourceListButton.clicked.connect(self.clearSourcesListButtonClicked)
        self.ui.startButton.clicked.connect(self.startSearchButtonClicked)
        self.ui.duplicatesTreeWidget.itemDoubleClicked.connect(
            lambda _: self.openPath(self.ui.duplicatesTreeWidget.currentItem().text(0))
        )

    def openPath(self, filepath: str):

            if os.path.exists(filepath):

                if platform.system() == "Windows":
                    subprocess.Popen(["explorer", "/select,", filepath.replace("/", "\\")])

                elif platform.system() == "Linux":
                    subprocess.Popen(["xdg-open", os.path.dirname(filepath)])

                elif platform.system() == "Darwin":
                    subprocess.Popen(["open", "-R", filepath])


    def sources(self):

        for source_item_index in range(self.ui.sourcesListWidget.count()):
            yield self.ui.sourcesListWidget.item(source_item_index)

    def startSearchButtonClicked(self):
        is_recursive = self.ui.isRecursiveSearchEnabledCheckBox.isChecked()

        self.duplicates.clear()

        self.fh = FileHasher(sources=[
            source.text() for source in self.sources()
        ], recursive=is_recursive)

        self.fh.file_hashed.connect(self.fileHashed)
        self.fh.hashing_finished.connect(self.hashingFinished)

        self.setControlsEnabled(False)
        self.ui.duplicatesTreeWidget.clear()
        self.ui.statusLabel.setText("Counting files...")

        files_count = self.fh.get_files_count()

        self.ui.progressBar.setMaximum(files_count)
        self.ui.progressBar.setValue(0)

        self.fh.start()


    def setControlsEnabled(self, enabled: bool):
        self.ui.startButton.setEnabled(enabled)
        self.ui.addSourceButton.setEnabled(enabled)
        self.ui.clearSourceListButton.setEnabled(enabled)
        self.ui.removeSourceButton.setEnabled(enabled)

    def isSourceUnique(self, source: str) -> bool:
        """
        Checks if the source already exsists in list of sources.

        :return: bool
        """

        for source_item in self.sources():
            if source_item.text() == source:
                return False

        return True

    def fileHashed(self, status: str, filepath: str, hash: str):
        self.duplicates[hash].append(filepath)

        self.ui.statusLabel.setText(f"{status}: {self.ui.progressBar.value() + 1}/{self.ui.progressBar.maximum()}")
        self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)

    def hashingFinished(self, status: str):

        self.setControlsEnabled(True)
        for hash, files in self.duplicates.items():

            if len(files) > 1:

                parent_tree_item = QTreeWidgetItem([hash])

                for file in files:

                    parent_tree_item.addChild(QTreeWidgetItem([file]))

                self.ui.duplicatesTreeWidget.addTopLevelItem(parent_tree_item)

        self.ui.statusLabel.setText(status)

    def addSourceButtonClicked(self):
        """
        Adds selected directory to the list of sources, where the programm will search for duplicates.
        """

        dialog = QFileDialog()
        dialog.setFileMode(dialog.DirectoryOnly)
        if dialog.exec_():
            source = dialog.selectedFiles()[0]
            if source:
                if self.isSourceUnique(source=source):
                    self.ui.sourcesListWidget.addItem(source)

    def removeSourceButtonClicked(self):
        current_row = self.ui.sourcesListWidget.currentRow()
        if current_row >= 0:
            self.ui.sourcesListWidget.takeItem(current_row)

    def clearSourcesListButtonClicked(self):
        self.ui.sourcesListWidget.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = Duplicated()
    main_window.show()

    sys.exit(app.exec())
