import csv
import matplotlib.pyplot as plt
import math
labels = []
values = []

with open('Iris.csv', newline='') as csvf:
    reader = csv.reader(csvf, delimiter=',')
    
    labels.append(next(reader))  # Reads the header row
    c=0
    for row in reader:
        values.append(row)  
        
n=len(values)

test_size=int(.2*n)
train_size=n-test_size

train_data=values[:train_size]
test_data=values[train_size:]
print(f"Train data size:{len(train_data)}")
print(f"Train data size:{len(test_data)}")

plt.scatter(
    [float((i[1]+i[2])/2) for i in train_data if i[5] == "Iris-setosa"],  
    [float((i[3]+i[4])/2) for i in train_data if i[5] == "Iris-setosa"],  
    color='red',
    label='iris-setosa',
    marker='x'  
)

plt.scatter(
    [float((i[1]+i[2])/2) for i in train_data if i[5] == "Iris-versicolor"],  
    [float((i[3]+i[4])/2) for i in train_data if i[5] == "Iris-versicolor"],  
    color='Blue',
    label='iris-Virginica',
    marker='+'  
)
plt.scatter(
    [float((i[1]+i[2])/2) for i in train_data if i[5] == "Iris-virginica"],  
    [float((i[3]+i[4])/2) for i in train_data if i[5] == "Iris-virginica"],  
    color='green',
    label='iris-Versicolor',
    marker='*'  
)

plt.xlabel(labels[0][2])
plt.ylabel(labels[0][3])
plt.title('Iris datasets: Iris-virginica, Iris-versicolor, Iris-setosa')
plt.legend()
plt.grid(True)
plt.show()


def euclidean_distance(point1, point2):
    distance = 0
    for i in range(len(train_data)):
        for j in range(1,):
            distance=math.sqrt(point1-point2)**2