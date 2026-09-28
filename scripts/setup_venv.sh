#!/usr/bin/env bash
# Create the project virtual environment in .venv and register it as a Jupyter kernel.
# Usage (from the project root):  ./scripts/setup_venv.sh        [PYTHON=python3.12 ./scripts/setup_venv.sh]
set -euo pipefail
cd "$(dirname "$0")/.."
PY="${PYTHON:-python3}"

"$PY" - <<'PYCHECK'
import sys
if not ((3, 10) <= sys.version_info[:2] <= (3, 13)):
    sys.exit(f"Python 3.10–3.13 required, found {sys.version.split()[0]}. Set PYTHON=python3.12 (for example).")
PYCHECK

if [ ! -d .venv ]; then
  "$PY" -m venv .venv
fi
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m ipykernel install --user --name party-map --display-name "Party Map (.venv)"

.venv/bin/python - <<'PYTEST'
import numpy, pandas, pyarrow, scipy, sklearn, Stemmer, matplotlib
print("OK:", "numpy", numpy.__version__, "| pandas", pandas.__version__, "| scikit-learn", sklearn.__version__,
      "| stemmer", Stemmer.Stemmer("finnish").stemWord("hallituksen"))
PYTEST
echo
echo "Done. Activate with:  source .venv/bin/activate"
echo "In Jupyter / VS Code choose the kernel 'Party Map (.venv)'."
