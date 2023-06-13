@api @epic
Feature: API Epic
	As an application developer,
	I want to manage pivotal Epics through REST API,
	So that my app can get answers and show them.

	@tc_36 @functional @fixture_create_project @fixture_delete_project
	Scenario: Get all Epic
		When the "GET" request to "/projects/<project.id>/epics" is sent
		Then the response status code should be 200
		And the response body should be verified with:
			| key | value        |
			| id  | <project.id> |

	@tc_35 @functional @fixture_create_project @fixture_delete_project
	Scenario: Create an Epic
		Given the following body parameters:
			| key  | value         |
			| name | AUTO_NEW_EPIC |
		When the "POST" request to "/projects/<project.id>/epics" is sent
		Then the response status code should be 200
		And the response body should be verified with:
			| key  | value         |
			| id   | <epic.id>     |
			| name | AUTO_NEW_EPIC |

	@tc_37 @functional @fixture_create_project @fixture_create_epic @fixture_delete_project
	Scenario: Get an Epic
		When the "GET" request to "/projects/<project.id>/epics/<epic.id>" is sent
		Then the response status code should be 200
		And the response body should be verified with:
			| key        | value        |
			| id         | <epic.id>    |
			| project_id | <project.id> |

	@tc_38 @functional @fixture_create_project @fixture_create_epic @fixture_delete_project
	Scenario: Update a Epic
		Given the following body parameters:
			| key  | value            |
			| name | AUTO_UPDATE_EPIC |
		When the "PUT" request to "/projects/<project.id>/epics/<epic.id>" is sent
		Then the response status code should be 200
		And the response body should be verified with:
			| key  | value            |
			| id   | <epic.id>        |
			| name | AUTO_UPDATE_EPIC |

	@tc_39 @functional @fixture_create_project @fixture_create_epic @fixture_delete_project
	Scenario: Delete an Epic
		When the "DELETE" request to "/projects/<project.id>/epics/<epic.id>" is sent
		Then the response status code should be 204
