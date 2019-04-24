# Ogame

This script allows you to automate fleet.


## Install

Clone the repository

`git clone https://github.com/DONSA/ogame.git`

`cd ogame`

`mv .env-dist .env`

Edit .env and add your credentials

Edit coordinates.py file and add your planets info

`source bin/activate`

Install necessary modules if you are running the script for the first time

`pip install ogame && pip install python-decouple`


## Run

First argument should be the destination planet **alias** specified in `coordinates.py` followed by origin.
You can specify as many origin planets as you need.

`python fleet.py destination origin1 origin2`

`python attack.py origin`

To exit python virtual environment

`deactivate`
