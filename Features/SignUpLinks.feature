Feature: Attempt to redirect from anchor links on Crypkit sign up page
  As new user I want to go to another page

  Scenario: User try to click on logo
    Given User visited sign up page
    When User click on "logo"
    Then User get to "homepage" page

  Scenario: User try to click on Sign in button
    Given User visited sign up page
    When User click on "sign in"
    Then User get to "sign in" page

  Scenario: User try to click on policy field
    Given User visited sign up page
    When User click on "policy"
    Then Should see the "policy" warning text
