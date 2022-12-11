# About

## Decathlon score counter

This app takes a CSV file as input with scores.
Counts points, ranks contestants
and outputs the data in JSON format.

# Setup

Access new directory via VSCode. Enter into a terminal window

```
git clone https://github.com/Gerkano/decathlon-score-counter.git
```

Create a virtual environment by typing into terminal window:

```
python -m venv venv
```

Activate the virtual environment

```
.\venv\Scripts\activate
```

Install requirements

```
pip install -r requirements.txt
```

Start the app by typing

```
py .\decathlon_point_counter\app.py
```

Click on this link, to acces the form:

http://127.0.0.1:5000/

# Input/Output

For input, only CSV type format is allowed.
The JSON file, with results, and CSV file,
will appear in static/files folder

# Algorithm diagram

You'll also find an algorithm diagram,
which highlights main procceses of this application
