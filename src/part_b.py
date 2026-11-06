"""Python entry point for the original assignment notebook(s)."""
try:
    from .notebook_runner import run_notebook
except ImportError:
    from notebook_runner import run_notebook

def run():
    print("\n=== Customer segmentation and lapse prediction ===")
    run_notebook('Customer Segments and Lapse Prediction_Part_B.ipynb')

if __name__ == "__main__":
    run()
