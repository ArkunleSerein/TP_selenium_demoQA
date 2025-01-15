Feature: Validation du formulaire de contact 
    Comme un visiteur
    Je voudrais m'assurer que le formulaire de contact est fonctionnel

    Scenario: Vérifie la présence du formulaire de contact
        Given Je suis sur la page de contact
        When Je veux compléter les champs requis
        Then Je devrais pouvoir remplir tous les champs
        And Je devrais pouvoir soumettre le formulaire

