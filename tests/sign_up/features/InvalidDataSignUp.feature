Feature: Attempt to signing up to Crypkit with invalid credentials
  As new user I want to create new account

  @tagCurrent
  Scenario: User shouldn't sign up with empty form
    Given I go to the site "https://app2.crypkit.com/signup"
    When I click on "sign up" button
    Then Should see three warning messages

  Scenario: User try to signing up with invalid e-mail
    Given User get to "sign up" page
    When User type invalid format e-mail
    And User click on "sign up" button
    Then Should see the "invalid e-mail" warning text

  Scenario: User try to signing up with short password
    Given User get to "sign up" page
    When User type short password
    And User click on "sign up" button
    Then Should see the "short password" warning text

  Scenario: User try to signing up with different password
    Given User get to "sign up" page
    When User type password
    And User type different password
    Then Should see the "different password" warning text