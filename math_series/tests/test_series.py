from math_series.series import fibonacci, lucas, sum_series

def test_fibonacci():

    expected1 = 0
    expected2 = 1
    expected3 = 1
    expected4 = 55

    actual1=fibonacci(0)
    actual2=fibonacci(1)
    actual3=fibonacci(2)
    actual4=fibonacci(10)

    assert actual1 == expected1
    assert actual2 == expected2
    assert actual3 == expected3
    assert actual4 == expected4


def test_lucas():

    expected1 = 2
    expected2 = 1
    expected3 = 3
    expected4 = 123

    actual1=lucas(0)
    actual2=lucas(1)
    actual3=lucas(2)
    actual4=lucas(10)

    assert actual1 == expected1
    assert actual2 == expected2
    assert actual3 == expected3
    assert actual4 == expected4


def test_sum():

    expected1 = 0
    expected2 = 1
    expected3 = 1
    expected4 = 123

    actual1=sum_series(0)
    actual2=sum_series(1,2,1)
    actual3=sum_series(2)
    actual4=sum_series(10,2,1)

    assert actual1 == expected1
    assert actual2 == expected2
    assert actual3 == expected3
    assert actual4 == expected4