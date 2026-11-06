"""Python entry point for the original assignment notebook(s)."""
try:
    from .notebook_runner import run_notebook
except ImportError:
    from notebook_runner import run_notebook

def run():
    print("\n=== Policy RAG and refund agent ===")
    run_notebook('Policy RAG Assistant and Refund Agent_Part_D.ipynb')

if __name__ == "__main__":
    run()
