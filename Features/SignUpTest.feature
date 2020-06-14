Feature: Sign up to Crypkit test
  As new user I want to create new account

  Scenario: Test sending empty form
    Given User visited crypkit sign up page
    When User don't fill form
    And Hit Sign Up button
    Then Should see three warning messages

  Scenario: Test sending valid form
    Given User visited crypkit sign up page
    When User fill valid form
    And Hit Sign Up button
    Then Should get to success page

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

  Scenario: Test valid password
    Given User visited crypkit sign up page
    When User fill valid password
    And Hit Sign Up button
    Then User don't see warning message

  Scenario: Test different password
    Given User visited crypkit sign up page
    When User fill password
    And User fill different password
    Then Should see different password warning text

  Scenario: Test same password
    Given User visited crypkit sign up page
    When User fill in valid password
    And User fill same password
    Then Shouldn't see any warning text

  Scenario: Test logo click
    Given User visited crypkit sign up page
    When User click on logo
    Then Should get to homepage

  Scenario: Test Sign In
    Given User visited crypkit sign up page
    When User click on sign in button
    Then Should get to sign in page

  Scenario: Test policy
    Given User visited crypkit sign up page
    When User click to policy button
    Then Should see policy text
