import unittest
from src.model import FakeNetModel

class TestFakeNetModel(unittest.TestCase):
    def test_prediction(self):
        model = FakeNetModel()
        result = model.predict(image_path="test_images/fake_image.jpg")
        self.assertIn(result, ["Real", "Fake"])

if __name__ == "__main__":
    unittest.main()
