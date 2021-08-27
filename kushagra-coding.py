import pandas


def moving_average(series, n):
#calculate moving average
    outcome=pandas.Series(series).rolling(window=n).mean().iloc[n-1:].values
    return print(outcome)

#testing array
x = [50, 55, 36, 49, 84, 75, 101, 86, 80, 104]

#testing the function
moving_average(x,5)
#array([47, 46.67, 56.33, 69.33, 86.67, 87.33, 89, 90])
