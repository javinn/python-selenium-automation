# Created by JM at 3/23/2021
# Homework 6-1


Feature: Test Scenarios for TC Page

  Scenario: User can open and close Amazon Applications
    Given Open Amazon T&C page
    When Store original windows
    And Click on Amazon applications link
    And Switch to the newly opened window
    Then Amazon app page is opened
    And User can close new window and switch back to original