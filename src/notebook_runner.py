"""Helpers for running the original assignment notebooks as Python entry points.

The notebooks remain the authoritative implementation. This wrapper executes them
in order without rewriting their calculations or model settings.
"""
from pathlib import Path
import nbformat
from nbclient import NotebookClient

PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_DIR = PROJECT_ROOT / "notebooks"

def run_notebook(filename: str):
    path = NOTEBOOK_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Required notebook not found: {path}")
    notebook = nbformat.read(path, as_version=4)
    client = NotebookClient(
        notebook,
        timeout=1200,
        kernel_name="python3",
        resources={"metadata": {"path": str(PROJECT_ROOT)}},
        allow_errors=True,
    )
    client.execute()
    # Continue past exploratory/debug cells that contain recorded notebook errors.
    executed_path = PROJECT_ROOT / "outputs" / f"{path.stem}_executed.ipynb"
    executed_path.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(notebook, executed_path)
    print(f"Completed: {filename}")
    print(f"Executed notebook saved: {executed_path.relative_to(PROJECT_ROOT)}")
    return executed_path
