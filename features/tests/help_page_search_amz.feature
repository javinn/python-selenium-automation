# Created by JM at 2/2/2021

# Homework 3-2



Feature: Test Scenarios for Search on Amazon Help Page


  Scenario: User can search for Cancel Order
    Given Open Amazon Help page
    When Input Cancel order into Search Help field
    And Click on Enter button
    Then Verify Cancel Items or Orders is present