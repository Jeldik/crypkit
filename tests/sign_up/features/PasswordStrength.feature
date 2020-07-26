@password
Feature: Attempt to signing up to Crypkit with different strength of password
  As new user I want to create new account with different strength of password

  Scenario: I try to signing up with weak password
    Given I go to the site sign up
    When I type weak password in password field
    And I move off the element
    Then I Should see text: Weak

  Scenario: I try to signing up with fair password
    Given I go to the site sign up
    When I type fair password in password field
    And I move off the element
    Then I Should see text: Fair

  Scenario: I try to signing up with good password
    Given I go to the site sign up
    When I type good password in password field
    And I move off the element
    Then I Should see text: Good

  Scenario: I try to signing up with strong password
    Given I go to the site sign up
    When I type strong password in password field
    And I move off the element
    Then I Should see text: Strong
