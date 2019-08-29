import pandas as pd
session = 2
address = 11
zero = 18
data = 

cycle_fail = [50895, 50920, 50945, 50970, 50995, 51145, 51245, 51570, 51595, 51620, 51645, 51670, 51720, 51745, 51770, 51795, 51845, 51870, 52370]

cycle_list = [int((52395-x)/25) for x in cycle_fail ]
cycle_list.reverse()
print(cycle_list)