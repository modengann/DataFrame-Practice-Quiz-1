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
df = pd.DataFrame(data)

class TestPandasMethods(unittest.TestCase):

    def test_print_age(self):
        expected_output = pd.Series([28, 32, 25, 29, 40], name="Age")
        result = data_access.get_age(df)
        pd.testing.assert_series_equal(result, expected_output)

    def test_print_name_occupation(self):
        data = {'Name': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve'],
                'Occupation': ['Engineer', 'Doctor', 'Artist', 'Lawyer', 'Manager']}
        expected_output = pd.DataFrame(data)
        result = data_access.get_name_and_occupation(df)
        pd.testing.assert_frame_equal(result, expected_output)

    def test_print_third_individual(self):
        data = {'Name': ['Carol'],
                'Age': [25],
                'Occupation': ['Artist'],
                'Salary': [50000]}
        expected_output = pd.Series(data, name=2)
        result = data_access.get_third_name(df)
        pd.testing.assert_series_equal(result, expected_output)

    def test_print_age_salary_first_two(self):
        data = {'Age': [28, 32],
                'Salary': [70000, 95000]}
        expected_output = pd.DataFrame(data)
        result = data_access.age_salary_of_first_two(df)
        pd.testing.assert_frame_equal(result, expected_output)

    def test_print_details_carol(self):
        data = {'Name': ['Carol'],
                'Age': [25],
                'Occupation': ['Artist'],
                'Salary': [50000]}
        expected_output = pd.DataFrame(data)
        result = data_access.carol_deets(df)
        pd.testing.assert_frame_equal(result, expected_output)

    def test_print_occupation_bob_eve(self):
        expected_output = pd.Series(['Doctor', 'Manager'], name="Occupation")
        result = data_access.occupation_bob_eve(df)
        pd.testing.assert_series_equal(result, expected_output)

# If running this script directly, it will execute all the tests
if __name__ == '__main__':
    unittest.main()
