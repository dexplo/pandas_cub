import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pandas_cub",
    version="0.0.6",
    author="Ted Petrou",
    author_email="ted@dunderdata.com",
    description="A simple data analysis library similar to pandas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dexplo/pandas_cub",
    packages=setuptools.find_packages(exclude=['tests']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
