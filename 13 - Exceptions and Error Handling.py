def division_total(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError(
            "You can't divide by zero!")
    return dividend / divisor
try:
    print(division_total(15, 0))
except ZeroDivisionError as exception:
    print(exception)

print("--------------------")

def division_total(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        return "You can't divide by zero!"
print(division_total(15, 0))

print("--------------------")

def division_total(dividend, divisor):
    if divisor == 0:
        return None
    return dividend / divisor
print(division_total(15, 0))
print(division_total(15, 3))

print("--------------------")

def division_total(dividend, divisor):
    match divisor:
        case 0:
            return None
        case _:
            return dividend / divisor
print(division_total(15, 0))
print(division_total(15, 3))