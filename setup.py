from setuptools import setup, find_packages
import zb

setup(
    name="zb",
    version=zb.__version__,
    keywords=("zb", "tool", "algorithm"),
    description="Personal Package of ZengBin",
    long_description="Personal tools and algorithms.",
    license="Apache-2.0",

    url="https://github.com/zengbin93/zb",
    author=zb.__author__,
    author_email="zeng_bin8888@163.com",

    packages=find_packages(exclude=['test', 'images']),
    include_package_data=True,
    install_requires=[
        "requests", "pandas", "click", "numpy", 'bs4', 'jieba', "pynput"
    ],
    package_data={'': ['*.csv', '*.txt']},
    entry_points={
        "console_scripts": [
            "zb=zb.cli:zb"
        ]
    },
    classifiers=[
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
        ]
)
