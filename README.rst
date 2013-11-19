================
run-your-command
================

This is simple one page web application for calling any commands from your browser.

Install
================

Setup your environment
--------------------------

#. Install Python (if you want)
#. Install setuptools (if you don't have)
#. Install virtualenv
#. Create virtual environment

::

  virtualenv -p ~/.pythonz/pythons/CPython-2.7.5/bin/python .pythonz/virtualenv/cpython275-ryc

#. Install nodebrew
#. Intall bower

::

  npm install -g bower

Resolve project dependencies
-----------------------------------

::

  source ~/.pythonz/virtualenv/cpython275-ryc/bin/activate
  pip install -r requirements.txt
  bower install

Run
================

  python main.py

