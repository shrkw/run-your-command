================
run-your-command
================

This is simple one page web application for calling any commands from your browser.

.. image:: https://www.dropbox.com/s/omx6sjha1e9vaga/image.png

Install
================

Setup your environment
--------------------------

Install Python (if you want)

Install setuptools (if you don't have)

Install virtualenv::

  pip install virtualenv

Create virtual environment::

  virtualenv -p ~/.pythonz/pythons/CPython-2.7.5/bin/python .pythonz/virtualenv/cpython275-ryc

Install nodebrew and Node.js::

  curl -L git.io/nodebrew | perl - setup
  export PATH=$HOME/.nodebrew/current/bin:$PATH
  nodebrew install stable
  nodebrew use stable

Intall bower::

  npm install -g bower

Resolve project dependencies
-----------------------------------

::

  source ~/.pythonz/virtualenv/cpython275-ryc/bin/activate
  pip install -r requirements.txt
  bower install

Run
================

::

  python main.py

