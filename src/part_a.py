"""Python entry point for the original assignment notebook(s)."""
try:
    from .notebook_runner import run_notebook
except ImportError:
    from notebook_runner import run_notebook

def run():
    print("\n=== Clean raw CSV data ===")
    run_notebook('Data_Cleaning_part_a.ipynb')
    print("\n=== Create and query SQLite database ===")
    run_notebook('SQL_Database_part_a.ipynb')

if __name__ == "__main__":
    run()
