# Install the package locally
pip install .

# Install the package with a symlink
pip install -e .

# Install the package with pip
pip install my_package

# Specifying Dependencies
python setup.py develop

# Running 'Nose' for gettint tests from the root of the repository
pip install nose
nosetests

# To run tests
python setup.py test