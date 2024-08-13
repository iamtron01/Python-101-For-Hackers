inventors = {
    "Pascal":"Calculator",
    "Edison":"light bulb",
    "Wright":"Airplane:"}

print(inventors)
print(inventors["Edison"])

print(inventors.keys())
print(inventors.values())

inventors["Marconi"] = "Radio"
print(inventors)

inventors["Edison"] = "Phonograph"

del inventors["Wright"]
print(inventors)

inventors.pop("Marconi")
print(inventors)