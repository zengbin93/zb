# -*- coding: utf-8 -*-


class ZbDict(dict):
    """Dict that can get attribute by dot"""

    def __init__(self, *args, **kwargs):
        super(ZbDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


class ZbList(list):
    """List that can get elements by discrete indices"""
    def __init__(self, *args, **kwargs):
        super(ZbList, self).__init__(*args, **kwargs)

    def discrete_index(self, indices):
        """get elements by discrete indices

        :param indices: list
            discrete indices
        :return: elements
        """
        elements = []
        for i in indices:
            elements.append(self[i])
        return elements


