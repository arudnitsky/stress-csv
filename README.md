# stress-csv

Quick and dirty python script to add pronunciation stress marks to csv files intended for importing into Anki.
- The script expects the first field to be in Ukrainian.
- Input can be read from a file, or provided on stdin.
- The separator is assumed to be a comma.
- Single column files are fine.
- Fields with commas must be quoted.

## Set up development environment - need to generate requirements

Set up the python virtual environment. Note: Use these commands because pyenv and pip seem to not get along. 
1. `python3 -m venv .venv`
1. `source .venv/bin/activate`
1. `python3 -m pip install -r requirements.txt`

Remember to `pip freeze > requirements.txt` if adding stuff via `pip install`

## Developer notes

### TODO

1. Add command line parsing and usage output
1. Quote all CSV output 