import unittest
import to_do_list

class TestToDoList(unittest.TestCase):

    def setUp(self):
        # Clear the task list before each test
        to_do_list.tasks.clear()

    def test_add_valid_task(self):
        result = to_do_list.add_task("Buy groceries")
        self.assertTrue(result)
        self.assertEqual(to_do_list.tasks, ["Buy groceries"])

    def test_add_invalid_task(self):
        result = to_do_list.add_task("")
        self.assertFalse(result)
        self.assertEqual(to_do_list.tasks, [])

    def test_delete_existing_task(self):
        to_do_list.add_task("Read book")
        result = to_do_list.delete_task(0)
        self.assertTrue(result)
        self.assertEqual(to_do_list.tasks, [])

    def test_delete_invalid_index(self):
        result = to_do_list.delete_task(10)
        self.assertFalse(result)

    def test_list_tasks(self):
        to_do_list.add_task("Call mom")
        to_do_list.add_task("Do homework")
        self.assertEqual(to_do_list.list_tasks(), ["Call mom", "Do homework"])

if __name__ == '__main__':
    unittest.main()
