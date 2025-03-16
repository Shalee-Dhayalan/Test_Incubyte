Feature: Login to Magento

  Background: Common Steps
    Given the user is on the Magento login page
    When the user enters email "test@gmail.com" and password "Test@123"
    And clicks the login button

  Scenario: Login with valid credentials
    Then the user should be successfully logged in

  Scenario: Login with invalid credentials
    Then the user should see an error message