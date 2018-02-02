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

        for k in known_answers:
            tree = parsexml.get_tree(k)
            test_data_generator = parsexml.extract_data(xmlns, tree)
            for elem in enumerate(test_data_generator):
                # test the sequentially outputted dictionaries.
                # the answer for a particular filename, k, is always a sequence of dictionaries in the same order
                # elem[0] is the enum portion of the tuple.
                # elem[1] is the generated dictionary from extract_data function being tested
                self.assertDictEqual(elem[1], known_answers[k][elem[0]])

    

if __name__ == '__main__':
    unittest.main()
