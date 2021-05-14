def movingAverage(numbers, window_size):
    moving_averages = []
    for i in range(0,len(numbers) - window_size + 1):
        this_window = numbers[i: i + window_size]
        window_average = sum(this_window) / window_size
        moving_averages.append(window_average)
        i += 1
    print(moving_averages)

if __name__ == "__main__":
    numbers = [1, 2, 3, 7, 9, 5, 7, 6, 6, 6, 6]
    window_size = 5
    movingAverage(numbers, window_size)