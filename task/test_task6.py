import unittest
import sys

class TestExample(unittest.TestCase):

    @unittest.skipIf(sys.platform.startswith("win"), "Test skipped on Windows")
    def test_not_on_windows(self):
        self.assertTrue(True)

    @unittest.skipUnless(sys.version_info >= (3, 10), "Requires Python 3.10 or higher")
    def test_python_version(self):
        self.assertTrue(True)

    def test_always_runs(self):
        self.assertEqual(1 + 1, 2)

if __name__ == "__main__":
    unittest.main()
