Feature: Sign In Access

  Scenario: Logged out user can access Sign In page
    Given Open Target main page
    When Click Sign In in header
    And Click Sign In from side menu
    Then Verify Sign In page is opened



