====================================
 Faculty portfolio for Noah Hoffman
====================================

Source code for https://faculty.washington.edu/ngh2

Set up the environment::

  python3 -m venv py3-env
  source py3-env/bin/activate
  pip install -U pip wheel
  pip install -r requirements.txt

Update publications::

  bin/get_refs.py -o content/pages/publications.md

Launch local server and restart with each page change (requires fswatch)::

  bin/watch.sh

Build::

  make html

Build and upload::

  make publish
