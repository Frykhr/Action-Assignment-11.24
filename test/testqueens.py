import unittest
from src.eight_queens import solve_queens

class TestEightQueens(unittest.TestCase):
    
    def test_queens_valid(self):
        # 测试 solve_queens 函数是否返回正确的解决方案数量
        self.assertEqual(solve_queens(8, 4, 3), 12, "Should be 12 solutions")

if __name__ == '__main__':
    unittest.main()
