Feature: Interaction avec les widgets sur le site DemoQA

  Scenario: Vérifier que le bouton Start atteint 100%
    Given je suis sur la page des widgets de DemoQA
    When je clique sur le bouton "Start"
    Then je vérifie que la barre de progression atteint 100%

#   Scenario: Naviguer dans le Main Item 2 et cliquer sur Sub Sub Item 2
#     Given je suis sur la page des widgets de DemoQA
#     When je navigue vers le "Main Item 2" puis "Sub Sub List" et clique sur "Sub Sub Item 2"
#     Then je vérifie que l'élément "Sub Sub Item 2" est sélectionné
