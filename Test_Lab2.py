import Lab2

def test_find_min_max():
    user_input = [12,3,5,10,7]
    result_min, result_max = Lab2.find_min_max(user_input)
    assert (result_min == 3 and result_max == 12)
def test_calc_average():
    user_input = [5,10,15]
    result = Lab2.calc_average(user_input)
    assert (result == 10)
def test_calc_median_temperature():
    user_input = [5,10,15,20]
    result = Lab2.calc_median_temperature(user_input)
    assert (result == 12.5)
