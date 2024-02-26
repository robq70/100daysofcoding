def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# TODO: Add more code here 👇
def days_in_month(i_year, i_month):
    """Dokumentacja do funkcji"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if i_month == 2 and is_leap(i_year):
        return 29
    return month_days[i_month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Podaj rok:"))  # Enter a year
month = int(input("Podaj miesiąc:"))  # Enter a month
days = days_in_month(year, month)
print(days)



def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
  
result = outer_function(5, 10)
print(result)