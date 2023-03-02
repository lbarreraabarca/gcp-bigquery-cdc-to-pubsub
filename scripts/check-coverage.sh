
cd src
python -m coverage run -m unittest
python -m coverage report --omit="*__init__.py,*test*.py"
