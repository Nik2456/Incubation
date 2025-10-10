def calculate_pass_rate(results):

    if not results:
        print("No test results provided.")
        return

    total_tests = len(results)
    passed_tests = sum(results)
    pass_rate = (passed_tests / total_tests) * 100

    print(f"Pass Rate: {pass_rate:.2f}%")


test_results = [True, False, True, True, True]
calculate_pass_rate(test_results)
