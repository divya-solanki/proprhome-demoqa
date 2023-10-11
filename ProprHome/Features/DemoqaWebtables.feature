Feature: DemoqaWebTables


  Scenario:
   Given Open the website in the chrome Browser
    When Navigate to demoqa "https://demoqa.com/webtables" website
    Then Click the add button
    Then Fill in the register form and submit
    Then Verifydata in the webtable
    Then delete a row by clicking the delete butoon in a web table
