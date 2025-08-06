import unittest
from contact import Contact
class TestContact(unittest.TestCase):
    """Test class that defines the test cases for the contact behavior.
    Args:
        unittest (TestCase): TestCase class that helps in creating test cases.
    """
    def setUp(self):
        """Set up method to run before each test case."""
        self.new_contact = Contact("James", "muriuki","0712345678", "james@gmail.com")
    def test_init(self):
        """Test if the contact object is initialized correctly."""
        self.assertEqual(self.new_contact.first_name, "James")
        self.assertEqual(self.new_contact.last_name, "muriuki")
        self.assertEqual(self.new_contact.phone_number, "0712345678")
        self.assertEqual(self.new_contact.email, "james@gmail.com")
if __name__ == '__main__':
    unittest.main()