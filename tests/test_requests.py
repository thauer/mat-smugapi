from .context import matsmug

import unittest
import requests

class RequestsTestSuite(unittest.TestCase):
    """Requests test cases."""

    def testRequestSimpleGet(self):
        r = requests.get('https://github.com/timeline.json')
        print r.text
        assert True

if __name__ == '__main__':
    unittest.main()