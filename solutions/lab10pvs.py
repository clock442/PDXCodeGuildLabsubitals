
def peaks(data):
    return [i for i in range(1, len(data)-1) if data[i-1] < data[i] and data[i] > data[i+1]]

def valleys(data):
    return [i for i in range(1, len(data)-1) if data[i-1] > data[i] and data[i] < data[i+1]]

def peaks_and_valleys(data):
    print(f'The peaks were at these points {peaks(data)} and the valleys were at these points {valleys(data)}.')



data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks_and_valleys(data)

            