# Python Data Structures
Simple package containing fundamental data structures used in coding questions. 
Meant to be used in personal projects only, and makes absolutely no guarantees.

[![](https://github.com/asarkar/pydata/workflows/CI/badge.svg)](https://github.com/asarkar/pydata/actions)

## Development

```
pydata% ./venv/bin/python -m pip install --upgrade pip

pydata% ./venv/bin/python -m pip install -e '.[dev]' wheel

pydata% ./venv/bin/python -m pip wheel --no-binary pydata --wheel-dir=dist -e .

```

## Running tests
```
./.github/run.sh <directory>
```

## License

Released under [Apache License v2.0](LICENSE).