import unittest
from food import Food

class TestFood(unittest.TestCase):

    def setUp(self):
        self.food = Food()
    
    def test_init(self):
        self.assertEqual(self.food.shape(), "circle")
        self.assertEqual(self.food.shapesize(), (0.5, 0.5))
        self.assertEqual(self.food.color()[1], "blue")

    def test_refresh(self):
        old_pos = self.food.pos()
        self.food.refresh()
        new_pos = self.food.pos()
        self.assertNotEqual(old_pos, new_pos)

if __name__ == '__main__':
    unittest.main()