# -*- coding: utf-8 -*-


class ZbDict(dict):
    """Dict that can get attribute by dot"""

    def __init__(self, *args, **kwargs):
        super(ZbDict, self).__init__(*args, **kwargs)
        self.__dict__ = self
