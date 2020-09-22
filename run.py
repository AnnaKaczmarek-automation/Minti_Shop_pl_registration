import unittest
from tests.registration_test import Test_registration




# Pobierz testy, które chcesz uruchomić
registration_test = unittest.TestLoader().loadTestsFromTestCase(Test_registration)

# Stwórz Test Suita łączac testy
test_suite = unittest.TestSuite([registration_test])

# odpal
unittest.TextTestRunner(verbosity=2).run(test_suite)
