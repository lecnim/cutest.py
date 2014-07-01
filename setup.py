
from cutest import __version__
from distutils.core import setup

doc = '''

.. figure:: https://github.com/lecnim/cutest.py/raw/master/images/example.png
   :alt: Example terminal output

Simple test source file powered by docstrings:

.. code:: python

    import cutest as unittest

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

    if __name__ == "__main__":
        unittest.main()


Usage
-----

Import and use it just like ``unittest`` package:

.. code:: python

    import cutest as unittest


Or run and it will auto-discover available tests:

.. code:: bash

    $ python cutest.py

You can also test given file or package:

.. code:: bash

    $ python cutest.py my_test.py


Standard minimalistic mode
--------------------------


.. code:: bash

    $ python cutest.py

Output:

.. figure:: https://github.com/lecnim/cutest.py/raw/master/images/minimal_success.png
   :alt: Minimalistic mode



Verbose mode
------------

.. code:: bash

    $ python cutest.py -v

Output:

.. figure:: https://github.com/lecnim/cutest.py/raw/master/images/verbose_success.png
   :alt: Verbose mode


'''

setup(
    name='cutest.py',
    version=__version__,
    author='Lecnim',
    author_email='lecnim@gmail.com',
    py_modules=['cutest'],
    url='https://github.com/lecnim/cutest.py',
    license='LICENSE',
    description='The colorful and beautiful terminal output of python unittest.',
    long_description=doc,
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities'
    ]
)
