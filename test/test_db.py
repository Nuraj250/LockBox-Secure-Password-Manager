import unittest
from backend.db_handler import add_entry, get_entries, delete_entry

class TestDatabase(unittest.TestCase):
    """
    Unit tests for the database functions in db_handler.py
    """

    def test_add_entry(self):
        """
        Step 1: Test adding a password entry
        - Adds a sample entry ("example.com", "user123", "password123").
        - Retrieves all entries from the database.
        - Asserts that the database is not empty.
        """
        add_entry("example.com", "user123", "password123")  # Add a test entry
        entries = get_entries()  # Fetch all entries
        self.assertGreater(len(entries), 0)  # Ensure at least one entry exists

    def test_delete_entry(self):
        """
        Step 2: Test deleting a password entry
        - Fetches all stored entries.
        - If entries exist, deletes the first one.
        - Fetches entries again and ensures the list has changed.
        """
        entries = get_entries()  # Fetch all entries
        if entries:  # Ensure there's at least one entry to delete
            entry_id = entries[0][0]  # Get the first entry's ID
            delete_entry(entry_id)  # Delete the entry
            entries_after_delete = get_entries()  # Fetch entries again
            self.assertNotEqual(entries, entries_after_delete)  # Ensure the entry was removed

if __name__ == "__main__":
    unittest.main()
