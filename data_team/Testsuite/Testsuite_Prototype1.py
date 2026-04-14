import unittest
from data_team.company.company_A import client as TS1 #Test Subject 1

PATH= "data_team/company/company_A/data.csv"

class Test_Subject_1_Class(unittest.TestCase):
    def test_classic(self):
        self.assertEqual(TS1.get_aggregates(PATH),(165000,3))

    
    def test_wrong_path(self):
        with self.assertRaises(ValueError) as context:
            TS1.get_aggregates("aaaaaaaaaaaaaaa")

        self.assertEqual(str(context.exception), "Error while fetching the file")


    def test_wrong_path_type(self):
        with self.assertRaises(ValueError) as context:
            TS1.get_aggregates(25)

        self.assertEqual( str(context.exception),"Wrong type submitted to the function gat_aggregates --  need string")
     
    

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
