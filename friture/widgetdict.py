#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2009 Timoth?Lecomte

# This file is part of Friture.
#
# Friture is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as published by
# the Free Software Foundation.
#
# Friture is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Friture.  If not, see <http://www.gnu.org/licenses/>.

from friture.spectrogram import Spectrogram_Widget

widgets = [
    {'Id': 1, "Class": Spectrogram_Widget, "Name": "2D Spectrogram"},
]


def widgetIds():
    return [widget['Id'] for widget in widgets]


def getWidgetById(widgetId):
    return next(widget for widget in widgets if widget["Id"] == widgetId)
