"""Python entry point for the original assignment notebook(s)."""
try:
    from .notebook_runner import run_notebook
except ImportError:
    from notebook_runner import run_notebook

def run():
    print("\n=== Support ticket triage ===")
    run_notebook('Support Ticket Triage with Guardrails _Part_C.ipynb')

if __name__ == "__main__":
    run()
