import statistics

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
    minimum = min(float_list)
    maximum = max(float_list)
    return minimum, maximum

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature(float_list):
    list = sorted(float_list)
    median_val = statistics.median(float_list)
    print("The median value is: " + str(median_val))
    return median_val

def main():
    display_main_menu()
    y = get_user_input()
    average = calc_average(y)
    print("Average = " + str(average))
    min, max = find_min_max(y)
    print("Minimum = " + str(min) + ", Maximum = " + str(max))
    calc_median_temperature(y)
if __name__ == "__main__":
    main()

