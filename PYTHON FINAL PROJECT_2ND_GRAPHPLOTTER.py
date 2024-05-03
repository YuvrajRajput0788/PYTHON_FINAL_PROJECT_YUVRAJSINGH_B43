# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 08:21:09 2024

@author: sarit
"""

import matplotlib.pyplot as plt

def plot_graph(x, y, graph_type):
    if graph_type == 1:
        plt.bar(x, y)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Bar Graph')
    elif graph_type == 2:
        plt.scatter(x, y)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Scatter Plot')
    elif graph_type == 3:
        plt.barh(x, y)
        plt.xlabel('Y-axis')
        plt.ylabel('X-axis')
        plt.title('Horizontal Bar Graph')
    elif graph_type == 4:
        plt.hist(y, bins=10)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Histogram')
    plt.show()

def main():
    data = []
    labels = []

    num_points = int(input("Enter the number of data points: "))

    for i in range(num_points):
        data.append(float(input(f"Enter data point {i + 1}: ")))

    for i in range(num_points):
        labels.append(input(f"Enter label for data point {i + 1}: "))

    print("Choose the type of graph:")
    print("1. Bar Graph")
    print("2. Scatter Plot")
    print("3. Horizontal Bar Graph")
    print("4. Histogram")
    graph_type = int(input("Enter your choice (1/2/3/4): "))

    plot_graph(labels, data, graph_type)

if __name__ == "__main__":
    main()