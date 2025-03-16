Feature: User Registration on Magento

  Background: Common steps
    Given the user is on the Magento Create Account page
    When the user enters personal details:
      | First Name | Last Name | Email          |
      | hello      | world     | test@abc.com   |

  Scenario: Validate password strength and create an account
    Then the user validates password strength
    When the user sets password "abCD!@12" and confirms "abCD!@12"
    And the user submits the registration form
    Then the account should be created successfully

  Feature: User Registration on Magento
      Then the user validates password strength:
      | Password  |
      | abc89     |
      | abCD!2  |
    When the user sets password "abCD!@12" and confirms "abCD!@12"
    And the user submits the registration form
    Then the account cannot create account successfully

   Scenario: Validate different password strengths
    Given the user is on the Magento Create Account page
    When the user enters the following passwords:
      | Password      |
      | abcde123      |
      | ABC!@#%^      |
      | asCD1234      |
      | abcABC!@      |
    Then the system should validate each password