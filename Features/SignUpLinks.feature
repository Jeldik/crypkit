Feature: Attempt to redirect from anchor links on Crypkit sign up page
  As new user I want to go to another page

  Scenario: User try to click on logo
    Given User visited crypkit sign up page
    When User click on logo
    Then Should get to homepage

  Scenario: User try to click on Sign in button
    Given User visited crypkit sign up page
    When User click on sign in button
    Then Should get to sign in page

  Scenario: User try to click on policy field
    Given User visited crypkit sign up page
    When User click to policy button
    Then Should see policy text
