import data_access
import unittest
import pandas as pd

# Sample DataFrame for testing
data = {
    'Name': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve'],
    'Age': [28, 32, 25, 29, 40],
    'Occupation': ['Engineer', 'Doctor', 'Artist', 'Lawyer', 'Manager'],
    'Salary': [70000, 95000, 50000, 85000, 90000]
}
df = pd.read_csv("data.csv", index_col=0)

class TestPandasMethods(unittest.TestCase):

    def test_age(self):
        expected_output = pd.Series([28, 32, 25, 29, 40], name="Age", index = data["Name"])
        expected_output.index.name = "Name"
        result = data_access.get_age(df)
        pd.testing.assert_series_equal(result, expected_output)

    def test_salary_occupation(self):
        test_data = {'Salary': [70000, 95000, 50000, 85000, 90000],
                'Occupation': ['Engineer', 'Doctor', 'Artist', 'Lawyer', 'Manager']}
        expected_output = pd.DataFrame(test_data, index = data["Name"])
        expected_output.index.name = "Name"
        result = data_access.get_salary_and_occupation(df)
        pd.testing.assert_frame_equal(result, expected_output, 
        check_dtype=False, check_exact=True)

    def test_third_individual(self):
        data = {'Age': 25,
                'Occupation': 'Artist',
                'Salary': 50000}
        expected_output = pd.Series(data)
        expected_output.name = "Carol"
        
        result = data_access.get_third_name(df)
        pd.testing.assert_series_equal(result, expected_output)

    def test_age_salary_first_two(self):
        data = {'Age': [28, 32],
                'Salary': [70000, 95000]}
        expected_output = pd.DataFrame(data, index = ["Alice", "Bob"])
        expected_output.index.name = "Name"
        result = data_access.get_age_salary_of_first_two(df)
        pd.testing.assert_frame_equal(result, expected_output)

    def test_details_carol(self):
        data = {'Age': 25,
                'Occupation': 'Artist',
                'Salary': 50000}
        expected_output = pd.Series(data)
        expected_output.name = "Carol"
        result = data_access.get_carol_deets(df)
        pd.testing.assert_series_equal(result, expected_output)

    def test_occupation_bob_eve(self):
        expected_output = pd.Series(['Doctor', 'Manager'], name="Occupation", index = ["Bob","Eve"])
        expected_output.index.name = "Name"
        result = data_access.get_occupation_bob_eve(df)
        pd.testing.assert_series_equal(result, expected_output)

# If running this script directly, it will execute all the tests
if __name__ == '__main__':
    unittest.main()
