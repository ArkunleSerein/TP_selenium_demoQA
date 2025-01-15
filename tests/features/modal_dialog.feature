Feature: Vérifier le contenu du Large Modal sur le site DemoQA

  Scenario: Ouvrir le Large Modal et vérifier qu'il contient 4 fois le terme "lorem ipsum"
    Given je suis sur la page Modal Dialogs de DemoQA
    When je clique sur "Large Modal"
    Then je vérifie que "lorem ipsum" apparaît 4 fois dans le texte du Large Modal
