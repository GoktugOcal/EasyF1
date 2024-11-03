from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="easyf1",
    version="0.0.1",
    description="""A Python API wrapper for real-time Formula 1 data collection.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Göktuğ Öcal",
    url="https://github.com/GoktugOcal/EasyF1",
    packages=find_packages(include=["easyf1"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Minimum Python version requirement
    install_requires=required,
    license="MIT",
    project_urls={
        "Bug Tracker": "https://github.com/GoktugOcal/easyF1/issues",
        "Documentation": "https://github.com/GoktugOcal/easyF1#readme",
        "Source Code": "https://github.com/GoktugOcal/easyF1",
    },
    include_package_data=True
)