# Python Virtual Environment Setup

## Create virtual environment
python -m venv venv

## Activate virtual environment
### Windows:
venv\Scripts\activate

### Linux/Mac:
source venv/bin/activate

## Install dependencies
pip install -r requirements.txt

## Run tests
pytest JPMC-tech-task-1-PY3/client_test.py

## Deactivate when done
deactivate
