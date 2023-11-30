import pytest
from src.eight_queens import solve_queens

def test_queens():
    assert solve_queens(8, 4, 3) == 12
    # assert eight_queens.solve_queens(8, 5, 5) == 2
    # assert eight_queens.solve_queens(8, 1, 1) == 1
