## Beginning Test-Driven Development in Python

The tutorial can be found [here](https://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137)

- Is the process of baking your tests into everyday coding instead of doing it all after
- It's intended to improve the quality of your code
- Also, provides clarity and focus on the functionality you're trying to achieve

### What is Test-Driven Development?

- The process of implementing code by writing tests first, watching them fail and then writing the code to make the test pass
- You can build on the functionality by altering the tests to achieve the expected outcome and repeating the process
- It is as much a mental model as a practical one, since the process of writing the tests helps to understand the problem before you begin writing the code to solve it
- You will think about what's being returned, or the potential errors etc...
- By doing this, you will consider the different routes to get to each piece of code, and better map out all of the different flows of the program

- The process
	1. Write a **failing** test
	2. Make the unit test **pass**
	3. **Refactor**

### Agile Development With Test-Driven Development

- The incremental update nature draws parallels with agile development
- Focus on quality not quantity

### Syntax - Main methods

- `assert`
- `assertEqual(a, b)`
- `assertNotEqual(a, b)`
- `assertIn(a, b)`
- `assertNotIn(a, b)`
- `assertFalse(a)`
- `assertTrue(a)
- `assertIsInstance(a, TYPE)
- `assertRaises(ERROR, a, args)

### Installing and Using Python's Nose

- `nosetest` is a test runner
- The only standard to follow, is to begin each test method with `test_`

### Nose options

- `-v` provides more verbose output
- `-s` or `-nocapture` shows output of print statements, good for debugging
- `--nologcapture` allows logging information output
- `--rednose` provides colored output for tests
- `--tags=TAGS` gives the option of executing tagged tests rather than the entire suite, uses `@TAG` above the test method

### Example Problem: Calculator Class

- Adding `__init__.py` files in folders will make that director a module, and allow its code to be imported across the directory structure
- Utilize classes to contain different test cases
- Use methods to test cases, prefixed with `test_`
- `unittest` has a standard runner, which allows it to be run via the standard script running procedure i.e `python script_name.py`. Just add the following to the bottom of the script

``` python
if __name__ == '__main__':
	unittest.main()
```

- Here, we will use `nosetests` runner, which has added features

- You can't **just** test for the case that you're interested in, but handle all (or the majority of) **potential** outcomes

- Using the `setUp()` method, allows you to put things in place before each test case, such as object instantiation
