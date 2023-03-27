from settings import SESSION_CONFIG_DEFAULTS


class Lexicon:

    # task
    lex_starting_balances = "Soldes de Départ"
    lex_interest_earned_last_period = "Intérêts Perçus le Mois Précédent"
    lex_total_cash = "Encaisse Totale"
    lex_ending_balances = "Soldes de Clôture"
    lex_savings_account = "Compte Épargne"
    lex_stock = "Stock"
    lex_unit = 'unité'
    lex_units = "unités"
    lex_market_data = "Données du Marché"
    lex_salary = "Salaire"
    lex_catalog = "Catalogue"
    lex_food = "Aliments"
    lex_price = "Prix"
    lex_my_cart = "Mon Panier"
    lex_name = "Nom"
    lex_quantity = "Quantité"
    lex_prix_total = "Prix Total"
    lex_finalize_purchase = "Finaliser l’Achat"
    lex_total = "Total"
    lex_current_choiceConfidence = "Dans quelle mesure êtes-vous sûr d'avoir pris la bonne décision ce mois-ci ?"
    lex_current_choiceConfidence_1 = "Pas du tout sûr d'avoir pris la bonne décision"
    lex_current_choiceConfidence_5 = "Absolument sûr d'avoir pris la bonne décision"
    lex_slider_your_value = "Votre estimation"
    lex_warning_final_purch = '''ATTENTION VOUS N'ALLEZ PAS SURVIVRE !! 
    • Le solde de votre stock est actuellement de 0.
    • Si c'est une erreur, veuillez cliquer sur *Annuler* et mettre à jour votre panier. 
    • Si vous n'avez pas assez d'argent, veuillez cliquer sur *OK* pour terminer le jeu et passer aux tâches supplémentaires.'''
    lex_warning_final_purch_2 = '''****Êtes-vous sûr(e) de ne pas vouloir survivre ?****
    • Cliquez sur "Annuler" pour changer votre panier.
    • Cliquez sur "OK" si vous voulez ne pas survivre.'''

    lex_slider = "Curseur"

    # General terms
    lex_game = "Jeu de l'Épargne"
    lex_I_do_not_know = "Je ne sais pas"
    lex_yes = "Oui"
    lex_no = "Non"
    lex_maybe = "Peut-être"
    lex_somewhat = "En partie"
    lex_true = "Vrai"
    lex_false = "Faux"
    lex_not_applicable = "Pas concerné"
    lex_more = "Plus"
    lex_less = "Moins"
    lex_the_same_amount = "La même quantité"
    lex_more_money = "Plus d'argent"
    lex_less_money = "Moins d'argent"
    lex_same_money = "Autant d'argent"
    lex_nothing = "Rien"
    lex_none_of_the_above = "Aucun de ces éléments"
    lex_next = "Suivant"

    lex_click_next = '''Cliquez sur le bouton "Suivant" ci-dessous 
    lorsque vous serez prêt à poursuivre.'''

    lex_completed_questionnaire = '''Vous avez maintenant terminé le 
    questionnaire. Cliquez sur le bouton "Suivant" ci-dessous 
    lorsque vous êtes prêt à continuer.'''

    lex_completed_game_round = f'''Vous avez maintenant terminé le 
    tour du jeu d’aujourd’hui. {lex_click_next}'''

    lex_completed_task_round = f'''Vous avez maintenant terminé le 
    tour du jeu d’aujourd’hui et les questions de suivi. 
    <br><br>{lex_click_next}'''

    lex_sliders_instructions = f'''Cliquez sur la barre bleue pour 
    faire apparaître le {lex_slider}. Faîtes-le glisser le long 
    de la barre pour sélectionner votre estimation avec votre souris 
    ou les flèches de votre clavier.'''

    lex_remunerated_questions = "Questions rémunérées"
    lex_increased = "Augmenté"
    lex_decreased = "Baissé"
    lex_stayed_same = "Resté constant"
    lex_increase = "Augmente"
    lex_decrease = "Baisse"
    lex_stay_same = "Reste constant"
    lex_no_change = "Pas de changement"
    lex_it_increases = "Il augmente."
    lex_it_decreases = "Il baisse."
    lex_it_stays_the_same = "Il reste constant."
    lex_not_enough_info = "Il n'y a pas assez d'informations pour déterminer l'effet."
    lex_instructions = "Instructions"
    lex_correct = "C'est exact."
    lex_interest_rate = "Taux d'Intérêt"
    lex_nominal_interest_rate = "Taux d'Intérêt Nominal"
    lex_real_interest_rate = "Taux d'Intérêt Réel"
    lex_inflation_rate = "Taux d'Inflation"
    lex_purchasing_power = "Pouvoir d'Achat"
    lex_completed_so_far = "État d'avancement"
    lex_comprehension = "Compréhension"
    lex_stock_up = f"Acheter plus d'une {lex_unit}"
    lex_save = f"Acheter 0 {lex_unit}"
    lex_buy_1 = f"Acheter 1 {lex_unit}"
    lex_buy_x = "Acheter {} {}"
    lex_buy_more_than = "Acheter plus de {} {}"

    # Numeracy
    lex_num_1 = '''Sur les 1.000 habitants d'une petite ville, 500 sont membres 
    d'une chorale. Sur ces 500 membres de la chorale, 100 sont des hommes. Sur 
    les 500 habitants qui ne sont pas dans la chorale, 300 sont des hommes. 
    Quelle est le pourcentage de chance qu'un homme tiré au hasard soit membre 
    de la chorale ? ________ (%) <br><br> (Indiquez un nombre entier)'''

    lex_num_2a = '''Imaginez que nous lançons 50 fois un dé à cinq faces. En 
    moyenne, sur ces 50 lancers, combien de fois ce dé à cinq faces 
    indiquera-t-il un nombre impair (1, 3 ou 5) ? ______ sur 50 lancers.'''

    lex_num_2b = '''Imaginez que nous lançons un dé pipé (6 faces). Le pourcentage 
    de chance que le dé indique un 6 est deux fois plus élevée que la probabilité 
    de chacun des autres chiffres. En moyenne, sur ces 70 lancers, combien de 
    fois le dé affichera-t-il le chiffre 6 ? ________ sur 70 lancers.'''

    lex_num_3 = '''Dans une forêt, 20% des champignons sont rouges, 50% bruns 
    et 30% blancs. Un champignon rouge est toxique avec un pourcentage de 
    chance de 20%. Un champignon qui n'est pas rouge est toxique avec un 
    pourcentage de chance de 5 %. Quelle est le pourcentage de chance qu'un 
    champignon toxique de la forêt soit rouge ? ________ (%)'''

    lex_numatt_1 = '''Sur une échelle de 1 à 5, quel est votre degré de 
    confiance dans vos capacités mathématiques ?'''

    lex_numatt_2 = '''Sur une échelle de 1 à 5, quel est votre degré de 
    confiance dans vos capacités à prendre des décisions financières ?'''

    lex_numatt_3 = '''Sur une échelle de 1 à 5, quel est votre degré de 
    confiance dans votre compréhension des probabilités ?'''

    lex_numatt_4 = '''Sur une échelle de 1 à 5, quel est votre degré de 
    confiance dans votre compréhension de l'économie ?'''

    lex_numatt_not_confident = "Pas du tout confiant"
    lex_numatt_confident = "Absolument confiant"

    # Loss aversion
    lex_toss_coin = "Lancer la pièce"
    lex_dont_toss_coin = "Ne pas lancer"

    # BRET
    lex_bret_bomb_collected = "Bombe collectée"
    lex_bret_boxes_collected = "Nombre de boîtes collectées"
    lex_bret_boxes_remaining = "Number of boxes remaining"
    lex_bret_boxes_to_collect = "Nombre de boîtes restantes"
    lex_bret_results = 'Résultats'
    lex_bret_round_history = "Histoire des tours"
    lex_bret_round_number = "Numéro du tour"
    lex_bret_round_payoff = "Gain du tour"
    lex_bret_start = "Début"
    lex_bret_stop = "Stop"
    lex_bret_solve = "Résoudre"
    lex_bret_your_decision = "Votre décision"

    # timePreferences
    lex_timePreferences_task_name = "Planificateur de paiement"
    lex_timePreferences_sooner = "Maintenant"
    lex_timePreferences_which = "Que préférez-vous ?"
    lex_timePreferences_delay_1 = "1 semaine"
    lex_timePreferences_delay_2 = "2 semaines"
    lex_timePreferences_delay_3 = "1 mois"
    lex_timePreferences_delay_4 = "3 mois"
    lex_timePreferences_delay_5 = "6 mois"
    lex_timePreferences_delay_6 = "1 an"

    # Error messages
    lex_error_task_instructions_general = '''C'est inexact. Veuillez 
    revoir les instructions et corriger votre réponse.'''

    lex_error_not_correct_selection = "C'est inexact. Veuillez réessayer."
