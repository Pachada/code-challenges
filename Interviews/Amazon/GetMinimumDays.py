"""
Given a list of packages to deliver, but you can only deliver the same number of packages fro the different warehouse
return the minimum number of days nedded to deliver all the packages


"""

def get_minimum_days(warehouse: list[int]):
    warehouse.sort()
    
    min_days = 0
    last_value = 0
    
    for  value in warehouse:
        if value != last_value:
            min_days += 1
            last_value = value
    
    return min_days


warehouse = [4,2,3,2]
print(get_minimum_days(warehouse))
warehouse = [3,3,3,3,3,3,3]
print(get_minimum_days(warehouse))