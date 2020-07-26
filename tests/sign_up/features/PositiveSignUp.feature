@positive
Feature: Attempt to signing up to Crypkit with valid credentials
  As new user I want to create new account

  Scenario: I try to signing up with valid credentials
    Given I go to the site sign up
    When I fill valid form
    And I click on sign up button
    Then I should be redirect to next page
