import unittest
import logging


# Available test results:

class Results(unittest.TestCase):
    """Test results"""

    def test_success(self):
        """success"""

    def test_fail(self):
        """fail"""
        self.assertTrue(False)

    def test_error(self):
        """error"""
        1 / 0

    @unittest.expectedFailure
    def test_expected(self):
        """expected error"""
        self.assertTrue(False)

    @unittest.expectedFailure
    def test_unexpected(self):
        """unexpected success"""
        self.assertTrue(True)

    @unittest.skip("it won't work")
    def test_skipped_reason(self):
        """skipped"""


# Test without docstrings:

class NoDoc(unittest.TestCase):
    def test_no_method_doc(self):
        self.assertTrue(0)
    def test(self):
        1 / 0


# Logging catching:

class Logging(unittest.TestCase):
    """Logging"""

    def test(self):
        """catch messages"""
        logging.basicConfig(level=logging.DEBUG)
        logging.debug('debug')
        logging.info('info')
        logging.warning('warning')
        logging.error('error')
        logging.critical('critical!')


# has, can, should, shouldn't:

class CoffeMachine(unittest.TestCase):
    """A good coffee machine"""

    def test_success(self):
        """should makes hot drinks"""

class Dog(unittest.TestCase):
    """A typical dog"""

    def test_barking(self):
        """should barks loudly"""
    def test_tail(self):
        """has a tail"""
        self.assertTrue(False)

class Cat(unittest.TestCase):
    """A typical cat"""

    def test_meow(self):
        """can meow"""
        print('an onomatopoeia for the voiced sound')
    def test_fur(self):
        """has a fur"""

if __name__ == '__main__':
    unittest.main()
