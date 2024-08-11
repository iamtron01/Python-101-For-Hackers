import os

os.system('cls')

philosophers = [
    "Descartes",
    "Bacon",
    "Pascal",
    "Kant"]
print(philosophers)

philosophers[3] = "Scruton"
print(philosophers)

# Aurivouir Monsieur Pascal
del philosophers[2] 
print(philosophers)

# Bienvenue Monsieur Pascal
philosophers.insert(2, "Pascal") 
print(philosophers)

philosophers.append("Leibniz")
print(philosophers)

philosophers.reverse()
print(philosophers)

mathematicians = [
    "Russell",
    "Whitehead",
    "Newton"]
print(philosophers + mathematicians)

philosophers.sort()
print(philosophers)

philosophers.sort(reverse=True)
print(philosophers)

more_philosophers = philosophers.copy()
more_philosophers.extend(["Hume", "Locke"])
print(more_philosophers)

numbers = [1, 2, 3, 4, 5]
print(numbers)

print(list(map(lambda x: x * 2, numbers)))