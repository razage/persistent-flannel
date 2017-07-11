# Persistent Flannel [![Build Status](https://travis-ci.org/razage/persistent-flannel.svg?branch=master)](https://travis-ci.org/razage/persistent-flannel)

## Development
I am developing this project using Python 3.6. While I'm not entirely sure if there's any features I'm using *exclusive* 
to 3.6, I can definitely verify it will not work for Python 2.7. I have no intention of supporting 2.7 and any issues 
related to 2.7 (or older) compatibility will be ignored.

### Required Applications
Ignoring Python 3.6, you will also need
* MySQL Server
* Node (for npm)

### Code
* I almost always adhere to PEP8 guidelines, with the major exception of my line length being longer (120 characters). I
use [Pycharm](https://www.jetbrains.com/pycharm/) as my editor, and I *highly* recommend you do as well. I will view all
pull requests in this environment to verify that the formatting is correct.
* I won't demand that all code has docstrings, but anything that is cryptic should. I will comment on pull requests and
ask for documentation if I don't understand something.

### Tests
No pull requests will be merged in unless all the tests pass. If your pull request is substantial enough, you may also
be expected to write tests for your methods. Tests should be as easy to run as double clicking them, or in clicking the
run button in Pycharm. If you want to run *all* of the tests at once, type `python -m pytest` in a command prompt from
within the project's directory. Note that if you're on Windows, this assumes that you add Python to your PATH.

### Database
I am using MySQL, and that is all I can guarantee will work. If you are developing on Windows, you can easily download
an installer from the MySQL website. If you are on Mac or Linux, you can install it in many ways 
(apt, yum, homebrew, etc).

## Installation
* Clone/download the repository
* `pip install -r requirements.txt`
* `npm install`
* Execute `create_db.py`

Make sure to execute these commands in the project's directory. A virtual environment is recommended, but not required.

### Configuration
You can look at the `config-example.py` to see what is configurable. Currently the only thing that is different in my
working config is the `SQLALCHEMY_DATABASE_URI`. This should point to wherever you're hosting your MySQL server and use
whatever credentials you created. 