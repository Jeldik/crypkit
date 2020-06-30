Feature: Attempt to signing up to Crypkit with invalid credentials
  As new user I want to create new account

  @current
  Scenario: I shouldn't sign up with empty form
    Given I go to the site sign_up
    When I click on sign_up_button
    Then I Should see the email_error_message text
    And I Should see the password_error_message text
    And I Should see the password_confirm_error_message text
  @current
  Scenario: User try to signing up with invalid e-mail
    Given I go to the site sign_up
    When I type invalid e-mail format
    And I click on sign_up_button
    Then I Should see the email_error_message text

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