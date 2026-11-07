"""Python entry point for the original assignment notebook(s)."""

try:
    from .notebook_runner import run_notebook
except ImportError:
    from notebook_runner import run_notebook


def run():
    print("\n=== Support Ticket Triage ===")
    run_notebook("Part_C_Support Ticket Triage with Guardrails .ipynb")


if __name__ == "__main__":
    run()