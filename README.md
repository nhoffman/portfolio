# Faculty portfolio for Noah Hoffman

Source code for https://faculty.washington.edu/ngh2

## Setup Instructions

### Initialize Submodules

After cloning, populate the Flex submodule:
```bash
git submodule update
```

### Set up the Environment

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### Update Publications

```bash
bin/get_refs.py -o content/pages/publications.md
```

### Local Development

Launch local server and restart with each page change (requires fswatch):

```bash
bin/watch.sh
```

### Build

```bash
make html
```

### Deploy

Build and upload:

```bash
make publish
```
