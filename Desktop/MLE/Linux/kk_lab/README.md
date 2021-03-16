# Install the package locally
```
pip install .
```
# Install the package with a symlink
```
pip install -e .
```
# Install the package with pip
```
pip install kk_lab
```
# Specifying Dependencies
```
python setup.py develop
```
# Running 'Nose' for gettint tests from the root of the repository or run test of test_avg_func.py using unittest
```
python -m unittest test_avg_func.py
```
or
```
pip install nose
nosetest
```
# To run test of setup.py
```
python setup.py test
```
# PyPi - https://test.pypi.org/project/kk-lab/0.1/
```
python3 -m pip install --user --upgrade twine
python3 -m twine upload --repository testpypi dist/*
```
# Install package in new env
```
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps kk_lab
```
