# cutest.py

The colorful and beautiful terminal output of python unittest, inspired by [Vows](http://vowsjs.org/)!

![Example terminal output](images/example.png)

Simple test source file powered by docstrings:

```python
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
```

## Installation

Supported python versions:

    3.2
    3.3
    3.4

Use pip to install...

    $ pip install cutest.py
    
...or download a [`cutest.py`](https://github.com/lecnim/cutest.py/releases/download/v0.9.0/cutest.py) script and it is ready to work. No requirements!

## Usage

Import and use it just like `unittest` package:

    import cutest as unittest

Or run and it will auto-discover available tests:

    $ python cutest.py

You can also test given file or package:

    $ python cutest.py my_test.py

## Verbose and minimal mode

Standard minimalistic mode:

    $ python cutest.py

![Minimalistic mode](images/minimal_success.png)

Verbose mode:

    $ python cutest.py -v

![Verbose mode](images/verbose_success.png)
