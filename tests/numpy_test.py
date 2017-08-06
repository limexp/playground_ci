import numpy as np
import unittest

class BaseTestClass(unittest.TestCase):

    def test_1(self):
        np.testing.assert_array_equal([1.0,2.33333,np.nan],
                                      [np.exp(0),2.33333, np.nan])

    def test_2(self):
        np.testing.assert_array_equal([1.0,np.pi,np.nan],
                                      [1, np.sqrt(np.pi)**2, np.nan])                                           

    def test_3(self):
        np.testing.assert_array_almost_equal([1.0,np.pi,np.nan],
                                             [1, np.sqrt(np.pi)**2, np.nan])                                           
                                           
if __name__ == '__main__':
    unittest.main()
 
