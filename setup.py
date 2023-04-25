import setuptools
import subprocess
import os

rDuplicate_version = subprocess.run(['git', 'describe', '--tags', '--abbrev=0'], stdout=subprocess.PIPE).decode('utf-8').strip()
assert "." in  rDuplicate_version

assert os.path.isfile("rDuplicate/version.py")
with open("rDuplicate/version.py", "w", encoding="utf-8") as fh:
    fh.write(f"__version__ = '{rDuplicate_version}\n'")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rDuplicate",
    version=rDuplicate_version,
    author="Dan Malengela",
    description="A simple duplicate file finder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DanMM7/rDuplicate",
    packages=setuptools.find_packages(),
    package_data={'rDuplicate': ['version.py']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "rDuplicate = rDuplicate.rDuplicate:main"
        ]
    },
    install_requires=[
        "cryptography >=3.4.4",
        "fabric >=2.6.0",
        "paramiko >=2.7.2",
        "requests >=2.25.0",
        "apache-libcloud >=3.3.1",
    ],
)