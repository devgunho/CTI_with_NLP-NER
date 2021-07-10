# Reference Datasets for CTI NER tagging

<br/>

### Table of contents

- `.ipynb`
  - Data-Detail.ipynb
    - Code showing current dictionary status
  - Comparative_Analysis_with_nltk.ipynb
    - After comparison validation with open word datasets, only pure security jargon is left.

- MongoDB
  - Managing Jargon Dictionry for Cybersecurity
- CoNLL 2003 (English) Dataset
- MITRE ATT&CTK® Website

<br/>

<br/>

## # MongoDB

*It does not disclose its vocabulary dictionary related to CTI, which is being developed secretly.*

*However, the process of processing NLPs using a hand-crafted dictionary could be explored indirectly.*

<br/>

### My Own Instructions

#### db.collection.insertMany()

```
db.collection.insertMany([
  { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
  {
    item: "notebook",
    qty: 50,
    size: { h: 8.5, w: 11, uom: "in" },
    status: "A",
  },
  { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
  {
    item: "planner",
    qty: 75,
    size: { h: 22.85, w: 30, uom: "cm" },
    status: "D",
  },
  {
    item: "postcard",
    qty: 45,
    size: { h: 10, w: 15.25, uom: "cm" },
    status: "A",
  },
]);
db.dictionary.update({}, { $rename: { ner: "entity" } }, false, true);
db.dictionary.createIndex({ corpus: 1 }, { unique: true });

db.entity.createIndex({ entity: 1 }, { unique: true });
db.entity.insert([{ entity: "IP" }]);
//E11000 duplicate key error collection: CTI-DICTIONARY.entity index: entity_1 dup key: { entity: "IP" }

db.dictionary.getIndexes();
db.dictionary.dropIndexes();
```

<br/>

#### db.collection.find()

```
db.getCollection("dictionary").find({ entity: "LOCATION" });
db.getCollection("dictionary").find({ category: "filename-extensions" });
db.getCollection("dictionary").find({ entity: "HASH" });
db.getCollection("dictionary").find({ corpus: "Suzhou" });
```

<br/>

#### Existence Check

```
db.getCollection('dictionary').find({category:{$exists:false}})
```

<br/>

#### Add field if conditions are correct

```
db.dictionary.updateMany(
  { entity: "LOCATION" },
  { $set: { category: "location" } }
);
db.dictionary.updateMany(
  { entity: "THREAT-ACTOR" },
  { $set: { category: "mitre-groups" } }
);
db.dictionary.updateMany(
  { entity: "MITIGATIONS" },
  { $set: { entity: "MITIGATION" } }
);
db.dictionary.updateMany(
  { category: "HASH-md5" },
  { $set: { category: "hash-md5" } }
);
db.dictionary.updateMany(
  { category: "HASH-sha256" },
  { $set: { category: "hash-sha256" } }
);
db.dictionary.updateMany(
  { category: "HASH-sha1" },
  { $set: { category: "hash-sha1" } }
);
db.dictionary.updateMany(
  { category: "location" },
  { $set: { category: "location-country" } }
);
```

<br/>

#### Removes all documents that match the `filter` from a collection.

```
db.dictionary.deleteMany({ category: "filename-extensions" });
db.dictionary.deleteMany({ category: "cve-ver-20061101" });
db.dictionary.deleteMany({ category: "location-city" });
db.dictionary.deleteMany({ category: "emails-in-the-article" });
db.dictionary.deleteMany({ category: "ip-v4" });
```

<br/>

#### Delete a Single Document

```
db.dictionary.deleteOne({ corpus: "go" });
db.dictionary.deleteOne({ corpus: "March" });
db.dictionary.deleteOne({ corpus: "We" });
db.dictionary.deleteOne({ corpus: "As" });
db.dictionary.deleteOne({ corpus: "Log" });
db.dictionary.deleteOne({ corpus: "Media" });
db.dictionary.deleteOne({ corpus: "Trail" });
db.dictionary.deleteOne({ corpus: "August" });
db.dictionary.deleteOne({ corpus: "Store" });
db.dictionary.deleteOne({ corpus: "Most" });
db.dictionary.deleteOne({ corpus: "Mobile" });
db.dictionary.deleteOne({ corpus: "Justice" });
db.dictionary.deleteOne({ corpus: "Man" });
db.dictionary.deleteOne({ corpus: "Spring" });
db.dictionary.deleteOne({ corpus: "SID" });
db.dictionary.deleteOne({ corpus: "Lower" });
db.dictionary.deleteOne({ corpus: "Upper" });
db.dictionary.deleteOne({ corpus: "Talent" });
db.dictionary.deleteOne({ corpus: "Baker" });
db.dictionary.deleteOne({ corpus: "Beacon" });
db.dictionary.deleteOne({ corpus: "March" });
db.dictionary.deleteOne({ corpus: "Player" });
db.dictionary.deleteOne({ corpus: "Tor" });
db.dictionary.deleteOne({ corpus: "Police" });
db.dictionary.deleteOne({ corpus: "January" });
db.dictionary.deleteOne({ corpus: "February" });
db.dictionary.deleteOne({ corpus: "April" });
db.dictionary.deleteOne({ corpus: "May" });
db.dictionary.deleteOne({ corpus: "June" });
db.dictionary.deleteOne({ corpus: "July" });
db.dictionary.deleteOne({ corpus: "August" });
db.dictionary.deleteOne({ corpus: "September" });
db.dictionary.deleteOne({ corpus: "October" });
db.dictionary.deleteOne({ corpus: "November" });
db.dictionary.deleteOne({ corpus: "December" });
db.dictionary.deleteOne({ corpus: "Elon" });
db.dictionary.deleteOne({ corpus: "Welcome" });
db.dictionary.deleteOne({ corpus: "Denis" });
db.dictionary.deleteOne({ corpus: "Obama" });
db.dictionary.deleteOne({ corpus: "Of" });
db.dictionary.deleteOne({ corpus: "Center" });
db.dictionary.deleteOne({ corpus: "David" });
db.dictionary.deleteOne({ corpus: "Save" });
db.dictionary.deleteOne({ corpus: "netstat" });
db.dictionary.deleteOne({ corpus: "Nice" });
db.dictionary.deleteOne({ corpus: "Media" });
db.dictionary.deleteOne({ corpus: "Jordan" });
db.dictionary.deleteOne({ corpus: "TUR" });
db.dictionary.deleteOne({ corpus: "Middle" });
```

