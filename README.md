QE Foundations

I do not currently know if this is for the first project or if this is just a week long exercise so idk the purpose yet


Project 1 milestone - Week 2, Monday

Exists - Utility library for future use and folder for future use
To come - Actual Functionality


Setup - My Laptop

python -m venv .venv
.venv/scripts/activate
python -m pip install -r requirements.txt
python smoke_utils.py 

Setup - PowerShell

python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python smoke_utils.py 

Setup - Bash

python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python smoke_utils.py 

Code Execution

PASS  slugify
PASS  is_valid_email
PASS  mask_email
PASS  clamp
PASS  add_days
PASS  days_between
PASS  make_users is repeatable
7/7 checks passed