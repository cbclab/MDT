import os
from PyQt5 import QtCore

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QBrush
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QAbstractItemView, QMenu, QMessageBox, \
    QDialog, QDialogButtonBox

import mdt
from mdt.gui.qt.design.ui_generate_protocol_load_gb_dialog import Ui_LoadGBDialog
from mdt.gui.qt.design.ui_generate_protocol_tab import Ui_GenerateProtocolTabContent
from mdt.gui.qt.design.ui_generate_protocol_update_dialog import Ui_UpdateColumnDialog
from mdt.gui.qt.utils import protocol_files_filters, MainTab
from mdt.protocols import Protocol

__author__ = 'Robbert Harms'
__date__ = "2016-06-27"
__maintainer__ = "Robbert Harms"
__email__ = "robbert.harms@maastrichtuniversity.nl"


class GenerateProtocolTab(MainTab, Ui_GenerateProtocolTabContent):

    def __init__(self, shared_state, computations_thread):
        self._shared_state = shared_state
        self._protocol = Protocol()
        self._opened_file = self._shared_state.base_dir
        self._tab_content = None

    def setupUi(self, tab_content):
        super(GenerateProtocolTab, self).setupUi(tab_content)
        self._tab_content = tab_content

        self.loadProtocolButton.clicked.connect(lambda: self._select_protocol())
        self.saveButton.clicked.connect(lambda: self._save_protocol())
        self.loadColumnButton.clicked.connect(lambda: self._load_column_action())
        self.loadGB.clicked.connect(lambda: self._load_g_and_b())
        self.clearButton.clicked.connect(self._clear_table)

        headers = self.protocol_table.horizontalHeader()
        headers.setContextMenuPolicy(Qt.CustomContextMenu)
        headers.customContextMenuRequested.connect(self.show_header_context_menu)
        headers.setSelectionMode(QAbstractItemView.SingleSelection)

    def _select_protocol(self):
        open_file, used_filter = QFileDialog().getOpenFileName(
            caption='Select the protocol', directory=self._shared_state.base_dir,
            filter=';;'.join(protocol_files_filters))

        if open_file:
            self._shared_state.base_dir = os.path.dirname(open_file)
            self.load_protocol(open_file)

    def _save_protocol(self):
        output_file_name, used_filter = QFileDialog().getSaveFileName(
            caption='Save the protocol as', directory=self._opened_file,
            filter=';;'.join(protocol_files_filters))

        if os.path.isdir(os.path.dirname(output_file_name)) and self._protocol.length:
            mdt.write_protocol(self._protocol, output_file_name)
            print('Saved protocol as: {}'.format(output_file_name))

    @pyqtSlot()
    def _clear_table(self):
        self._protocol = Protocol()
        self._update_views()

    def load_protocol(self, file_name):
        self._protocol = mdt.protocols.load_protocol(file_name)
        self._update_views()
        self._opened_file = file_name
        print('Loaded protocol: {}'.format(file_name))

    def _update_views(self):
        self._update_protocol_info()
        self._update_table_view()

    def _update_protocol_info(self):
        self.nmrRows.setText(str(self._protocol.length))

        try:
            self.nmrUnweighted.setText(str(len(self._protocol.get_unweighted_indices())))
        except KeyError:
            self.nmrUnweighted.setText('0')

        try:
            self.nmrWeighted.setText(str(len(self._protocol.get_weighted_indices())))
        except KeyError:
            self.nmrWeighted.setText('0')

        try:
            self.nmrShells.setText(str(len(self._protocol.get_b_values_shells())))
        except KeyError:
            self.nmrShells.setText('0')
        self.nmrColumns.setText(str(self._protocol.number_of_columns))

        try:
            self.differentShells.setText(', '.join(map(lambda s: '{:0=.3f}e9'.format(s/1e9),
                                                       self._protocol.get_b_values_shells())))
        except KeyError:
            self.differentShells.setText('-')

    def _update_table_view(self):
        real_column_names, estimated_column_names, all_column_names = self._get_column_names()

        self.protocol_table.clear()
        self.protocol_table.setRowCount(self._protocol.length)
        self.protocol_table.setColumnCount(len(all_column_names))

        for index, column_name in enumerate(all_column_names):
            header_cell = QTableWidgetItem(column_name)
            if index >= len(real_column_names):
                header_cell.setToolTip('This column is estimated from the other columns in the protocol.')
            self.protocol_table.setHorizontalHeaderItem(index, header_cell)

        for column_ind, column_name in enumerate(all_column_names):
            estimated_column = column_ind >= len(real_column_names)

            try:
                values = self._protocol.get_column(column_name)
                for row in range(self._protocol.length):
                    cell = QTableWidgetItem('{:e}'.format(values[row, 0]))
                    cell.setFlags(QtCore.Qt.ItemIsEnabled)

                    if estimated_column:
                        cell.setBackground(QBrush(Qt.lightGray))

                    self.protocol_table.setItem(row, column_ind, cell)
            except KeyError:
                for row in range(self._protocol.length):
                    cell = QTableWidgetItem('?')
                    cell.setFlags(QtCore.Qt.ItemIsEnabled)
                    cell.setBackground(QBrush(Qt.lightGray))
                    self.protocol_table.setItem(row, column_ind, cell)

    def _get_column_names(self):
        real_column_names = self._protocol.column_names
        estimated_column_names = self._protocol.estimated_column_names
        all_column_names = real_column_names + estimated_column_names

        return [real_column_names, estimated_column_names, all_column_names]

    @pyqtSlot()
    def show_header_context_menu(self, position):
        real_column_names, estimated_column_names, all_column_names = self._get_column_names()
        column_index = self.protocol_table.horizontalHeader().logicalIndexAt(position)
        column_name = all_column_names[column_index]

        if column_index < len(real_column_names):
            menu = QMenu()
            remove_action = menu.addAction("&Remove column")
            ac = menu.exec_(self.protocol_table.horizontalHeader().mapToGlobal(position))

            if ac == remove_action:
                quit_msg = "Are you sure you want to remove the " \
                           "column '{}' from the protocol".format(column_name)
                reply = QMessageBox.question(self._tab_content, 'Delete confirmation', quit_msg,
                                             QMessageBox.Yes, QMessageBox.No)

                if reply == QMessageBox.Yes:
                    self._protocol.remove_column(column_name)
                    self._update_views()

    def _load_column_action(self):
        dialog = LoadColumnDialog(self._shared_state, self._tab_content)
        return_value = dialog.exec_()

        if return_value:
            dialog.update_protocol(self._protocol)
            self._update_views()

    def _load_g_and_b(self):
        dialog = LoadGBDialog(self._shared_state, self._tab_content)
        return_value = dialog.exec_()

        if return_value:
            self._protocol = dialog.get_protocol()
            self._update_views()


