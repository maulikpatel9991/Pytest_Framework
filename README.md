# Pytest_Framework
# Pre-requisite

- Before running the Pytest code, you need to install the required dependencies and packages.
- I have used the command `pip freeze > requirements.txt` to list down all the packages that were used for this proof of
  concept.
- Make sure you have created the virtual environment in project directory to install the python packages
  i.e., `python3 -m venv demoenv`
- Activate the newly created environment using the command: `env\Scripts\activate`
- To install all the required packages, you can use the command `pip install -r requirements.txt`

# Steps to run the pytest

- Make sure you run the command in terminal, and you are in project root directory. here it's a `demo`
- To run all the tests execute the command: `pytest`
- To run the specific test file use the command: `pytest -k "test_unit"`
- To run the specific test use the command: `pytest -k "test_page_title"`

# Steps to check the generated report

- Report will be generated in the `Report` directory that is located at the root directory. i.e., `maulik_demo\Report`
