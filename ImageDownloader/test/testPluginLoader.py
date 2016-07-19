import unittest
from plugins.loader.PluginLoader import PluginLoader
class TestPluginLoader(unittest.TestCase):
    def test_A(self):
        model  = PluginLoader()
        print model.Plugins()
if __name__ == '__main__':
    unittest.main()
