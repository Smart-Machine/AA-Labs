import matplotlib.pyplot as plt

def plot_graph(x, y, title):
    plt.plot(x, y, marker='o')

    plt.xlabel("Array Length")
    plt.ylabel("Time")
    plt.title(title)

    plt.show()

def print_results(x, y):
    print()
    for i in range(len(x)):
        print("| {:4} | {:.9f} |".format(x[i], y[i]))
    print()
