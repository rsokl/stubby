from setuptools import find_packages, setup

DISTNAME = "stubby"

setup(
    name=DISTNAME,
    version="1.0.0",
    python_requires=">=3.6",
    packages=find_packages(where="src", exclude=["tests", "tests.*"]),
    package_dir={"": "src"},
)
