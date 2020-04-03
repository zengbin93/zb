# -*- coding: utf-8 -*-

import warnings
import six


class Deprecated(object):
    """支持装饰类或者方法，在使用类或者方法时警告Deprecated信息

    borrowed from `abu\abupy\CoreBu\ABuDeprecated.py`
    """

    def __init__(self, tip_info=''):
        self.tip_info = tip_info

    def __call__(self, obj):
        if isinstance(obj, six.class_types):
            return self._decorate_class(obj)
        else:
            return self._decorate_fun(obj)

    def _decorate_class(self, cls):
        """实现类装饰警告Deprecated信息"""

        msg = "class {} is deprecated".format(cls.__name__)
        if self.tip_info:
            msg += "; {}".format(self.tip_info)
        # 取出原始init
        init = cls.__init__

        def wrapped(*args, **kwargs):
            warnings.warn(msg, category=DeprecationWarning)
            return init(*args, **kwargs)

        cls.__init__ = wrapped

        wrapped.__name__ = '__init__'
        wrapped.__doc__ = self._update_doc(init.__doc__)
        # init成为deprecated_original，必须要使用这个属性名字
        wrapped.deprecated_original = init

        return cls

    def _decorate_fun(self, fun):
        """实现方法装饰警告Deprecated信息"""

        msg = "function `{}` is deprecated".format(fun.__name__)
        if self.tip_info:
            msg += "; {}".format(self.tip_info)

        def wrapped(*args, **kwargs):
            warnings.warn(msg, category=DeprecationWarning)
            return fun(*args, **kwargs)

        # update meta
        wrapped.__name__ = fun.__name__
        wrapped.__dict__ = fun.__dict__
        wrapped.__doc__ = self._update_doc(fun.__doc__)

        return wrapped

    def _update_doc(self, func_doc):
        """更新文档信息，把原来的文档信息进行合并格式化,
        即第一行为deprecated_doc(Deprecated: tip_info)，下一行为原始func_doc"""
        deprecated_doc = "Deprecated"
        if self.tip_info:
            deprecated_doc = "{}: {}".format(deprecated_doc, self.tip_info)
        if func_doc:
            func_doc = "{}\n{}".format(deprecated_doc, func_doc)
        return func_doc
