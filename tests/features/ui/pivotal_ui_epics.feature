@ui @epics
Feature: UI Epics
    As an application developer,
    I want to manage pivotal Home Page through UI,
    So that my app can get answers and show them.

    @tc_100 @fixture_create_project @fixture_delete_project
    Scenario: Verify that an Epic can be created
        Given I log in to Pivotal portal
        When I click on the "<Project.name>" on "project"
        And I create an epic with random data
        Then I should verify that the name is displayed correctly

    @tc_101 @fixture_create_project @fixture_delete_project
    Scenario: Verify that an Epic can be deleted
        Given I log in to Pivotal portal
        When I click on the "<Project.name>" on "project"
        And I create an epic with random data
        And I delete an epic
        Then I should verify that the epic is deleted

    @tc_102 @fixture_create_project @fixture_delete_project
    Scenario: Verify that an Epic can be updated
        Given I log in to Pivotal portal
        When I click on the "<Project.name>" on "project"
        And I create an epic with random data
        And I modify the title of an epic
        Then I should verify that the epic title was updated

    @tc_103 @fixture_create_project @fixture_delete_project
    Scenario: Verify that an Epic can be followed
        Given I log in to Pivotal portal
        When I click on the "<Project.name>" on "project"
        And I create an epic with random data     
        And I follow an epic
        Then I should verify that the epic is followed

    @tc_104 @fixture_create_project @fixture_delete_project
    Scenario: Verify that a Description can be added to an epic
        Given I log in to Pivotal portal
        When I click on the "<Project.name>" on "project"
        And I create an epic with random data
        And I add an epic description
        Then I should verify the description can be added