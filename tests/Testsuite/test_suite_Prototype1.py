import unittest
import os
from companies.company_A import client as TS1 #Test Subject 1

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

PATH = os.path.join(
    ROOT_DIR,
    "companies",
    "company_B",
    "data.csv"
)

class Test_Subject_1_Class(unittest.TestCase):
    def test_classic(self):
        self.assertEqual(TS1.get_aggregates(PATH),(192000.17, 3))

    
    def test_wrong_path(self):
        with self.assertRaises(ValueError) as context:
            TS1.get_aggregates("aaaaaaaaaaaaaaa")

        self.assertEqual(str(context.exception), "Error while fetching the file")


    def test_wrong_path_type(self):
        with self.assertRaises(ValueError) as context:
            TS1.get_aggregates(25)

        self.assertEqual( str(context.exception),"Wrong type submitted to the function gat_aggregates --  need string")
     
    

if __name__ == '__main__':
    unittest.main(verbosity=2)