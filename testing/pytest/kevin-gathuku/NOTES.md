# Tutorial can be found [here](https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytes)

Pytest is great to use due to its
	
- Ease of use
- Ability to handle complex testing need

### Basic Pytest Usage

`test_capitalize.py`

Name files as test_ or _test.py

### Using Pytest Fixtures

`test_wallet.py`

- Wallet application enables adding and spending
- Will be modeled as a class with the instance methods
	- `spend_cash`
	- `add_cash`

### Refactoring our Tests with Fixtures

`test_wallet.py`

- Allow you to avoid the repetition when having to initialize the class in each test
- Set up helper code, to run before any test is executed
- Use `@pytest.fixture` decorator
- Fixtures as accepted by test functions as arguments

### Some Pointers on Test Fixtures

- Each test will receive a new instance of the class initialized in the fixture
- Use docstrings
- `pytest --fixtures` allows you to see all of them

### Parametrized Test Functions

- Testing various combinations of our methods
- Uses `@pytest.mark.parametrize`