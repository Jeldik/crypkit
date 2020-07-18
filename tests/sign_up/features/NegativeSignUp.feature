@tom
Feature: Attempt to signing up to Crypkit with invalid credentials
  As new user I want to create new account

  Scenario: I shouldn't sign up with empty form
    When I go to the site sign_up
    Then sign_up_button should be disabled


  Scenario: I try to signing up with invalid e-mail
    Given I go to the site sign_up
    When I type invalid_email format
    And I move off the element
    Then I Should see text: Email is not valid.


  Scenario: I try to signing up with weak password
    Given I go to the site sign_up
    When I type weak_password
    And I move off the element
    Then I Should see text: Password is too weak

@tomas
  Scenario: I try to signing up with different passwords
    Given I go to the site sign_up
    When I type valid_password
    And I type different_confirm_password
    And I move off the element
    Then I Should see text: Passwords must match