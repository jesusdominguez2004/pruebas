# Semana 11 | Algoritmos 1
from random import randint

emojis = ["💙", "💛", "🤖", "🐍"]

for i in range(100):
    x = randint(0, len(emojis) - 1)
    print(emojis[x], end=" ")