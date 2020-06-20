Feature: Attempt to signing up to Crypkit with invalid credentials
  As new user I want to create new account

  @tagCurrent
  Scenario: Test sending empty form
    Given User visited crypkit sign up page
    When User don't fill form
    And Hit Sign Up button
    Then Should see three warning messages

  Scenario: Test invalid e-mail
    Given User visited crypkit sign up page
    When User fill invalid
    And Hit Sign Up button
    Then Should see invalid e-mail warning text

  Scenario: Test short password
    Given User visited crypkit sign up page
    When User fill short password
    And Hit Sign Up button
    Then Should see short password warning text

  Scenario: Test different password
    Given User visited crypkit sign up page
    When User fill password
    And User fill different password
    Then Should see different password warning text