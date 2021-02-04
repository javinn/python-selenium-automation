# Created by JM at 2/2/2021

#  Homework 3-3

Feature: Test Scenarios for Amazon Shopping Cart

  Scenario:  is empty
    Given Open Amazon Main page
    When Click on Shopping Cart
    Then Verify Shopping Cart is empty



#  Homework 3-4

  Scenario: User checks Shopping Cart
    Given Open Amazon Main page
    When User opens Bestsellers
    And User opens Bestseller Books
    And User opens the Top Bestseller
    And User adds to Cart
    And Click on Shopping Cart
    Then Verify Shopping Cart has exact 1 Item(s)
