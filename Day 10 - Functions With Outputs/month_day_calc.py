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

# This "days_in_month" function is the only one that was built by me from the code exercise
# It utilized the above function and variables below to calculate days in a month
# Could have simplified this even further to just "return month_days[month - 1]" after testing for leap year
  
def days_in_month(y, m):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if month_days[m-1] == 28 and is_leap(y) == True:
      return 29
  elif month_days[m-1] == 28 and is_leap(y) == False:
      return 28
  elif month_days[m - 1] == 31:
    return 31
  else:
    return 30
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


