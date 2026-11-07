"""Python entry point for the original assignment notebook(s)."""

try:
    from .notebook_runner import run_notebook
except ImportError:
    from notebook_runner import run_notebook


def run():
    print("\n=== Customer Segmentation and Lapse Prediction ===")

    run_notebook(
        "Part_B_Customer Segments and Lapse Prediction.ipynb"
    )


if __name__ == "__main__":
    run()