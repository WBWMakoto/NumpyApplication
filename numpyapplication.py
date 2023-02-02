# Simple choose random number from list with probability with 96 - x lines idk :D (by Makoto-kun#4120 | https://discord.gg/wbw)

from numpy.random import choice

# Setup environment variables (venv) and install numpy (pip install numpy)

sampleList = [69, 96]

# Put your numbers here

randomNumberList = choice(sampleList, 69, p=[0.6, 0.4])

# Run your list (sequence , count answer, p = probability of each number)

print(randomNumberList)
