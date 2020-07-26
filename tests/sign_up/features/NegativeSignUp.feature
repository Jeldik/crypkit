@negative
Feature: Attempt to signing up to Crypkit with invalid credentials
  As new user I want to create new account

  Scenario: I shouldn't sign up with empty form
    When I go to the site sign up
    Then sign up button should be disabled

  Scenario: I try to signing up with invalid e-mail
    Given I go to the site sign up
    When I type invalid email in email field
    And I move off the element
    Then I Should see text: Email is not valid.

  Scenario: I try to signing up with weak password
    Given I go to the site sign up
    When I type weak password in password field
    And I move off the element
    Then I Should see text: Weak
    And I Should see text: Password is too weak

  Scenario: I try to signing up with different passwords
    Given I go to the site sign up
    When I type valid password in password field
    And I type different confirm password in confirm password field
    And I move off the element
    Then I Should see text: Passwords must match