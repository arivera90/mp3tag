from setuptools import setup

setup (
    name = 'Mp3tag',
    description = "Gui for mp3 tag edition.",
    author = "Alberto Rivera",
    author_email= "alberto.rivera.garcia@gmail.com",
    version ="0.0.1",
    packages= ["Mp3tag"],
    entry_points = {"console_scripts": ["Mp3tag = Mp3tag.__main__:main"]},
    install_requires = ["PyQt6"]
)