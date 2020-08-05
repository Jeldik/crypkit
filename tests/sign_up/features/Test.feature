@test
Feature: Attempt to visit all categories in Seznam.cz

  Background: Go to Seznam.cz page
    Given I go to the site Seznam.cz

  Scenario: I try to visit Novinky from Seznam
    When I click on Novinky
    Then the page should be open in new tab with Novinky.cz – nejčtenější zprávy na českém internetu title

  Scenario: I try to visit Živě.cz from Seznam
    When I click on Super
    Then the page should be open in new tab with Super.cz title