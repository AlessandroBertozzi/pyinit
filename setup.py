from setuptools import setup, find_packages

setup(
    name="pyinit",
    version="0.2",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pyinit=pyinit.cli:main",  # Comando globale
        ],
    },
    install_requires=["rich"],
    author="Alessandro Bertozzi",
    description="Uno script per inizializzare velocemente un progetto Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tuo-username/pyinit",  # Modifica con il tuo repository
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
