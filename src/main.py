"""Run the completed Instamart project in assignment order (Parts A-D).

This executes the original notebooks, preserving their original calculations,
parameters, prompts, mock-LLM behaviour, and assignment logic.
"""
from src.part_a import run as run_part_a
from src.part_b import run as run_part_b
from src.part_c import run as run_part_c
from src.part_d import run as run_part_d

def main():
    print("\n######## PART A ########")
    run_part_a()
    print("\n######## PART B ########")
    run_part_b()
    print("\n######## PART C ########")
    run_part_c()
    print("\n######## PART D ########")
    run_part_d()
    print("\nAll notebook stages completed.")

if __name__ == "__main__":
    main()
