@positive
Feature: Attempt to signing up to Crypkit with valid credentials
  As new user I want to create new account
@tom
  Scenario: User try to signing up with valid credentials
    Given I go to the site sign_up
    When I fill valid form
    And I click on sign_up_button
    Then I should navigate to next page

  Scenario: User try to signing up with valid password
    Given User visited sign up page
    When User type valid password
    And User click on "sign up"
    Then User don't see warning message

  Scenario: User try to signing up with same password
    Given User visited sign up page
    When User type in valid password
    And User type in same password
    Then User shouldn't see any warning text