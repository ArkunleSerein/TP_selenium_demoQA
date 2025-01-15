Feature: Gestion des Web Tables

  Scenario: Supprimer les deux dernières lignes et modifier le salaire de la première ligne
    Given je suis sur la page Web Tables
    When je supprime les deux dernières lignes et modifie le salaire de la première ligne
    Then je vérifie que le salaire a bien été mis à jour à 4300
