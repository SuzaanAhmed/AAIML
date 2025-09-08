import csv
import math
import random
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

labels_header = []
all_data = []
with open('Iris.csv', newline='') as csvf:
    reader = csv.reader(csvf, delimiter=',')
    labels_header = next(reader) 
    
    for row in reader:
        features = [float(x) for x in row[1:5]] 
        species = row[5]
        all_data.append(features + [species])


random.shuffle(all_data)

n = len(all_data)
test_size = int(0.2 * n)
train_size = n - test_size

train_set = all_data[:train_size]
test_set = all_data[train_size:]

# Separate features (X) from labels (y)
x_train = [row[:-1] for row in train_set]
y_train = [row[-1] for row in train_set]
x_test = [row[:-1] for row in test_set]
y_test = [row[-1] for row in test_set]



print(f"Train data size: {len(x_train)}")
print(f"Test data size: {len(x_test)}")

def euclidean_distance(point1, point2):
    distance = 0.0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)

def knn_classification(k, test_point, train_features, train_labels):
    distances = []
    
    for i, train_point in enumerate(train_features):
        dist = euclidean_distance(test_point, train_point)
        distances.append((dist, train_labels[i]))

    distances.sort(key=lambda x: x[0])

    neighbors = [distances[i][1] for i in range(k)]
    
    most_common = Counter(neighbors).most_common(1)
    return most_common[0][0]

def plot():
    plot_df = pd.DataFrame(all_data, columns=labels_header[1:])
    
    # Now use this DataFrame with Seaborn
    sns.pairplot(plot_df, hue='Species', markers=["o", "s", "D"])
    plt.suptitle('Pair Plot of Loaded Iris.csv Data', y=1.02)
    plt.show()


if __name__ == "__main__":
    accuracy=1.0
    error,acc=0,0
    errors=[]
    for i in range(30):
        test_val = x_test[i]
        true_label = y_test[i]
        
        K_VALUE = 5
        
        prediction = knn_classification(K_VALUE, test_val, x_train, y_train)
        
        print(f"\n--- {i} KNN Prediction ---")
        print(f"Test Point Features: {test_val}")
        print(f"True Label: {true_label}")
        print(f"Predicted Label (with K={K_VALUE}): {prediction}")
        if prediction==true_label:
            acc+=1
        else:
            error+=1
            print(f"The predicition for test point {i} is {prediction} while true prediction is {true_label}")
            errors.append(i)
    accuracy=float(acc/(acc+error))
    print(f"The accuracy is {accuracy*100}")
    print(f"False predictions at all {errors}")
    plot()
