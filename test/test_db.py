import unittest
from backend.db_handler import add_entry, get_entries, delete_entry

class TestDatabase(unittest.TestCase):

    def test_add_entry(self):
        add_entry("example.com", "user123", "password123")
        entries = get_entries()
        self.assertGreater(len(entries), 0)

    def test_delete_entry(self):
        entries = get_entries()
        if entries:
            entry_id = entries[0][0]  # Get the first entry ID
            delete_entry(entry_id)
            entries_after_delete = get_entries()
            self.assertNotEqual(entries, entries_after_delete)

if __name__ == "__main__":
    unittest.main()
