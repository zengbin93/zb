from setuptools import setup, find_packages
import zb

setup(
    name="zb",
    version=zb.__version__,
    keywords=("zb", "tool", "algorithm"),
    description="Personal Package of ZengBin",
    long_description="Personal established tools and implement of algorithm. ",
    license="Apache-2.0",

    url="https://github.com/zengbin93/zb",
    author=zb.__author__,
    author_email="zeng_bin8888@163.com",

    packages=find_packages(exclude=['code_set', 'test', 'images']),
    include_package_data=True,
    install_requires=[
        "requests", "pandas", "click", 'retrying',
        "numpy", "wxpy"
    ],
    entry_points={
        "console_scripts": [
            "zb=zb.cli:zb"
        ]
    }
)
