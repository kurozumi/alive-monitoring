import unittest
import requests
import os

class Monitoring(unittest.TestCase):

    def setUp(self):
        self.url = os.environ['SITE_URL']

    def test(self):
        r = requests.get(self.url, allow_redirects=False)
        assert 200 == r.status_code, "{0} {1}".format(r.status_code, r.reason)

if __name__ == "__main__":
    unittest.main()