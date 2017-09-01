#!/bin/bash

cd /vagrant

# Windows doesn't support symlinks, so virtualbox/vagrant shared folders on a 
# Windows host does not, use --no-bin-links
echo "npm --no-bin-links install"
npm --no-bin-links install

# same deal with virtualenv and symlinks
virtualenv --always-copy mwachx-virtualenv

# use the virtualenv for the rest of the python stuff
source mwachx-virtualenv/bin/activate
pip install -r requirements.txt
dos2unix /vagrant/manage.py
python manage.py migrate