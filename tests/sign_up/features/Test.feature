@test
Feature: Attempt to visit all categories in Seznam.cz

  Background: Go to Seznam.cz page
    Given I go to the site Seznam.cz

  Scenario Outline: I try to visit Categories from Seznam
    When I click on <category>
    Then the page should be open in new tab with <title> title

    Examples:
      | category | title                                               |
      | Novinky  | Novinky.cz – nejčtenější zprávy na českém internetu |
      | Super    | Super.cz                                            |
