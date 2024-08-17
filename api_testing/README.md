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


## Running a test

1. Start the API service using `just start-backend`
2. Make a new terminal, make sure that the venv in this directory is activated
3. run `locust` and open the web terminal
4. Enter the information and start it.
5. Watch your API handle all of those requests.
