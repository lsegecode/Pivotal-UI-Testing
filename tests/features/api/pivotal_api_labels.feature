@api @label
Feature: API Label
	As an application developer,
	I want to query the Label of the Pivotal API,
	So that my app can consume those responses.

	@functional @tc_48 @fixture_create_project @fixture_delete_project
	Scenario: Post a Label
		Given the following body parameters:
			| key  | value           |
			| name | AUTO_TEST_LABEL |
		When the "POST" request to "/projects/<project.id>/labels" is sent
		Then the response status code should be 200
		And the response body should be verified with:
			| key  | value           |
			| id   | <label.id>      |
			| name | AUTO_TEST_LABEL |

	@tc_47 @functional @fixture_create_project @fixture_create_label @fixture_delete_project
	Scenario: Get a Label
		When the "GET" request to "/projects/<project.id>/labels/<label.id>" is sent
		Then the response status code should be 200
		And the response body should be verified with:
			| key        | value        |
			| id         | <Label.id>   |
			| project_id | <Project.id> |

	@tc_49 @functional @fixture_create_project @fixture_create_label @fixture_delete_project
	Scenario: Update a Label
		Given the following body parameters:
			| key  | value             |
			| name | AUTO_UPDATE_LABEL |
		When the "PUT" request to "/projects/<project.id>/labels/<label.id>" is sent
		Then the response status code should be 200
		And the response body should be verified with:
			| key  | value                 |
			| id   | <Project.id>          |
			| name | NEW_AUTO_UPDATE_LABEL |

	@functional @tc_50 @fixture_create_project @fixture_create_label @fixture_delete_project
	Scenario: Delete a Label
		When the "DELETE" request to "/projects/<project.id>/labels/<label.id>" is sent
		Then the response status code should be 204
