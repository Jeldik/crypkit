Feature: Check sign up page elements

  Scenario: The Sign Up page should have correct title
    When I go to the site sign up
    Then The page title should be "Sign Up | Crypkit"

  Scenario: The Sign Up page should have correct url
    Given I go to the site sign up
    Then current url should be "https://app2.crypkit.com/signup"

  Scenario: I try to click on logo
    Given I go to the site sign up
    When I click on logo
    Then I should be redirect to home page

  Scenario: I try to redirect to Sign in page
    Given I go to the site sign up
    When I click on sign in
    Then I should be redirect to sign in page

  Scenario: I want to read policy
    Given I go to the site sign up
    When I click on policy button
    Then I Should see text: policy
