import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="string_generator",
    version="0.0.1",
    author="Witekkq",
    author_email="",
    description="String bruteforce generator",
    long_description=long_description,
    packages=setuptools.find_packages(),
    install_requires=[],
)
