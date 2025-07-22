import random

# 1. Ask the user for their name
name = input("Welcome, agent. What is your real name? ")

# 3. Create two lists: adjectives and animals
adjectives = ["Handsome", "Mogging", "Tuff", "Pretty", "Fearless", "Cunning"]
animals = ["Panther", "Fox", "Eagle", "Otter", "Cobra", "Wolf"]

# 5. Generate random codename
codename = f"{random.choice(adjectives)} {random.choice(animals)}"

# 6. Generate random lucky number from 1 to 99
lucky_number = random.randint(1, 99)

# 7. Print the results
print("\n🕵️ Mission Briefing 🕵️")
print(f"Agent {name}, your codename is **{codename}**.")
print(f"Your lucky number for this mission is: {lucky_number}")
print("Good luck, agent. This message will self-destruct in 5 seconds... 💥")