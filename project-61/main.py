import random

# Function to simulate Independent Events (e.g., Coin Flips)
def independent_events():
    print("--- Independent Events (Coin Flips) ---")
    # Event A: First flip is Heads
    # Event B: Second flip is Heads
    # Probability of both is P(A) * P(B)
    p_a = 0.5
    p_b = 0.5
    p_both = p_a * p_b
    print(f"Probability of First flip Heads: {p_a}")
    print(f"Probability of Second flip Heads: {p_b}")
    print(f"Both flips are Heads: {p_both} (Since Flips don't affect each other)")

# Function to simulate Dependent Events (e.g., Drawing cards without replacement)
def dependent_events():
    print("\n--- Dependent Events (Drawing Cards without Replacement) ---")
    # A standard deck has 52 cards (13 hearts)
    cards = 52
    hearts = 13
    
    # Event A: Drawing a heart first
    p_a = hearts / cards
    print(f"Probability of drawing a Heart 1st: {hearts}/{cards} = {p_a:.2f}")
    
    # Event B: Drawing a heart second (deck now has 51 cards and 12 hearts)
    cards -= 1
    hearts -= 1
    p_b_given_a = hearts / cards
    print(f"Probability of drawing a Heart 2nd (given 1st was a Heart): {hearts}/{cards} = {p_b_given_a:.2f}")

# Function to simulate Mutually Exclusive Events (e.g., Rolling a single die)
def mutually_exclusive():
    print("\n--- Mutually Exclusive Events (Single Die Roll) ---")
    # A die roll cannot be both a 2 AND an odd number (1, 3, 5) at the same time
    # Probability of A AND B is 0. 
    p_a = 1 / 6 # Rolling a 2
    p_b = 3 / 6 # Rolling an odd number (1, 3, 5)
    p_intersection = 0 
    
    print(f"Probability of rolling a 2: {p_a:.2f}")
    print(f"Probability of rolling an odd number: {p_b:.2f}")
    print(f"Probability of both at the same time: {p_intersection} (Mutually Exclusive)")

if __name__ == "__main__":
    independent_events()
    dependent_events()
    mutually_exclusive()