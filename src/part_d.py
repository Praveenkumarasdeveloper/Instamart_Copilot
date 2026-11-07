"""Part D: Policy RAG Assistant and Refund Agent."""

try:
    from .notebook_runner import run_notebook
except ImportError:
    from notebook_runner import run_notebook


def run():
    print("\n=== Policy RAG and Refund Agent ===")

    run_notebook(
        "Part_D_Policy RAG Assistant and Refund Agent.ipynb"
    )


if __name__ == "__main__":
    run()