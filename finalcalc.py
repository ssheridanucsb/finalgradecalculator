#!/usr/bin/python

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys


class SubGrade:

    def __init__(self, name, grade, weight):
        self.name = name
        self.grade = grade
        self.weight = weight

    def agg(self):
        return self.grade * self.weight


def grade_plotter(subgrade_list, grade_breaks):
    """takes list of partial grades for a class and plots potential final test scores vs final grade"""
    pregrade = sum([x.agg() for x in subgrade_list])
    percent_non_final= sum([x.weight for x in subgrade_list])

    percent_final = 1 - percent_non_final

    x = np.arange(101)
    y = pregrade + percent_final * x

    for g in grade_breaks:
        grade_needed = (g - pregrade) / percent_final
        print("For a " + str(g) + " you need a " + str(grade_needed))

    sns.set()
    plt.plot(x, y)
    plt.title("Final Grade vs Test Score")
    plt.xlabel("Final Test Score")
    plt.ylabel("Final Grade")
    plt.yticks(grade_breaks)
    plt.hlines(grade_breaks, 0, 100, color='red', alpha=0.5)
    plt.xticks(np.arange(101, step=5))
    plt.show()

sections = input("Excluding the final how many graded categories are there: ")

sections = int(sections)

objs = [SubGrade(i, 0, 0) for i in range(sections)]

for i in range(sections):
    n = input("Enter the name of this  category (midterm/hw/etc): ")
    g = input("Enter your average grade out of 100: ")
    w = input("Enter the weight of this category  between 0 and 1: ")
    objs[i].grade = float(g)
    objs[i].weight = float(w)
    objs[i].name = n

g = input("Enter the grade cutoffs you'd like to see separated by commas (94, 90, 88, .. etc): ")
gs = [float(i) for i in g.split(",")]

grade_plotter(objs, gs)
sys.exit()
