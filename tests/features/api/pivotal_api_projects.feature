@api @project
Feature: API Project
	As an application developer,
	I want to manage pivotal Projects through REST API,
	So that my app can get answers and show them.

	@tc_41 @functional @fixture_create_project @fixture_delete_project
	Scenario: Get a Project
		When the "GET" request to "/projects/<Project.id>" is sent
		Then the response status code should be 200
		And the response body should be verified with:
			| key | value        |
			| id  | <Project.id> |

	@tc_40 @functional @fixture_create_project @fixture_delete_project
	Scenario: Update a Project
		Given the following body parameters:
			| key  | value               |
			| name | AUTO_UPDATE_PROJECT |
		When the "PUT" request to "/projects/<Project.id>" is sent
		Then the response status code should be 200
		And the response body should be verified with:
			| key  | value               |
			| id   | <Project.id>        |
			| name | AUTO_UPDATE_PROJECT |

	@functional @tc_44 @fixture_create_project
	Scenario: Delete an Project
		When the "DELETE" request to "/projects/<Project.id>" is sent
		Then the response status code should be 204

	@functional @tc_43 @fixture_delete_project
	Scenario: Create an Project
		Given the following body parameters:
			| key  | value            |
			| name | AUTO_NEW_PROJECT |
		When the "POST" request to "/projects" is sent
		Then the response status code should be 200
		And the response body should be verified with:
			| key  | value          |
			| name | <Project.name> |
			| id   | <Project.id>   |

	@negative @tc_45
	Scenario: Error when create a project with initial velocity up to 999
		Given the following body parameters:
			| key              | value            |
			| name             | AUTO_NEW_PROJECT |
			| initial_velocity | 9999             |
		When the "POST" request to "/projects" is sent
		Then the response status code should be 400
		And the response body should be verified with:
			| key  | value          |
			| code | <project.code> |
			| kind | <project.kind> |