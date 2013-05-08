# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2010, 2011, 2012 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

from wtforms.validators import ValidationError, StopValidation


class RequiredIf(object):
    """
    """
    def __init__(self, other_field_name, values, message=None):
        self.other_field_name = other_field_name
        self.values = values
        self.message = message

    def __call__(self, form, field):
        try:
            other_field = getattr(form, self.other_field_name)
            other_val = other_field.data
            if other_val in self.values:
                if not field.data or isinstance(field.data, basestring) and not field.data.strip():
                    if self.message is None:
                        self.message = 'This field is required.'
                    field.errors[:] = []
                    raise StopValidation(self.message % {'other_field': other_field.label.text, 'value': other_val})
        except AttributeError:
            pass