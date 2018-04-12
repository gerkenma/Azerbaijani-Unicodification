# Azerbaijani-Unicodification

## Team

**Developer**
> Mark Gerken

**Professor:**
> Kevin Scannell, PhD.

## Requirements
- Python 3.3+ (Tested on Python 3.6.4)
- Unidecode 1.0.22
- unidecodecsv 0.14.1

## Set up

1. Install [Python](https://www.python.org/downloads/)
2. If not installed, install Virtualenv with `pip install virtualenv`
3. Navigate in a terminal window to the root directory of the project and set up a virtual environment with `virtualenv venv`
4. Activate the virtual environment with `venv\Scripts\activate` on a Windows machine or `soruce venv\bin\activate`
	- *More complete directions can be found [here](https://virtualenv.pypa.io/en/stable/userguide/#activate-script)*
5. Install the required Python packages with `pip install -r requirements.txt`

## Testing

Training data received from `ajz-train.txt`. Text file contains large corpus of Azjerbaijani text with (presumed) correct diacritics. Program trains off of this data, then receives `input.csv`. This CSV file contains lines of non-decorated Azjerbaijani text and attempts to restore all necessary diacritics. The program outputs the file `prediction.csv`. This file is then uploaded to [Kaggle](https://www.kaggle.com/c/azerbaijani-unicodification/) for scoring.

## Process

**Attempt #1:** Dictionary Style

Memorized each word in training data. If found in test data, replaced word with example seen in training data.
> Result: 0.60232

**Attempt #2/3:** Single letter Unigram

Records each instance of a unique character. Every character is replaced individually with the most commonly seen equivalent, diacritically decorated or not. Attempt #3 was due to fixing logic mistake in code.
> Result: 0.53447
