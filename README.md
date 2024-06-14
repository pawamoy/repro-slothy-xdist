# Issue between Slothy and Pytest XDist

```bash
git clone https://github.com/pawamoy/repro-slothy-xdist
cd repro-slothy-xdist
uv venv
uv pip install -r requirements.txt
. .venv/bin/activate
PYTHONPATH=. pytest tests --dist no  # OK
PYTHONPATH=. pytest tests -n auto  # STILL OK BUT SHOULDN'T, WORKING ON REPRO
```
