"""Python entry point for the original assignment notebook(s)."""

try:
    from .notebook_runner import run_notebook
except ImportError:
    from notebook_runner import run_notebook


def run():
    print("\n=== Clean Raw CSV Data ===")
    run_notebook("Part_A_Data_Cleaning.ipynb")

    print("\n=== Create and Query SQLite Database ===")
    run_notebook("Part_A_SQL_Database.ipynb")


if __name__ == "__main__":
    run()