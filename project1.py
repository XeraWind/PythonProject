import time
import random

choice = random.choice("a", "b","c", "d")

match input("Pick a, b, c, or d: "):
    case "a":
        print("A")
    case "b":
        print("B")
    case "c":
        print("C")
    case "d":
        print("D")