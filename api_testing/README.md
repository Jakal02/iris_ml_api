# Testing

Instead of running unit tests inside of the docker container, 
its important to verify that the application as a standalone process works.  

To measure API response time and to test the limits of its load, we will use Locust.

## Setup

Begin by creating and installing packages into a virtual environment.

```bash
$ python3 -m venv (venv name here)
$ source ./venv/bin/activate
$ python3 -m pip install -r requirements.txt 
```

