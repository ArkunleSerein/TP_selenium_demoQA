# checkbox.feature
Feature: Tester les checkboxes sur le site DemoQA

Scenario: Sélectionner et vérifier un élément
  Given je suis sur la page des checkboxes
  When je sélectionne tous, sauf Excel File.doc et Office
  Then je dois voir le message 'You have selected : desktop notes commands workspace react angular veu wordFile' soit affiché
