@elements
Feature: Check sign up page elements

  Background: Go to the Sign up page
    Given I go to the site sign up

  Scenario: The Sign Up page should have correct title
    Given The page title should be "Sign Up | Crypkit"

  Scenario: The Sign Up page should have correct url
    Given current url should be "https://app2.crypkit.com/signup"

  Scenario: I want to read policy
    When I click on policy button
    Then I Should see text: policy

  Scenario Outline: I try to click on <element>
    When I click on <element>
    Then I should be redirect to <page>

    Examples:
      | element | page         |
      | logo    | home page    |
      | sign in | sign in page |

