# About Tests

- The tests are located in the `tests/` directory.
- Each test file corresponds to a specific module or functionality.
- There are two types of tests: experiments tests (using plain python with no framework) and tests using pytest framework.

### Running Tests
- You can run all pytest tests using this command:
  ```
  pytest tests/pylint
  ```
- Also to run experiments tests, you can execute the scripts directly using Python:
  ```
  python -m tests.experiments.test_example
  ```