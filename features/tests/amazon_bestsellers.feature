# Created by JM at 2/8/2021


# Homework 4-1


Feature: Test Scenarios for Amazon Bestsellers Page


  Scenario: User checks the number of links
    Given Open Amazon Main page
    When User opens Bestsellers
    Then Verify number of links is 5
    And Click on Bestsellers