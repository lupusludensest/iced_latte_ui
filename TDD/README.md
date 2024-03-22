# run all tests refactored
pytest --alluredir=allure_reports_refactored -k "test_refactored_1.py or test_refactored_2.py or test_refactored_3.py or test_refactored_4.py or test_refactored_5.py"

# allure report
allure serve allure_reports_refactored