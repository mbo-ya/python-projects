# Ask the user what's on their mind, then count the number of words in their
# response and print that as an output.
s = input("What's on your mind today?:\n")
st = s.split()          # split the sentence into individual words
print(f"Oh nice, you just told me what's on your mind in {len(st)} words!")
