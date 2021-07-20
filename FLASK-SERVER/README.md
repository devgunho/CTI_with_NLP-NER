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

<br/>

## To Do List

- [ ] BERT Start Action
  - [ ] https://github.com/kamalkraj/BERT-NER
  - [ ] https://github.com/bond005/deep_ner
- [ ] brat
- [ ] LDA
- [ ] Entity Scoring
- [ ] Time Entity Extraction

<br/>

<br/>
