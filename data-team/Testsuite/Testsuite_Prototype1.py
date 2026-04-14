import unittest
from ./../company/company_A/client.py as TS1 #Test Subject 1


class Test_Subject_1_Class(unittest.TestCase):
    
    def classic(self):
        self.assertEqual(TS1.get_aggregates("data.csv"),(165000,3))


    def wrong_path(self):
        self.assertRaises(TS1.get_aggregates("aaaaaaaaaaaaaaa"),"Error while fetching the file")

    def wrong_path_type(self):
        self.assertRaises(TS1.get_aggregates(25),"Wrong type submitted to the function gat_aggregates --  need string")

    
    
def suite():
    test_suite = unittest.TestSuite()
    # Add all tests from a specific class
    test_suite.addTest(unittest.makeSuite(Test_Subject_1_Class))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
