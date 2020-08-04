
def peaks(data):
    return [i for i in range(1, len(data)-1) if data[i-1] < data[i] and data[i] > data[i+1]]

def valleys(data):
    return [i for i in range(1, len(data)-1) if data[i-1] > data[i] and data[i] < data[i+1]]

def chart_builder(data):
    greatest_number = max(data)
    for i in range(0, greatest_number):
        graph_list = []
        for j in range(len(data)):
            if data[j] < greatest_number:
                graph_list.append('  ')
            else:
                graph_list.append(' X')
        graph_list = ''.join(graph_list)
        print(graph_list)
        greatest_number -= 1

def peaks_and_valleys(data):
    chart_builder(data)
    print(f'The peaks were at these points {peaks(data)} and the valleys were at these points {valleys(data)}.')




data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks_and_valleys(data)

            