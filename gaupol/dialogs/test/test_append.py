# -*- coding: utf-8 -*-

# Copyright (C) 2005-2008 Osmo Salomaa
#
# This file is part of Gaupol.
#
# Gaupol is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Gaupol is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Gaupol. If not, see <http://www.gnu.org/licenses/>.

import gaupol
import os

from gi.repository import Gtk
from .test_file import _TestFileDialog


class TestAppendDialog(_TestFileDialog):

    def run_dialog(self):
        self.dialog.run()

    def setup_method(self, method):
        gaupol.conf.file.directory = os.getcwd()
        self.dialog = gaupol.AppendDialog(Gtk.Window())
        self.dialog.show()
