

### Setup

I used poetry to manage python package information.

To get VSCode to recognize this poetry environment, I had to type:

```
>Python: Select Interpreter
```

into the search bar in VSCode, then enter the path to this projects virtual environment.

Then, when I open a `.ipynb` file, I can click "Select Interpreter" > "Select another Kernel" > "Python Environment" and the python env will show up 

To get poetry to work with jupyter notebooks, I had to follow the advice from [here](https://stackoverflow.com/questions/72434896/jupyter-kernel-doesnt-use-poetry-environment)

Also, you have to downgrade numpy to version 1.26 and change the pinned versions for python to `python = ">=3.10,<3.13"`
