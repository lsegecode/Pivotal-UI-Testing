@ui @project
Feature: UI Project
	As an application developer,
	I want to manage pivotal Home Page through UI,
	So that my app can get answers and show them.

	@tc_55 @fixture_delete_project
	Scenario: Verify that a Project can be created
		Given I log in to Pivotal portal
		When I click on "Projects" tag on dashboard tabs
		And I click on "Create project" button
		And I create the "project" with random data
		And I get the Id "project" from the description page
		And I click on "MORE" navigation tab
		Then I verify that the Project information is displayed on Project Details page

	@tc_57 @fixture_create_project
	Scenario: Verify that a Project can be deleted
		Given I log in to Pivotal portal
		When I search "<Project.name>" on the search bar
		And I click on the "Delete" link from the "MORE" navigation tab
		Then I confirm the deletion of the "project" with name "<Project.name>"

	@tc_58 @fixture_create_project @fixture_delete_project
	Scenario Outline: Verify that a Project can be updated
		Given I log in to Pivotal portal
		When I search the project on the search bar
		And I click on "MORE" navigation tab
		And I change the data with "<name>" and "<description>"
		Then I verify that the Project information is displayed on Project Details page
		Examples: Projects
			| name            | description      |
			| project_name_1  | desc_1           |
			| 31123132313     | 1231421241235131 |
			| ()(##))##*++++# | ......---""""""  |
			| (black space)   | (blanck space)   |

	@tc_59 @fixture_create_project @fixture_delete_project
	Scenario: Verify that a Project can be obtained
		Given I log in to Pivotal portal
		When I search "<Project.name>" on the search bar
		And I click on "MORE" navigation tab
		Then I verify that the Project information is displayed on Project Details page

	@tc_60 @negative
	Scenario: Verify that error messages are displayed if required data is missing when create a Project
		Given I log in to Pivotal portal
		When I click on "Projects" tag on dashboard tabs
		And I click on "Create project" button
		And I try to create the project without a name and an account
		Then I verify the error message "Enter a name for your project" is displayed on "projects"
		And I verify the error message "Please select or create an account for the new project" is displayed on "projects"

	@tc_61 @fixture_create_project @fixture_delete_project
	Scenario: Verify that Project fields can be updated
		Given I log in to Pivotal portal
		When I search "<Project.name>" on the search bar
		And I click on "MORE" navigation tab
		Then I update the project with:
			| key                               | value                       |
			| name                              | test_61_project_name        |
			| description                       | test_61_project_description |
			| enable_tasks                      | False                       |
			| public                            | True                        |
			| week_start_day                    | Thursday                    |
			| time_zone                         | (GMT-05:00) Bogota          |
			| iteration_length                  | 2                           |
			| point_scale                       | Powers of 2 (0, 1, 2, 4, 8) |
			| initial_velocity                  | 25                          |
			| velocity_averaged_over            | Average of 4 iterations     |
			| number_of_done_iterations_to_show | 15                          |
			| automatic_planning                | False                       |
			| enable_incoming_emails            | False                       |
		Then I verify that the Project information is displayed on Project Details page
