import unittest
from unittest.mock import patch
from scoreboard import Scoreboard

class TestScoreboard(unittest.TestCase):

    def setUp(self):
        self.scoreboard = Scoreboard()
    
    def test_init(self):
        self.assertEqual(self.scoreboard.color(), "white")
        self.assertTrue(self.scoreboard.isvisible())
        self.assertEqual(self.scoreboard.xcor(), 0)
        self.assertEqual(self.scoreboard.ycor(), 270)
    
    @patch('scoreboard.open')
    def test_reset(self, mock_open):
        self.scoreboard.high_score = 10
        self.scoreboard.reset() 
        mock_open.assert_called_with("data.txt", "w")
    
    def test_increase_score(self):
        self.scoreboard.increase_score()
        self.assertEqual(self.scoreboard.score, 1)

if __name__ == '__main__':
    unittest.main()
