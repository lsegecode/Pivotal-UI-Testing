DEATULT_TAGS=api
TAGS="$(DEATULT_TAGS)"
REPORT_FILE=./reports/cucumber_report.json
ENV="develop"
BROWSER="CHROME"
REMOTE_BROWSER="CHROME"

DEFAULT_CONFIG_JSON=.configuration.json
CONFIG_JSON="${DEFAULT_CONFIG_JSON}"
DEFAULT_ENVIRONMENT_JSON=.environment.json
ENVIRONMENT_JSON="${DEFAULT_ENVIRONMENT_JSON}"


setup:
	@echo "Settin up"
	@echo "Installing PIPENV package..."
	python -m pip install pipenv
	@echo "Activating virtualenv"
	pipenv shell
	@echo "Installing dependencies..."
	pipenv install -d
	@echo "Setup cucumber-html-reporter"
	pipenv run npm install cucumber-html-reporter --save-dev 
	@echo "Setup Done!"

static_code_analysis:
	@echo "Static Code analysis"
	pipenv run pylint main/
	pipenv run pylint tests/
	pipenv run flake8 main/ --benchmark
	pipenv run flake8 tests/ --benchmark
	pipenv run pycodestyle main/ --benchmark
	pipenv run pycodestyle tests/ --benchmark

test:
	@echo "Executing testing scenarios with TAGS: $(TAGS)"
	@echo "Report file: $(REPORT_FILE)"
	pipenv run pytest --cache-clear --cucumber-json="$(REPORT_FILE)" -vsm "$(TAGS)"
	@echo "Finished testing."

report:
	@echo "Generating html report"
	pipenv run node cucumberReportGenerator.js