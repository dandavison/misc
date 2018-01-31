#!/bin/bash

set -e

venv=/tmp/flake8-import-order-venv
virtualenv $venv
. $venv/bin/activate
pip install flake8==2.5.4 flake8-import-order==0.12
cat > bad.py <<EOF
import b
import a
EOF
flake8 - < bad.py
