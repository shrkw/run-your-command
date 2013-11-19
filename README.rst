================
run-your-command
================

**Important notice**

*This application expects to work for internal network and faithful guys only.*
*You must not provide this for internet and unnkown guys. If you don't accept this alert, your server may make trouble to not only your server but also other network.*

This is simple one page web application for calling any commands from your browser.

.. image:: https://r4jsig.blu.livefilestore.com/y2mLlEDXtbb65QNrX9JHZoNDIM2qiUCdTRNUttdDd-sjKf0nYceLyiA2UiTzrBycmK1iLQZjOMC8ObWcjmEehMCTASThI9e4Ln9zKh8NKIooBlo-mdKFqZ668V00hNRbz4F/image.png?psid=1
   :alt: screen image

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

