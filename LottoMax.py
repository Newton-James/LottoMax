import random

# Random Number Generator Function
def generate_ticket(minNum, maxNum, howManyNum):
    return set(random.sample(range(minNum, maxNum+1), howManyNum))

# ---
# Lotto Max
print("\nLotto Max")

# Define Lotto Max criteria
lottoMaxminNum = 1
lottoMaxmaxNum = 50
lottoMaxHowManyNum = 7

# Generate 6 unique winning numbers between 1 and 50
#winning_numbers = set(random.sample(range(1, 51), 7))
winning_numbers = generate_ticket(lottoMaxminNum, lottoMaxmaxNum, lottoMaxHowManyNum)

# Print the winning numbers
print("\nWinning Numbers:")
for i, num in enumerate(winning_numbers, start=1):
    print(f"Pick {i}: {num}")

# Generate 7 unique player numbers between 1 and 50
player_numbers = generate_ticket(lottoMaxminNum, lottoMaxmaxNum, lottoMaxHowManyNum)
# Keep track of how many attepmts the player needs win the jackpot
attempt = 1
# Loop the ticket generation for player until player ticket number match winning numbers
while player_numbers != winning_numbers:
    # Generate 7 unique player numbers between 1 and 50
    player_numbers = generate_ticket(lottoMaxminNum, lottoMaxmaxNum, lottoMaxHowManyNum)
    attempt += 1

    # Optional: Show progress every million attempts
    #if attempt % 1_000_000 == 0:
    #    print(f"{attempt:,} attempts... still trying.")

# Player has finally won!
print("\nPlayer has won the Lotto Max Jackpot!")

# Print the player's numbers
print("\nPlayer's Numbers:")
for i, num in enumerate(player_numbers, start=1):
    print(f"Pick {i}: {num}")

# Print the number of attempts taken to win the jackpot
print("\nTotal number of Attempts: ", attempt)
print("\n---")
# ---
#