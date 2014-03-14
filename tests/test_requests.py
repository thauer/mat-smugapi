from .context import matsmug

import unittest
import requests

class RequestsTestSuite(unittest.TestCase):
    """Requests test cases."""

    def testRequestConnection(self):
        r = requests.get('https://github.com/timeline.json')
        self.assertEqual(r.status_code,200)

    def testRequestGet(self):
        r = requests.get('https://api.smugmug.com/services/api/json/1.3.0/')

if __name__ == '__main__':
    unittest.main()
