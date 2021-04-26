import  datetime
# corrent time
# x=datetime.datetime.now()
# print(x)
# # year
# print(x.year)
# #month
# print(x.month)

# create your on time
# y=datetime.datetime(2060,3,18)
# print(y)
# print(y.month)
# print(y.year)


# time formating  STRFTIME()
x=datetime.datetime.now()
# print(x.year)

# print(x.strftime("%A"))  #it will print day like monday
# print(x.strftime("%a"))  # it will print day in short like mon
# print(x.strftime("%B"))  # it will print month
# print(x.strftime("%b"))  # it will print month in short
# print(x.strftime("%p"))  # am pm
# print(x.strftime("%w")) # no of week day monday is 1
# print(x.strftime("%m"))  # MONTH
# print(x.strftime("%M"))  # MINUTE
# print(x.strftime("%y"))    # YEAR
# print(x.strftime("%H"))    # HOUR 24-HOUR CLOCK
# print(x.strftime("%I"))     # hour 12 hour clock
