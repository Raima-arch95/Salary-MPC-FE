import unittest
from ./../company/company_A/client.py as TS1 #Test Subject 1


class Test_Subject_1_Class(unittest.TestCase):
    
    def classic(self):
        self.assertEqual(TS1.get_aggregates("data.csv"),(165000,3))


    def wrong_path(self):
        self.assertRaises(TS1.get_aggregates("aaaaaaaaaaaaaaa"),"Error while fetching the file")

    def wrong_path_type(self):
        self.assertRaises(TS1.get_aggregates(25),"Wrong type submitted to the function gat_aggregates --  need string")

    
    
