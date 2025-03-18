Feature: Target search test cases

  #Scenario: User can search for a tea on Target
  #  Given Open target main page
   # When Search for tea
   # Then Verify correct search results shown for tea

 # Scenario Outline: User can search for a product on Target
  #  Given Open Google page
   # When Input Car into search field
    #And Click on search icon
   # Then Product results for Car are shown

  Scenario: 'Your cart is empty' search is shown for empty cart
    Given Open target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty'

   Scenario: 'Sign into your Target account' search is shown for sing in
    Given Open target main page
    When Click on sing in icon
    Then Verify 'Sign into your Target account'