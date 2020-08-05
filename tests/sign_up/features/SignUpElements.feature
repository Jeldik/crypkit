@elements
Feature: Check sign up page elements

  Background: Go to the Sign up page
    Given I go to the site sign up

  Scenario: The Sign Up page should have correct title
    Given The page title should be "Sign Up | Crypkit"

  Scenario: The Sign Up page should have correct url
    Given current url should be "https://app2.crypkit.com/signup"

  Scenario: I try to click on logo
    When I click on logo
    Then I should be redirect to home page

  Scenario: I try to redirect to Sign in page
    When I click on sign in
    Then I should be redirect to sign in page

  Scenario: I want to read policy
    When I click on policy button
    Then I Should see text: policy
