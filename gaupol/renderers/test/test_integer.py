# -*- coding: utf-8 -*-

# Copyright (C) 2009 Osmo Salomaa
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

from gi.repository import Gtk


class TestIntegerCellRenderer(gaupol.TestCase):

    def run__renderer(self):
        tree_view = Gtk.TreeView()
        tree_view.set_headers_visible(False)
        store = Gtk.ListStore(int)
        store.append((12,))
        tree_view.set_model(store)
        self.renderer.props.editable = True
        column = Gtk.TreeViewColumn("", self.renderer, text=0)
        tree_view.append_column(column)
        window = Gtk.Window()
        window.connect("delete-event", Gtk.main_quit)
        window.set_position(Gtk.WindowPosition.CENTER)
        window.set_default_size(200, 50)
        window.add(tree_view)
        window.show_all()
        Gtk.main()

    def setup_method(self, method):
        self.renderer = gaupol.IntegerCellRenderer()
