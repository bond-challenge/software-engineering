import pandas


def moving_average(series, n):
#calculate moving average
    outcome=pandas.Series(series).rolling(window=n).mean().iloc[n-1:].values
    return print(outcome)

#testing array
x = [87, 56, 16, 97, 45, 75, 41, 863, 90.2, 4]

#testing the function with window of 5, feel free to change the window size
moving_average(x,5)
