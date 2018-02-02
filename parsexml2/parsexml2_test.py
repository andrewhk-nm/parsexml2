import unittest
import parsexml
import xml.etree.ElementTree as etree


class Test_parsexml2_test(unittest.TestCase):
    def test_A(self):
        self.fail("Not implemented")

    def test_get_root_class_is_correct(self):
        """ This test tests the get_root module to make sure
        it returns the correct class, which should be a 
        etree.Element
        """
        # I don't really know how to test this....
        filename = r'C:\Users\perm7158\Documents\Visual Studio 2017\Projects\parsexml2\parsexml2\test\Term Conversion - Anonimized Test Data.xml'

        self.assertIsInstance(parsexml.get_root(filename), etree.Element)
        
        
    

if __name__ == '__main__':
    unittest.main()
