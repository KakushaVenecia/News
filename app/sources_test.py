from models import Sources
import unittest

class TestSources(unittest.TestCase):
    """
    SourcesTest class to test the behaviour of the Sources class
    """
    def setUp(self):
        """
        Method that runs before each other test runs
        """
        self.new_source = Sources('al-jazeera-english','Al Jazeera English','News, analysis from the Middle East and worldwide, multimedia and interactives, opinions, documentaries, podcasts, long reads and broadcast schedule.',
         'http://www.aljazeera.com', 'general', 'us', 'en')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

if __name__ == "__main__":
    unittest.main()