## Setup Env.

```powershell
> python --version
Python 3.8.10

FLASK-SERVER> pip install virtualenv
FLASK-SERVER> virtualenv venv	// virtualenv 'virtual environment name'
FLASK-SERVER> .\venv\Scripts\Activate

(venv) FLASK-SERVER> python -m pip install -r requirements.txt

(venv) FLASK-SERVER> python server.py
```

```powershell
(venv) FLASK-SERVER> pip freeze > requirements.txt
(venv) FLASK-SERVER> cat requirements.txt
(venv) FLASK-SERVER> deactivate
```

<br/>

### Ubuntu 20.04

```bash
FLASK-SERVER$ virtualenv venv
FLASK-SERVER$ source ./venv/bin/activate
FLASK-SERVER$ python -m pip install -r requirements.txt
FLASK-SERVER$ python server.py
```

<br/>

<br/>

## To Do List

- [ ] MongoDB
  - [x] Simple Connection
  - [ ] Search DB
- [ ] BERT Start Action
  - [x] https://github.com/kamalkraj/BERT-NER
  - [x] Attaching to Flask server
  - [ ] Change `ner_data` to Custom dataset
- [ ] brat
  - [ ] Install & Run Server
- [ ] LDA
- [ ] Entity Scoring
- [ ] Time Entity Extraction

<br/>

<br/>

## Module Description

- `mongodb_connect.py`
- `run_ner.py`
  - `bert.py`

