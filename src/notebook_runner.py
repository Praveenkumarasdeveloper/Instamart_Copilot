
"""Helpers for executing the original assignment notebooks."""

from pathlib import Path
import nbformat
from nbclient import NotebookClient


PROJECT_ROOT = Path(__file__).resolve().parents[1]

NOTEBOOK_DIRS = [
    PROJECT_ROOT,
    PROJECT_ROOT / "notebooks"
]


def run_notebook(filename: str):

    # Find the notebook
    path = next(
        (
            folder / filename
            for folder in NOTEBOOK_DIRS
            if (folder / filename).is_file()
        ),
        None
    )

    if path is None:
        checked_paths = "\n".join(
            str(folder / filename)
            for folder in NOTEBOOK_DIRS
        )
        raise FileNotFoundError(
            f"Notebook not found. Checked:\n{checked_paths}"
        )

    print(f"\nRunning notebook: {path.name}")

    # Read notebook
    notebook = nbformat.read(path, as_version=4)

    # Execute notebook
    client = NotebookClient(
        notebook,
        timeout=1200,
        kernel_name="python3",
        resources={"metadata": {"path": str(PROJECT_ROOT)}},
        allow_errors=False,
    )

    client.execute()

    # Save executed notebook
    output_dir = PROJECT_ROOT / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)

    executed_path = output_dir / f"{path.stem}_executed.ipynb"

    nbformat.write(notebook, executed_path)

    print("\nNotebook executed successfully!")
    print(f"Saved at: {executed_path}")

    return executed_path
