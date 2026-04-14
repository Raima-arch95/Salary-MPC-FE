# To launch: go to the root of the project
# and use this command : python3 -m data_team.Testsuite.main_testsuite
# this will launch all the testsuites at once

import unittest
from data_team.Testsuite import Testsuite_Prototype1


def main():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(Testsuite_Prototype1)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == "__main__":
    main()
