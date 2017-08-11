## Python Unit Testing Tutorial

### unittest - Automated testing framework

- Also referred to as `PyUnit`
- Supports
	- fixtures
	- test suites
	- a test runner

### Basic Test Structure

`test_structure.py`

- Tests have two parts
	1. Code to manage `fixtures`
	2. The test itself
- Created by subclassing `TestCase` and overriding or adding methods
- Using `if __name__ == '__main__` is the easiest way to run unittest tests
- If you want more detail use `-v` when running the test

### Test Outcomes

`test_outcomes.py`

1. `ok`
2. `FAIL`
3. `ERROR`

- Raises an `Exception` **not** an `Error`
- Tests don't necessarily `pass`, they depend on the whether or not an `Exception` is raised

- In the `test_outcome` file, the `test_fail()` fails, which produced a `traceback`
- This shows the line where the code failed
- `assert*()` takes a `msg` as a parameter, which can be used to display a more detailed error message
	- Shown here `assertTrue(False, 'failure message goes here')`

### Asserting Truth

- Most tests are checking for some sort of condition to evaluate to either `True` or `False`
- unittest comes with `assertTrue` and `assertFalse` methods to check for this

### List Of Assertions

- `assertTrue`
- `assertFalse`
- `assertIsNone`
- `assertIsNotNone`
- `assertEqual`
- `assertNotEqual`
- `assertIs`
- `assertIsNot`
- `assertIn`
- `assertNotIn`
- `assertIsInstance`
- `assertNotIsInstance`

- `assertAlmostEqual`
- `assertNotAlmostEqual`
- `assertGreater`
- `assertGreaterEqual`
- `assertLess`
- `assertLessEqual`
- `assertRegex`
- `assertNotRegex`
- `assertCountEqual`
- `assertMultiLineEqual`
- `assertSequenceEqual`
- `assertListEqual`
- `assertTupleEqual`
- `assertSetEqual`
- `assertDictEqual`

### Failure Messages

- The failure messages for `assertEqual` and `assertNotEqual` display the values being compared in the failure message.

### Testing for Exceptions (and Warnings)

- The `TestCase` class gives us methods to check for expected `Exceotions`
	- `assertRaises(exception)`
	- `assertRaisesRexex(exception, regexp)`
	- `assertWarns(warn, fun, *args, **kwargs)`
	- `assertWarnsRegex(warn, fun, *args, **kwargs)`

- These are useful, when you wish to check that `Exceptions` are triggered properly

### Test Fixtures

- These are resources needed by a test
- Useful when writing tests for the same class, in which they all need an instance
- Other fixtures include
	- Database connections
	- Temporary files
- Involves the use of `setUp()` and `tearDown()`
