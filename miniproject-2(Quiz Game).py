score = 0  

print("Welcome to my quiz game")
is_playing = input("Do you want to play this quiz game? (yes/no): ").strip().lower()

if is_playing == "yes":
    print("GREAT!!")
else:
    print("Game exited")
    quit()  


print("\n1st Question:")
a = input("What is the full form of RBI? ").strip().lower()  

if a == "reserve bank of india":
    print("✅ CORRECT ANSWER!")
    score += 1
else:
    print("❌ WRONG ANSWER! The correct answer is 'Reserve Bank of India'.")

print("Score:", score, "/3")  


print("\n2nd Question:")
a = input("What is the full form of ATM? ").strip().lower()  

if a == "automated teller machine": 
    print("✅ CORRECT ANSWER!")
    score += 1
else:
    print("❌ WRONG ANSWER! The correct answer is 'Automated Teller Machine'.")

print("Score:", score, "/3")  


print("\n3rd Question:")
a = input("What is the full form of WHO? ").strip().lower()  

if a == "world health organization": 
    print("✅ CORRECT ANSWER!")
    score += 1
else:
    print("❌ WRONG ANSWER! The correct answer is 'World Health Organization'.")

print("\nFINAL SCORE:", score, "/3")


if score == 0:
    print("😂 lol, you're too dumb!")
elif score == 1:
    print("😬 Pretty mehhh score.")
elif score == 2:
    print("😊 Good score!")
else:
    print("🔥 Excellent, smart af!")
