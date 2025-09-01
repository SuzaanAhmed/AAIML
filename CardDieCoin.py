import random

class Toss:
    def __init__(self):
        self.coin_outcomes = ['H', 'T']

        self.All_die_outcomes = [1, 2, 3, 4, 5, 6]
        self.Odd_die_outcomes = [1, 3, 5]
        self.Even_die_outcomes = [2, 4, 6]

        self.cards = {
            's1': 1, 's2': 2, 's3': 3, 's4': 4, 's5': 5, 's6': 6, 's7': 7, 's8': 8, 's9': 9, 's10': 10,
            'c1': 1, 'c2': 2, 'c3': 3, 'c4': 4, 'c5': 5, 'c6': 6, 'c7': 7, 'c8': 8, 'c9': 9, 'c10': 10,
            'h1': 1, 'h2': 2, 'h3': 3, 'h4': 4, 'h5': 5, 'h6': 6, 'h7': 7, 'h8': 8, 'h9': 9, 'h10': 10,
            'd1': 1, 'd2': 2, 'd3': 3, 'd4': 4, 'd5': 5, 'd6': 6, 'd7': 7, 'd8': 8, 'd9': 9, 'd10': 10,
            'K': 20, 'Q': 17, 'J': 15
        }
        self.totalProb = 1.0  

    def flip_a_coin(self, number_of_flips):
        if number_of_flips <= 0:
            return 'None', 0.0

        head_count = 0
        tail_count = 0
        for _ in range(number_of_flips):
            if random.choice(self.coin_outcomes) == 'H':
                head_count += 1
            else:
                tail_count += 1

        if head_count > tail_count:
            return 'H', head_count / number_of_flips
        elif tail_count > head_count:
            return 'T', tail_count / number_of_flips
        else:
            return random.choice(['H', 'T']), 0.5  

    def roll_a_die(self, number_of_rolls):
        avoid_even = False
        avoid_odd = False
        if number_of_rolls % 2 != 0 and number_of_rolls > 11:
            avoid_even = True
        elif number_of_rolls % 2 == 0 and number_of_rolls > 11:
            avoid_odd = True
        else:
            pass

        total_sum = 0
        if avoid_even:
            present_die_outcomes = self.Odd_die_outcomes
        elif avoid_odd:
            present_die_outcomes = self.Even_die_outcomes
        else:
            present_die_outcomes = self.All_die_outcomes

        for _ in range(number_of_rolls):
            roll_outcome = random.choice(present_die_outcomes)
            total_sum += roll_outcome
            self.totalProb *= 1/len(present_die_outcomes)
        
        print(f"No. or rolls: {number_of_rolls}, Sum of all rolls: {total_sum}. Probability: {self.totalProb:.8f}.")
        return self.flip_a_coin(total_sum)

    def pick_a_card(self):
        card_name, card_value = random.choice(list(self.cards.items()))

        if card_name in ['K', 'Q', 'J']:
            card_probability = 12 / 52
            self.totalProb = card_probability 
        else:
            card_probability = 4 / 52
            self.totalProb = card_probability
        
        print(f"The card picked : {card_name}. The probability of picking this was {card_probability:.4f}.")
        
        return self.roll_a_die(card_value)
        
if __name__ == "__main__":
    toss = Toss()
    
    while True:
        coin_selection = input("Choose heads or tails (H/T): ").upper()
        if coin_selection in ['H', 'T']:
            break
        print("Invalid choice. Please enter 'H' or 'T'.")

    winner, probability = toss.pick_a_card()
    print(f"The calculated probability is: {probability:.2f}")

    if coin_selection == winner:
        print(f"You win! Majority of flips landed on {winner}.")
    else:
        print(f"You lose! Majority of flips landed on {winner} .")