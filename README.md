# PITA

PredictIt Tracking and Analysis  
Python 3.8 fork (original in Python 2.7)
requires Unix/Linux for Cron scheduling

# Features

Current:  
-Polls the predictit.org API every minute to retrieve current pricing data as a JSON object  
-Inserts data into SQLite3 database using SQLAlchemy ORM  
-Processes requests for historical prices and outputs data as .csv

Future:  
-Train LSTM neural network to predict price movement

# Installation

Clone the directory:

```bash
git clone https://github.com/Talophex/PITA.git
cd PITA
```

Create a [virtualenv](https://docs.python.org/3.8/library/venv.html):

```bash
python3 -m venv venv
```

Activate the virtualenv:

```bash
source venv/bin/activate
```

Self-upgrade pip:

```bash
pip install --upgrade pip
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create the SQLite3 database to store data:

```bash
python CreateDatabase.py
```

Add cron job to poll API once per minute. On Linux or macOS systems, this will modify system wide setttings so that the `PullCurrentData.py` script runs once every minute as long as your computer is on. Make sure you know that you want to do this so it's not running for weeks and months long after you've forgotten about PredictIt:

```bash
python CronScheduler.py
```

# Basic use:

I. To dump price data into csv, run:

```bash

python DumpCSV.py <market-predictit-id>

```

A separate csv file will be created for each contract found in the specified market.

II. To disconnect the current database for storage, run:

```bash

python DisconnectDatabase.py

```

A new database will automatically be created by CreateDatabase.py to ensure no disruptions to data acquisition.
