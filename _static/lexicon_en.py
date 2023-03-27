from settings import SESSION_CONFIG_DEFAULTS


class Lexicon:

    # task
    lex_starting_balances = "Starting Balances"
    lex_interest_earned_last_period = "Interest Earned Last Month"
    lex_total_cash = "Total Cash"
    lex_ending_balances = "Ending Balances"
    lex_savings_account = "Savings Account"
    lex_stock = "Stock"
    lex_unit = 'unit'
    lex_units = "units"
    lex_market_data = "Market Data"
    lex_salary = "Salaire"
    lex_catalog = "Catalog"
    lex_food = "Food"
    lex_price = "Price"
    lex_my_cart = "My Cart"
    lex_name = "Name"
    lex_quantity = "Quantity"
    lex_prix_total = "Total price"
    lex_finalize_purchase = "Finalize Purchase"
    lex_total = "Total"
    lex_current_choiceConfidence = '''"How confident are you that you made the 
    right decision this month?'''

    lex_current_choiceConfidence_1 = '''"Not at all confident to have made the 
    right decision'''

    lex_current_choiceConfidence_5 = '''"Absolutely confident to have made the 
    right decision'''

    lex_slider_your_value = "Your estimate"

    lex_warning_final_purch = f'''Warning! Your {lex_stock} balance is currently 0. 
    If this is a mistake, please click Cancel and update {lex_my_cart}. If you do 
    not have enough money, please click OK to end the game and proceed to the 
    additional tasks.'''

    lex_slider = "Slider"

    # General expressions
    lex_game = "Savings Game"
    lex_I_do_not_know = "I do not know"
    lex_yes = "Yes"
    lex_no = "No"
    lex_maybe = "Maybe"
    lex_somewhat = "Somewhat"
    lex_true = "True"
    lex_false = "False"
    lex_not_applicable = "Not applicable"
    lex_more = "More"
    lex_less = "Less"
    lex_the_same_amount = "The same amount"
    lex_more_money = "More money"
    lex_less_money = "Less money"
    lex_same_money = "The same amount of money"
    lex_none_of_the_above = "None of the above"
    lex_next = "Next"
    lex_click_next = '''Click the Next button below to proceed.'''

    lex_completed_questionnaire = '''You have completed the questionnaire. 
    Please, click the Next button below to proceed.'''

    lex_completed_game_round = '''You have now completed today's round of the 
    game. Click the Next button below to proceed to the follow-up questions.'''

    lex_completed_task_round = '''You have now completed today's round of the 
    game and follow-up questions. Click the Next button below to proceed.'''

    lex_slider = "Slider"

    lex_sliders_instructions = f'''Click the blue bar to reveal the 
    {lex_slider}. Drag it along the bar to select your estimate with either 
    your mouse or the arrow keys on your keyboard.'''

    lex_remunerated_questions = "Remunerated Questions"
    lex_increased = "Increased"
    lex_decreased = "Decreased"
    lex_stayed_same = "Stayed the same"
    lex_increase = "Increase"
    lex_decrease = "Decrease"
    lex_stay_same = "Stay the same"
    lex_no_change = "No change"
    lex_it_increases = "It increases."
    lex_it_decreases = "It decreases."
    lex_it_stays_the_same = "It stays the same."
    lex_not_enough_info = "There is not enough information to determine the effect."
    lex_instructions = "Instructions"
    lex_correct = "That is correct."
    lex_interest_rate = "Interest Rate"
    lex_nominal_interest_rate = "Nominal Interest Rate"
    lex_real_interest_rate = "Real Interest Rate"
    lex_completed_so_far = "Completed so far"
    lex_inflation_rate = "Inflation Rate"
    lex_purchasing_power = "Purchasing Power"
    lex_comprehension = "Comprehension"
    lex_stock_up = f"Buy more than 1 {lex_unit}"
    lex_save = "Save"
    lex_buy_1 = f"Buy 1 {lex_unit}"
    lex_buy_x = "Buy {} {}"
    lex_buy_more_than = "Buy more than {} {}"

    # Numeracy
    lex_num_1 = '''Out of 1,000 people in a small town 500 are members of a 
    choir. Out of these 500 members in the choir 100 are men. Out of the 500 
    inhabitants that are not in the choir 300 are men. What is the probability 
    that a randomly drawn man is a member of the choir? ________ (%)'''

    lex_num_2a = '''Imagine we are throwing a five-sided die 50 times. On 
    average, out of these 50 throws how many times would this five-sided die 
    show an odd number (1, 3 or 5)? ______ out of 50 throws.'''

    lex_num_2b = '''Imagine we are throwing a loaded die (6 sides). The 
    probability that the die shows a 6 is twice as high as the probability of 
    each of the other numbers. On average, out of these 70 throws how many times 
    would the die show the number 6? ________out of 70 throws.'''

    lex_num_3 = '''In a forest 20% of mushrooms are red, 50% brown and 30% 
    white. A red mushroom is poisonous with a probability of 20%. A mushroom 
    that is not red is poisonous with a probability of 5%. What is the 
    probability that a poisonous mushroom in the forest is red? ________ (%)'''

    lex_numatt_1 = '''On a scale of 1 to 5, how confident are you in your 
    mathematical abilities?'''

    lex_numatt_2 = '''On a scale of 1 to 5, how confident are you in your 
    financial decision-making abilities?'''

    lex_numatt_3 = '''On a scale of 1 to 5, how confident are you in your 
    understanding of mathematics?'''

    lex_numatt_4 = '''On a scale of 1 to 5, how confident are you in your 
    understanding of probability?'''

    lex_numatt_5 = '''On a scale of 1 to 5, how confident are you in your 
    understanding of economics?'''

    lex_numatt_not_confident = "Not confident at all"
    lex_numatt_confident = "Absolutely confident"

    # Loss aversion
    lex_toss_coin = "Toss coin"
    lex_dont_toss_coin = "Don't toss coin"

    # BRET
    lex_bret_bomb_collected = "Bomb collected"
    lex_bret_boxes_collected = "Number of boxes collected"
    lex_bret_boxes_remaining = "Number of boxes remaining"
    lex_bret_boxes_to_collect = "Number of boxes to collect"
    lex_bret_results = 'Results'
    lex_bret_round_history = "Round history"
    lex_bret_round_number = "Round no."
    lex_bret_round_payoff = "Round payoff"
    lex_bret_solve = "Solve"
    lex_bret_start = "Start"
    lex_bret_stop = "Stop"
    lex_bret_your_decision = "Your decision"

    # timePreferences
    lex_timePreferences_task_name = "Payment Scheduler"
    lex_timePreferences_sooner = "Right Now"
    lex_timePreferences_which = "Which do you prefer?"
    lex_timePreferences_delay_1 = "1 week"
    lex_timePreferences_delay_2 = "2 weeks"
    lex_timePreferences_delay_3 = "1 month"
    lex_timePreferences_delay_4 = "3 months"
    lex_timePreferences_delay_5 = "6 months"
    lex_timePreferences_delay_6 = "1 year"

    # Error messages

    lex_error_task_instructions_general = '''That is incorrect. Please, review 
    the instructions and correct your answer.'''

    lex_error_not_correct_selection = '''That is incorrect. Please, try again.'''
