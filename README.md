# zb
[`zb`](https://pypi.org/project/zb/) is a python module, which contains some
 tools and algorithm implemented by myself.

If you are interested in this module, you can install it by `pip install zb`.


安装：`pip install zb -U -i https://pypi.python.org/simple`


## Tools

* Modify Dict

```python
from zb import AttrDict, OrderedAttrDict

# AttrDict is a dict that can get attribute by dot
d1 = AttrDict(x=1, y=2)
print(d1, '\n', d1.x, d1.y)

# OrderedAttrDict is same as AttrDict, but items are ordered
d2 = OrderedAttrDict(x=1, y=2)
print(d2, '\n', d2.x, d2.y)
```


* extract text from pdf file - `zb.tools.pdf.pdf2text`

```python
from zb.tools import pdf2text

pdf_path = "test.pdf"
pdf_url = "http://www.cninfo.com.cn/cninfo-new/disclosure/szse/download/1205276701?announceTime=2018-08-11"
text = pdf2text(pdf_path)
```


