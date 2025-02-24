====================================
 Faculty portfolio for Noah Hoffman
====================================

Source code for https://faculty.washington.edu/ngh2

Populate the Flex submodule after cloning::

  git submodule update

Set up the environment::

  uv venv
  source .venv/bin/activate
  uv pip install -r requirements.txt

Update publications::

  bin/get_refs.py -o content/pages/publications.md

Launch local server and restart with each page change (requires fswatch)::

  bin/watch.sh

Build::

  make html

Build and upload::

  make publish
