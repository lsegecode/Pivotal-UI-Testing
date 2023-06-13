@ui @workspace
Feature: UI Workspace
	As an application developer,
	I want to manage pivotal Home Page through UI,
	So that my app can get answers and show them.

	@tc_62 @fixture_delete_workspace
	Scenario: Verify that a Workspace can be created
		Given I log in to Pivotal portal
		When I click on "Workspaces" tag on dashboard tabs
		And I click on "Create workspace" button
		And I create the "workspace" with random data
		And I get the Id "workspace" from the description page
		And I click on "MORE" navigation tab
		Then I verify that the Workspace information is displayed on Workspace Details page

	@tc_63 @fixture_create_workspace
	Scenario: Verify that a Workspace can be deleted
		Given I log in to Pivotal portal
		When I click on "Workspaces" tag on dashboard tabs
		And I click on the "<Workspace.name>" on "workspace"
		And I click on the "Delete" link from the "MORE" navigation tab
		And I click on "Workspaces" tag on dashboard tabs
		Then I confirm the deletion of the "workspace" with name "<Workspace.name>"

	@tc_64 @fixture_create_workspace @fixture_delete_workspace
	Scenario Outline: Verify that a Workspace can be updated
		Given I log in to Pivotal portal
		When I click on "Workspaces" tag on dashboard tabs
		And I click on the workspace
		And I click on "MORE" navigation tab
		And I change the data with "<name>"
		Then I verify that the Workspace information is displayed on Workspace Details page
		Examples: Workspaces
			| name             |
			| workspace_name_1 |
			| 31123132313      |
			| ()(##))##*++++#  |
			| (black space)    |

	@tc_65 @fixture_create_workspace @fixture_delete_workspace
	Scenario: Verify that a Workspace can be obtained
		Given I log in to Pivotal portal
		When I click on "Workspaces" tag on dashboard tabs
		And I click on the "<Workspace.name>" on "workspace"
		And I click on "MORE" navigation tab
		Then I verify that the Workspace information is displayed on Workspace Details page

	@tc_66 @negative
	Scenario: Verify that error messages are displayed if required data is missing when create a Workspace
		Given I log in to Pivotal portal
		When I click on "Workspaces" tag on dashboard tabs
		And I click on "Create workspace" button
		And I try to create the workspace without a name
		Then I verify the error message "Workspace name can't be blank." is displayed on "workspaces"
