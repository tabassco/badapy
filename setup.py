import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="badapy",
    version="0.2",
    author="Tim Kreitner",
    author_email="tim@kreitner.xyz",
    description="python package implementation of the EUROCONTROL BADA calculationse",
    classifiers=['Programming Language :: Python :: 3.6',
                 'Development Status :: Beta'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scipy'
    ]
)

