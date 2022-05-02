from models import Articles
import unittest

class TestArticles(unittest.TestCase):
    def setUp(self):
        self.new_article = Articles('Zulu','BikoZulu','Drunk','Heeeeeh heeeeh heeeeh heeeeeh','www.bikozulu.co.ke','https://cdn.cnn.com/cnnnext/dam/assets/220308152825-thomas-siderio-super-tease.jpg','2022-05-02T17:51:00Z')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

if __name__ == "__main__":
    unittest.main()