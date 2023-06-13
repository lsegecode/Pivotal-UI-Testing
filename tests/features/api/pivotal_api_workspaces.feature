@api @workspace
Feature: API Workspace
	As an application developer,
	I want to manage pivotal Workspaces through REST API,
	So that my app can get answers and show them.

	@functional @tc_25 @fixture_create_workspace @fixture_delete_workspace
	Scenario: Get an Workspace
		When the "GET" request to "/my/workspaces/<Workspace.id>" is sent
		Then the response status code should be 200
		And the response body should be verified with:
			| key | value          |
			| id  | <Workspace.id> |

	@functional @tc_24 @fixture_delete_workspace
	Scenario: Create an Workspace
		Given the following body parameters:
			| key  | value              |
			| name | AUTO_NEW_WORKSPACE |
		When the "POST" request to "/my/workspaces" is sent
		Then the response status code should be 200
		And the response body should be verified with:
			| key  | value            |
			| name | <Workspace.name> |
			| id   | <Workspace.id>   |

	@functional @tc_26 @fixture_create_workspace
	Scenario: Delete an Workspace
		When the "DELETE" request to "/my/workspaces/<Workspace.id>" is sent
		Then the response status code should be 204

	@negative @tc_31 @fake_create_workspace
	Scenario: Error when get a non-existent Workspace
		When the "GET" request to "/my/workspaces/<Workspace.id>" is sent
		Then the response status code should be 404
		And the response body should be verified with:
			| key  | value            |
			| code | <Workspace.code> |
			| kind | <Workspace.kind> |

	@negative @tc_32
	Scenario: Error when workspace name is higher than 25
		Given the following body parameters:
			| key  | value                                           |
			| name | AUTO_NEW_WORKSPACE_WITH_MORE_THAN_25_CHARACTERS |
		When the "POST" request to "/my/workspaces" is sent
		Then the response status code should be 400
		And the response body should be verified with:
			| key  | value            |
			| code | <Workspace.code> |
			| kind | <Workspace.kind> |

	@negative @tc_33
	Scenario: Error when workspace name is a integer
		Given the following body parameters:
			| key  | value |
			| name | 12345 |
		When the "POST" request to "/my/workspaces" is sent
		Then the response status code should be 400
		And the response body should be verified with:
			| key  | value            |
			| code | <Workspace.code> |
			| kind | <Workspace.kind> |