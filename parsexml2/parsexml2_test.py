import unittest
import parsexml
import xml.etree.ElementTree as etree


class Test_parsexml2_test(unittest.TestCase):
    def test_get_tree_class_is_correct(self):
        """ This test tests the get_tree module to make sure
        it returns the correct class, which should be a 
        etree.ElementTree
        """
        filename = r'C:\Users\perm7158\Documents\Visual Studio 2017\Projects\parsexml2\parsexml2\test\Term Conversion - Anonimized Test Data.xml'

        self.assertIsInstance(parsexml.get_tree(filename), etree.ElementTree)
        
    def test_extract_data(self):
        """ Confirm the extract data function grabs what is expected
        """
        known_answers = {r'C:\Users\perm7158\Documents\Visual Studio 2017\Projects\parsexml2\parsexml2\test\Term Conversion - Anonimized Test Data.xml': 
                         [{'insured': 'Alice P Client', 'payer': 'John Q Client', 'owner': 'John Q Client', 'final conversion year': '2049'},
                          {'insured': 'Susan A Sample', 'payer': 'Susan A Sample', 'owner': 'Susan A Sample', 'final conversion year': '2031'},
                          {'insured': 'Dillon B Tester', 'payer': 'Dillon B Tester', 'owner': 'Dillon B Tester', 'final conversion year': '2029'},
                          {'insured': 'Hannah P Example', 'payer': 'Hannah P Example', 'owner': 'Hannah P Example', 'final conversion year': '2039'},
                          {'insured': 'Andrew R Sameling', 'payer': 'Gretchen Sameling', 'owner': 'Andrew R Sameling', 'final conversion year': '2028'},
                         ]
                        }
        xmlns = "_x007B_04D313F1-5010-E511-80D0-005056866F29_x007D_"
        tree = parsexml.get_tree(k)

        for k in known_answers:
            tree = parsexml.get_tree(k)
            self.assertDictEqual(parsexml.extract_data(xmlnm, tree), known_answers[k])

    

if __name__ == '__main__':
    unittest.main()
