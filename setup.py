import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SteamSystems",
    version="20.5",
    author="Kai Norvell",
    author_email="kainorvell@gmail.com",
    description="A python package for steam/rankine cycle modelling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Norvell-git/SteamSystems",
    packages=setuptools.find_packages(),
    install_requires=['IAPPWS', 'numpy', 'scipy']
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
