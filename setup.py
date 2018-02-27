from setuptools import setup, find_packages
import zb

setup(
    name="zb",
    version=zb.__version__,
    keywords=("zb", "tool", "algorithm"),
    description="Personal Package",
    long_description="Personal established tools and implement of algorithm. ",
    license="Apache-2.0",

    url="https://github.com/zengbin93/zb",
    author="zengbin",
    author_email="zeng_bin8888@163.com",

    packages=find_packages(),
    package_data={
    },
    include_package_data=True,
    install_requires=["requests", "pandas", "click", 'retrying'],

    entry_points=dict(console_scripts=[
        ''
    ]),
)
