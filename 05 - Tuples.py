currencies = ('EUR', 'USD', 'JPY', 'GBP')
print(currencies)

europe, america, japan, britain = currencies
print(europe)
print(america)
print(japan)
print(britain)

print(europe in currencies)

print(currencies[-1])
print(currencies[-2])

print(currencies[:2])

print(currencies[1])
print(currencies.index('USD'))

repeat = ('EUR',) *4
print(repeat)

mixed = ('EUR', 1, ("USD", 2))
print(mixed)

combined = currencies + repeat
print(combined)