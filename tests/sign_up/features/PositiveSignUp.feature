Feature: Sign up to Crypkit test
  As new user I want to create new account

  Scenario: User try to signing up with valid credentials
    Given User visited sign up page
    When User fill valid form
    And User click on "sign up"
    Then User should get to "success" page

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