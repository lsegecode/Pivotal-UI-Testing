@ui @story
Feature: UI Story
	As an application developer,
	I want to manage pivotal Home Page through UI,
	So that my app can get answers and show them.

	@tc_67 @functional @fixture_create_project @fixture_delete_project
	Scenario: Verify that a Story can be created
		Given I log in to Pivotal portal
		When I search the project on the search bar
		And I create the story with random data
		Then I should verify the story title

	@tc_68 @functional @fixture_create_project @fixture_create_story @fixture_delete_project
	Scenario: Verify that a Story can be deleted
		Given I log in to Pivotal portal
		When I search the project on the search bar
		And I click the "<Story.name>"
		And I click on the Delete button
		Then I confirm the deletion of the story "<Story.name>"

	@tc_69 @functional @fixture_create_project @fixture_create_story @fixture_delete_project
	Scenario: Verify that a Story name can be updated
		Given I log in to Pivotal portal
		When I search the project on the search bar
		And I click the "<Story.name>"
		And I edit the Story name
		Then I confirm the change of the "<Story name>"

	@tc_70 @functional @fixture_create_project @fixture_create_story @fixture_delete_project
	Scenario: Verify that a Story can be moved from icebox to currentbacklog
		Given I log in to Pivotal portal
		When I search the project on the search bar
		And I drag and drop the "<Story.name>" from icebox to currentbacklog
		Then I confirm the Story is in currentbacklog

	@tc_71 @functional @fixture_create_project @fixture_create_story @fixture_delete_project
	Scenario: Start Feature
		Given I log in to Pivotal portal
		When I search the project on the search bar
		And I click the "<Story.name>"
		And I change the story points
		And I change the story state from Unstarted to Started
		Then I check the Story state is Started

	@tc_72 @functional @fixture_create_project @fixture_create_story @fixture_delete_project
	Scenario: Start Bug
		Given I log in to Pivotal portal
		When I search the project on the search bar
		And I click the "<Story.name>"
		And I change the story type to bug
		And I change the story state from Unstarted to Started
		Then I check the Story state is Started

	@tc_73 @negative @fixture_create_project @fixture_delete_project
	Scenario: Create story without name
		Given I log in to Pivotal portal
		When I search the project on the search bar
		And I click on the add story button
		And I click on the save button
		Then I check an error window is displayed



