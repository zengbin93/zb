# -*- coding: utf-8 -*-

from collections import OrderedDict


class AttrDict(dict):
    """Dict that can get attribute by dot"""

    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


class OrderedAttrDict(OrderedDict):
    """OrderedDict that can get attribute by dot"""

    def __init__(self, *args, **kwargs):
        super(OrderedAttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self
