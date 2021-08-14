## Setup Environment [Ubuntu 20.04]

```bash
FLASK-SERVER$ python --version
Python 3.8.10

FLASK-SERVER$ pip install virtualenv
FLASK-SERVER$ virtualenv venv
FLASK-SERVER$ source ./venv/bin/activate

(venv) FLASK-SERVER$ python -m pip install -r requirements.txt
(venv) FLASK-SERVER$ python server.py
```

```bash
(venv) FLASK-SERVER$ pip freeze > requirements.txt
(venv) FLASK-SERVER$ cat requirements.txt
(venv) FLASK-SERVER$ deactivate
```

<br/>

#### brat Installation

```bash
FLASK-SERVER$ git clone https://github.com/nlplab/brat.git
FLASK-SERVER$ cd brat/
FLASK-SERVER/brat$ rm -rf .git
FLASK-SERVER/brat$ ./install.sh -u

# brat username (e.g. “editor”)
# brat password (for the given user, e.g. “annotate”)
# administrator contact email (e.g. “admin@example.com”)

FLASK-SERVER/brat$ python standalone.py
```

<br/>

#### Only run brat

```bash
FLASK-SERVER/brat$ python standalone.py
```

<br/>

## To Do List

- [ ] Crawling
- [ ] MongoDB
  - [x] Simple Connection
  - [ ] Search DB
- [ ] BERT Start Action
  - [x] https://github.com/kamalkraj/BERT-NER
  - [x] Attaching to Flask server
  - [ ] Change `ner_data` to Custom dataset
- [ ] brat
  - [x] Install & Run Server
  - [ ] Auto Annotation
- [ ] LDA
- [ ] Entity Scoring
- [ ] Time Entity Extraction

<br/>

<br/>

## Module Description

- `mongodb_connect.py`
- `run_ner.py`
  - `bert.py`

