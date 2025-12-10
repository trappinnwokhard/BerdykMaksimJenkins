import unittest
from library_system import LibraryManager 

class TestLibrarySystem(unittest.TestCase):
    
    def setUp(self):
        self.lib = LibraryManager()
        self.book1 = self.lib.add_book("Кобзар", "Т. Шевченко")

    def test_add_book(self):
        self.assertEqual(len(self.lib.books), 1)
        self.assertEqual(self.lib.books[1].title, "Кобзар")

    def test_get_book(self):
        book = self.lib.get_book(1)
        self.assertIsNotNone(book)
        self.assertEqual(book.author, "Т. Шевченко")
        
        missing = self.lib.get_book(999)
        self.assertIsNone(missing)

    def test_update_book_info(self):
        updated_book = self.lib.update_book_info(1, new_title="Кобзар (Видання 2)")
        self.assertEqual(updated_book.title, "Кобзар (Видання 2)")
        self.assertEqual(self.lib.get_book(1).title, "Кобзар (Видання 2)")

    def test_borrow_and_return_flow(self):
        result = self.lib.borrow_book(1)
        self.assertTrue(result)
        self.assertTrue(self.lib.get_book(1).is_borrowed)

        result_retry = self.lib.borrow_book(1)
        self.assertFalse(result_retry)

        result_return = self.lib.return_book(1)
        self.assertTrue(result_return)
        self.assertFalse(self.lib.get_book(1).is_borrowed)

    def test_delete_book(self):
        result = self.lib.delete_book(1)
        self.assertTrue(result)
        self.assertIsNone(self.lib.get_book(1))

        result_fail = self.lib.delete_book(999)
        self.assertFalse(result_fail)

if __name__ == '__main__':
    unittest.main()