<br/>

<br/>

## # **CoNLL 2003 (English) Dataset**

> https://deepai.org/dataset/conll-2003-english

##### Some excerpts from the original data

```
Japan NNP B-NP B-LOC
began VBD B-VP O
the DT B-NP O
defence NN I-NP O
of IN B-PP O
their PRP$ B-NP O
Asian JJ I-NP B-MISC
Cup NNP I-NP I-MISC
title NN I-NP O
with IN B-PP O
a DT B-NP O
lucky JJ I-NP O
2-1 CD I-NP O
win VBP B-VP O
against IN B-PP O
Syria NNP B-NP B-LOC
in IN B-PP O
a DT B-NP O
Group NNP I-NP O
C NNP I-NP O
championship NN I-NP O
match NN I-NP O
on IN B-PP O
Friday NNP B-NP O
. . O O
```

<br/>

##### Size

```
  748095 test.txt
 3283420 train.txt
  827443 valid.txt
```

<br/>

<br/>

## # MITRE ATT&CTK® Website

>https://github.com/mitre-attack/attack-website

This repository contains the source code used to generate the MITRE ATT&CK® website as seen at `attack.mitre.org`. The source code is flexible to allow users to generate the site with custom content.

<br/>

### Usage

The [Install and Run](https://github.com/mitre-attack/attack-website#Install-and-Build) section below explains how to set up a local version of the site. You can also visit the live site at [attack.mitre.org](https://attack.mitre.org/). If you want to extend the style, content or functionality of this site, please see our [Customizing the ATT&CK Website](https://github.com/mitre-attack/attack-website/blob/master/CUSTOMIZING.md) document for tips and tricks.

Use our [Github Issue Tracker](https://github.com/mitre-attack/attack-website/issues) to let us know of any bugs or other issues you encounter. We also encourage pull requests if you've extended the site in a cool way and want to share back to the community!

If you find errors or typos in the site content, please let us know by sending an email to [attack@mitre.org](mailto:attack@mitre.org) with the subject **Website Content Error**, and make sure to include both a description of the error and the URL at which it can be found.

*See [CONTRIBUTING.md](https://github.com/mitre-attack/attack-website/blob/master/CONTRIBUTING.md) for more information on making contributions to the ATT&CK website.*

<br/>

### Requirements

- [python](https://www.python.org/) 3.6 or greater

<br/>

### Install and Build

- **Install requirements**

1. Create a virtual environment:
   - macOS and Linux: `python3 -m venv env`
   - Windows: `py -m venv env`
2. Activate the virtual environment:
   - macOS and Linux: `source env/bin/activate`
   - Windows: `env/Scripts/activate.bat`
3. Install requirement packages: `pip3 install -r requirements.txt`

<br/>

### Build and serve the local site

1. Update ATT&CK markdown from the STIX content, and generate the output html from the markdown: `python3 update-attack.py`. *Note: `update-attack.py`, has many optional command line arguments which affect the behavior of the build. Run `python3 update-attack.py -h` for a list of arguments and an explanation of their functionality.*

2. Serve the html to `localhost:8000`

   1. `cd output`
2. `python3 -m pelican.server`

<br/>

### Installing, building, and serving the site via Docker

1. Build the docker image:
   - `docker build -t <your_preferred_image_name> .`
2. Run a docker container:
   - `docker run --name <your_preferred_container_name -d -p <your_preferred_port>:80 <image_name_from_build_command>`
3. View the site on your preferred localhost port

<br/>

### Related MITRE Work

#### CTI

[Cyber Threat Intelligence repository](https://github.com/mitre/cti) of the ATT&CK catalog expressed in STIX 2.0 JSON.

#### ATT&CK Navigator

The ATT&CK Navigator is an open-source tool providing basic navigation and annotation of ATT&CK matrices, something that people are already doing today in tools like Excel. It is designed to be simple and generic - you can use the Navigator to visualize your defensive coverage, your red/blue team planning, the frequency of detected techniques, and more.

https://github.com/mitre-attack/attack-navigator

#### STIX

Structured Threat Information Expression (STIX™) is a language and serialization format used to exchange cyber threat intelligence (CTI).

STIX enables organizations to share CTI with one another in a consistent and machine readable manner, allowing security communities to better understand what computer-based attacks they are most likely to see and to anticipate and/or respond to those attacks faster and more effectively.

STIX is designed to improve many different capabilities, such as collaborative threat analysis, automated threat exchange, automated detection and response, and more.

https://oasis-open.github.io/cti-documentation/

<br/>

### Notice

Copyright 2015-2020 The MITRE Corporation

Approved for Public Release; Distribution Unlimited. Case Number 19-3504.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

This project makes use of ATT&CK®

[ATT&CK Terms of Use](https://attack.mitre.org/resources/terms-of-use/)

