nosetests -v --with-xunit --all-modules --traverse-namespace --with-coverage --cover-inclusive ExperimentTest.py 2> output.txt
python -m coverage xml --include=*
