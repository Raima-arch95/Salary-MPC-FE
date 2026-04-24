# To launch: go to the root of the project
# and use this command : python3 -m tests.Testsuite.main_testsuite
# this will launch all the testsuites at once

import unittest
from tests.Testsuite import test_suite_Prototype1


def main():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_suite_Prototype1)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == "__main__":
    main()
