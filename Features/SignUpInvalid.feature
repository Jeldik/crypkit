Feature: Attempt to signing up to Crypkit with invalid credentials
  As new user I want to create new account

  @tagCurrent
  Scenario: User try to signing up with empty form
    Given User visited crypkit sign up page
    When User don't fill form
    And User hit Sign Up button
    Then Should see three warning messages

  Scenario: User try to signing up with invalid e-mail
    Given User visited crypkit sign up page
    When User fill invalid
    And User hit Sign Up button
    Then Should see invalid e-mail warning text

  Scenario: User try to signing up with short password
    Given User visited crypkit sign up page
    When User fill short password
    And User hit Sign Up button
    Then Should see short password warning text

  Scenario: User try to signing up with different password
    Given User visited crypkit sign up page
    When User fill password
    And User fill different password
    Then Should see different password warning text