print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67,32): ")

def get_user_input():
    user_input = input()
    string_list = user_input.split(',')
    float_list = [float(num) for num in string_list]
    print("List of numbers:", float_list)
    return float_list

def calc_average(float_list):
    average = sum(float_list) / len(float_list)
    return average

def find_min_max(float_list):
    x = min(float_list)
    y = max(float_list)
    print("Minimum value is: " + str(x))
    print("Maxmimum value is: " + str(y))

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")

display_main_menu()
y = get_user_input()
average = calc_average(y)
print("Average = " + str(average))
find_min_max(y)

