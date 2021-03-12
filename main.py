import unittest
import requests

class Monitoring(unittest.TestCase):

    def setUp(self):
        self.url = "https://v4.eccube-plugin.net"

    def test(self):
        r = requests.get(self.url, allow_redirects=False)
        assert 200 == r.status_code, "{0} {1}".format(r.status_code, r.reason)

if __name__ == "__main__":
    unittest.main()