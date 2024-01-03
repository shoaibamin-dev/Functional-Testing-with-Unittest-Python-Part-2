# Functional Testing with Unittest Python Part 2

This project extends the functional testing scenarios using the `unittest` framework in Python. It includes additional test cases for product and transaction insight functionalities.

## Project Structure

### Files and Directories

- **Files:**
  - `requirements.txt`: Requirements file listing necessary Python dependencies.
  - `test_product.py`: Test script for product-related scenarios.
  - `test_enrichtransaction.py`: Test script for enriching transaction scenarios.
  - `test_txninsight.py`: Test script for transaction insight scenarios.
  - `utils`: Directory containing utility modules.
  
- **Directories:**
  - `utils`: Subdirectory within `utils` containing utility modules.
    - `__init__.py`: Initialization file for the `utils` package.
    - `__pycache__`: Python cache directory for `utils`.
    - `configloader.py`: Module for loading configuration.
    - `mssqlutil.py`: Module for MSSQL database utilities.

## Usage

1. **Install Dependencies:**
   - Install the required Python dependencies using `pip install -r requirements.txt`.

2. **Test Execution:**
   - Run the tests using the command: `python -m unittest test_product.py test_enrichtransaction.py test_txninsight.py`.

## Test Scenarios

1. **Product Test (`test_product.py`):**
   - Validates product-related functionalities.

2. **Enrich Transaction Test (`test_enrichtransaction.py`):**
   - Tests the scenario of enriching transaction data.

3. **Transaction Insight Test (`test_txninsight.py`):**
   - Validates transaction insight scenarios.

## Configuration

- The project relies on a configuration file to set up environment-specific parameters. Ensure that the configuration is correctly set before running the tests.

## References

- [unittest Documentation](https://docs.python.org/3/library/unittest.html)

## Change History

- [Refer to the change history in the source code for detailed updates.](test_product.py)


