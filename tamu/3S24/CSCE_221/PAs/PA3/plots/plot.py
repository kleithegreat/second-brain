import matplotlib.pyplot as plt
import csv


def plot_results(filename, title, log_scale=False):
    sizes = []
    unsorted_times = []
    sorted_times = []
    heap_times = []

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            sizes.append(int(row[0]))
            unsorted_times.append(int(row[1]))
            sorted_times.append(int(row[2]))
            heap_times.append(int(row[3]))

    fig, ax = plt.subplots()
    ax.plot(sizes, unsorted_times, marker='o', label='Unsorted PQ')
    ax.plot(sizes, sorted_times, marker='o', label='Sorted PQ')
    ax.plot(sizes, heap_times, marker='o', label='Heap PQ')

    ax.set_xlabel('Input Size')
    ax.set_ylabel('Time (microseconds)')
    if log_scale:
        ax.set_yscale('log')
        title += ' (Log Scale)'
    ax.set_title(title)
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.grid(True)
    plt.tight_layout()
    plt.show()


plot_results('enqueue_results.csv', 'Enqueue Operation')
plot_results('enqueue_results.csv', 'Enqueue Operation', log_scale=True)
plot_results('heapsort_results.csv', 'Heap Sort Operation')
plot_results('heapsort_results.csv', 'Heap Sort Operation', log_scale=True)
