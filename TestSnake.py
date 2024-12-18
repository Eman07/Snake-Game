import unittest 
from unittest.mock import patch
from snake import Snake
from food import Food
from scoreboard import Scoreboard

class TestSnake(unittest.TestCase):

    def setUp(self):
        self.snake = Snake()
        
    @patch('snake.Turtle.goto')  
    def test_move(self, mock_goto):
        self.snake.move() 
        mock_goto.assert_called()
        
    def test_add_segment(self):
        initial_length = len(self.snake.segments)
        self.snake.add_segment((0,0))  
        self.assertEqual(len(self.snake.segments), initial_length + 1)

class TestFood(unittest.TestCase):

    @patch('random.randint')
    def test_refresh(self, mock_randint):
        food = Food()
        food.refresh()        
        mock_randint.assert_called()  

class TestScoreboard(unittest.TestCase):

    def setUp(self):
        self.scoreboard = Scoreboard()
        
    def test_increase_score(self):
        self.scoreboard.increase_score()
        self.assertEqual(self.scoreboard.score, 1)
        
if __name__ == '__main__':
    unittest.main()