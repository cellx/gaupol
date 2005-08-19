# Copyright (C) 2005 Osmo Salomaa
#
# This file is part of Gaupol.
#
# Gaupol is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Gaupol is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Gaupol; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA


"""Statistics and information."""


import re

try:
    from psyco.classes import *
except ImportError:
    pass

from gaupol.lib.delegates.delegate import Delegate


class Analyzer(Delegate):
    
    """Statistics and information."""

    def get_character_count(self, row, col):
        """
        Get character count of text specified by row and col.
        
        Return: list of row lengths, total length
        """
        text = self.texts[row][col]
        re_tag = self.get_regex_for_tag(col)
        
        if re_tag is not None:
            text = re_tag.sub('', text)

        lines = text.split('\n')

        lengths = [len(line) for line in lines]
        total = len(text)
        
        return lengths, total