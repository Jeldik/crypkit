Feature: Sign up to Crypkit test
  As new user I want to create new account

  Scenario: Test sending valid form
    Given User visited crypkit sign up page
    When User fill valid form
    And User hit Sign Up button
    Then Should get to success page

  Scenario: Test valid password
    Given User visited crypkit sign up page
    When User type valid password
    And User hit Sign Up button
    Then User don't see warning message

  Scenario: Test same password
    Given User visited crypkit sign up page
    When User type in valid password
    And User type in same password
    Then Shouldn't see any warning text