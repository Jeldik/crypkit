@password
Feature: Attempt to signing up to Crypkit with different strength of password
  As new user I want to create new account with different strength of password

  Background: Go to the Sign up page
    Given I go to the site sign up

  Scenario Outline: I try to signing up with <password>
    When I type <password type> in password field
    And I move off the element
    Then I Should see text: <text>

    Examples:
      | password type   | text   |
      | weak password   | Weak   |
      | fair password   | Fair   |
      | good password   | Good   |
      | strong password | Strong |