class LoadColumnDialog(Ui_UpdateColumnDialog, QDialog):

    def __init__(self, shared_state, parent):
        super(LoadColumnDialog, self).__init__(parent)
        self._input_options = {'from_file': 0, 'from_value': 1}
        self._shared_state = shared_state
        self.setupUi(self)
        self.inputMethodSelector.currentIndexChanged.connect(self.enable_correct_inputs)
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.columnNameInput.textChanged.connect(self._update_ok_button)
        self.singleValueInput.textChanged.connect(self._update_ok_button)
        self.fileInput.clicked.connect(lambda: self._select_value_file())
        self.selectedFile.textChanged.connect(self._update_ok_button)
        self.enable_correct_inputs(self.inputMethodSelector.currentIndex())

    def update_protocol(self, protocol):
        column_name = self.columnNameInput.text()
        if column_name:
            try:
                scale = float(self.valueScale.text())
            except ValueError:
                scale = 1

            if self.inputMethodSelector.currentIndex() == self._input_options['from_value']:
                value = float(self.singleValueInput.text())
                protocol.add_column(column_name, value * scale)
            else:
                protocol.add_column_from_file(column_name, self.selectedFile.text(), scale)

    @pyqtSlot(int)
    def enable_correct_inputs(self, selection):
        if selection == self._input_options['from_value']:
            self.singleValueInput.setDisabled(False)
            self.fileInput.setDisabled(True)
            self.selectedFile.setDisabled(True)
        else:
            self.singleValueInput.setDisabled(True)
            self.fileInput.setDisabled(False)
            self.selectedFile.setDisabled(False)

    @pyqtSlot()
    def _update_ok_button(self):
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(self.columnNameInput.text() != '' and self._has_value())

    def _has_value(self):
        if self.inputMethodSelector.currentIndex() == self._input_options['from_value']:
            if self.singleValueInput.text() != '':
                try:
                    float(self.singleValueInput.text())
                    return True
                except ValueError:
                    pass
            return False
        else:
            if os.path.isfile(self.selectedFile.text()):
                return True
        return False

    def _select_value_file(self):
        initial_dir = self._shared_state.base_dir
        if self.selectedFile.text() != '':
            initial_dir = self.selectedFile.text()

        open_file, used_filter = QFileDialog().getOpenFileName(caption='Select the column info file', directory=initial_dir)

        if open_file:
            self.selectedFile.setText(open_file)
            self._shared_state.base_dir = os.path.dirname(open_file)
            self._update_ok_button()


class LoadGBDialog(Ui_LoadGBDialog, QDialog):

    def __init__(self, shared_state, parent):
        super(LoadGBDialog, self).__init__(parent)
        self._shared_state = shared_state
        self.setupUi(self)
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.bvecFileInput.textChanged.connect(self._update_ok_button)
        self.bvalFileInput.textChanged.connect(self._update_ok_button)
        self.bvecFileChooser.clicked.connect(lambda: self._select_bvec_file())
        self.bvalFileChooser.clicked.connect(lambda: self._select_bval_file())

    def get_protocol(self):
        try:
            bval_scale = float(self.bvalScale.text())
        except:
            bval_scale = 1

        return mdt.load_protocol_bval_bvec(bvec=self.bvecFileInput.text(),
                                           bval=self.bvalFileInput.text(),
                                           bval_scale=bval_scale)

    @pyqtSlot()
    def _update_ok_button(self):
        enable = os.path.isfile(self.bvalFileInput.text()) and os.path.isfile(self.bvecFileInput.text())
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(enable)

    def _select_bvec_file(self):
        initial_dir = self._shared_state.base_dir
        if self.bvecFileInput.text() != '':
            initial_dir = self.bvecFileInput.text()

        open_file, used_filter = QFileDialog().getOpenFileName(caption='Select the bvec file', directory=initial_dir)

        if open_file:
            self.bvecFileInput.setText(open_file)
            self._shared_state.base_dir = os.path.dirname(open_file)
            self._update_ok_button()

    def _select_bval_file(self):
        initial_dir = self._shared_state.base_dir
        if self.bvalFileInput.text() != '':
            initial_dir = self.bvalFileInput.text()

        open_file, used_filter = QFileDialog().getOpenFileName(caption='Select the bval file', directory=initial_dir)

        if open_file:
            self.bvalFileInput.setText(open_file)
            self._shared_state.base_dir = os.path.dirname(open_file)
            self._update_ok_button()
