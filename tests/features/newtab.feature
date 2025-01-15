Feature: Fermer la fenêtre NewTab sur le site DemoQA

  Scenario: Ouvrir et fermer la fenêtre NewTab
    Given je suis sur la page DemoQA
    When je clique sur le lien 'New Tab'
    Then je vérifie que la nouvelle fenêtre est ouverte
    And je ferme la fenêtre
    And je reviens à la fenêtre principale
