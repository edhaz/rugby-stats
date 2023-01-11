from distutils.core import setup

setup(
    name="rugby",
    version="1.0",
    description="Rugby web app",
    author="Ed Hazledine",
    author_email="ed.hazledine@gmail.com",
    packages=["rugby"],
    install_requires=["flask", "flask_sqlalchemy", "requests", "bs4"],
    extras_require={"test": ["pytest"]},
)
