import unittest


class TestMain(unittest.TestCase):
    """ Test sat-util generic parser class """

    def parse(self, args='', search=False, download=False, process=False):
        parser = SatParser()
        if search:
            parser.add_search()
        if download:
            parser.add_download()
        if process:
            parser.add_process()
        return parser.parse_args(args.split())
