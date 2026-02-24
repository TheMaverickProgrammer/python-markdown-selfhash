# mkdselfhash
A [Python-Markdown][PYTHON_MARKDOWN] preprocessor extension that creates in-place links to be shared with others.

Transforms `{#str}` into `<a href="#str" class="mkdselfhash">str</a><span id="str"/>`.

View this package on [PyPi][PYPI].

# Installation
```shell
pip install mkdselfhash
```

# Testing
1. Install `pytest` via `pip install pytest`.
1. Enter the `test` directory.
1. Run `python -m pytest`. 

[PYTHON_MARKDOWN]: https://github.com/waylan/Python-Markdown
[PYPI]: https://github.com/TheMaverickProgrammer/python-markdown-mkdselfhash
