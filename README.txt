1) To generate Allure reports have allure-pytest package installed  run pip install allure-pytest command
Next, download the latest allure package zip file from the allure-framework GitHub repo  https://github.com/allure-framework/allure2/releases
a) Unzip the downloaded zip file
b) Copy the path till bin
c) Add it to the path environment variable

To create allure report   run   pytest --alluredir=allure-report/ command
Once test execution completes, all the test results would get stored in allure-report directory.

To view the allure-report in the browser run   allure serve allure-report/ command
This will open up the report in your default browser automatically

2) To generate pytest html reports have pytest-html plugin installed    run   pip install pytest-html  command
Next, run pytest --html=report.html command

This will generate html reports, which you can open in your preferred browser
