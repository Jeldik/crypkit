Feature: Attempt to redirect from anchor links on Crypkit sign up page
  As new user I want to go to another page

  Scenario: Test logo click
    Given User visited crypkit sign up page
    When User click on logo
    Then Should get to homepage

  Scenario: Test signing in click
    Given User visited crypkit sign up page
    When User click on sign in button
    Then Should get to sign in page

  Scenario: Test policy click
    Given User visited crypkit sign up page
    When User click to policy button
    Then Should see policy text
