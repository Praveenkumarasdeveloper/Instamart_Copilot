"""Run the complete Instamart assignment (Parts A-D) in sequence.

Place this file in the project root, alongside the src/ folder.
Run with: python run_project.py

This uses the existing Part A-D entry-point modules and preserves their
current notebook execution logic.
"""

from src.part_a import run as run_part_a
from src.part_b import run as run_part_b
from src.part_c import run as run_part_c
from src.part_d import run as run_part_d


def main():
    print("\\n========== PART A: DATA CLEANING AND SQL DATABASE ==========")
    run_part_a()

    print("\\n========== PART B: CUSTOMER SEGMENTATION AND LAPSE PREDICTION ==========")
    run_part_b()

    print("\\n========== PART C: SUPPORT TICKET TRIAGE ==========")
    run_part_c()

    print("\\n========== PART D: POLICY RAG AND REFUND AGENT ==========")
    run_part_d()

    print("\\n========== ALL PARTS A-D COMPLETED ==========")


if __name__ == "__main__":
    main()
