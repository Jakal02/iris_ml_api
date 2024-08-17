

### Setup

I used the classic python venv to manage this project.

To get started, make `model` your root directory, then run:
```bash
$ python3 -m venv (venv name here)
$ source ./venv/bin/activate
$ python3 -m pip install -r requirements.txt 
```

To get VSCode to recognize this environment, I had to type:

```
>Python: Select Interpreter
```

into the search bar in VSCode, then enter the path to this projects virtual environment.

Then, when I open a `.ipynb` file, I can click "Select Interpreter" > "Select another Kernel" > "Python Environment" and the python env will show up 

Also, I had to downgrade numpy to version 1.26 and change the pinned versions for python to `python = ">=3.10,<3.13"`
