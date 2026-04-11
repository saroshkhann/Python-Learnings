import numpy as np

names= np.array(["Ali", "Sara", "Ahmed", "John", "Zara"])
marks = np.array([
    [78, 70, 75],   # Ali
    [92, 95, 89],   # Sara
    [85, 80, 82],   # Ahmed
    [60, 65, 70],   # John
    [88, 90, 85]    # Zara
])

total = marks.sum(axis = 1)
average = marks.mean(axis=1)

print("Total:", total)
print("Average:", average)

grades = []

for avg in average:
    if avg >= 85:
        grades.append("A")
    elif avg >= 70:
        grades.append("B")
    elif avg >= 50:
        grades.append("C")
    else:
        grades.append("F")

grades = np.array(grades)
print(grades)

rank_indices = np.argsort(-average)
print("Rank order (index):", rank_indices)

print("\nRanking:")
for i in rank_indices:
    print(names[i], "-", average[i])

top_students = names[average >= 85]
print("Top students:", top_students)
