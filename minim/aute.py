# Define a dictionary to store test results
test_results = {
    'test1': 'pass',
    'test2': 'fail',
    'test3': 'pass'
}

# Function to display test results
def display_test_results(results):
    for test, result in results.items():
        print(f"{test}: {result}")

# Call the function to display the results
display_test_results(test_results)
