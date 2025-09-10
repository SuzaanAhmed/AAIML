import csv
import math
import random
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class KNN:
    def __init__(self, k):
        self.labels_header = []
        self.all_data = []
        self.K_VALUE = k

        with open("iris.csv", newline='') as csvf:
            reader = csv.reader(csvf, delimiter=',')
            self.labels_header = next(reader)

            for row in reader:
                features = [float(x) for x in row[1:5]]
                species = row[5]
                self.all_data.append(features + [species])
        
        random.shuffle(self.all_data)
        test_size = int(len(self.all_data) * 0.2)

        train_set = self.all_data[test_size:]
        test_set = self.all_data[:test_size]

        self.x_train = [row[:-1] for row in train_set]
        self.y_train = [row[-1] for row in train_set]
        self.x_test = [row[:-1] for row in test_set]
        self.y_test = [row[-1] for row in test_set]

    @staticmethod
    def euclidean_distance(point1, point2):
        distance = 0.0
        for i in range(len(point1)):
            distance += (point1[i] - point2[i]) ** 2
        return math.sqrt(distance)

    def predict_one(self, test_point):
        distances = []
        for i, train_point in enumerate(self.x_train):
            dist = self.euclidean_distance(test_point, train_point)
            
            distances.append((dist, self.y_train[i]))

        distances.sort(key=lambda x: x[0])
        neighbors = [distances[i][1] for i in range(self.K_VALUE)]
        
        most_common = Counter(neighbors).most_common(1)
        return most_common[0][0]

    def plot(self):        
        plot_df = pd.DataFrame(self.all_data, columns=self.labels_header[1:])
        
        sns.pairplot(plot_df, hue='Species', markers=["o", "s", "D"])
        plt.suptitle('Pair Plot of Loaded Iris.csv Data', y=1.02)
        plt.show()

    def classify_and_evaluate(self):
        correct_predictions = 0
        misclassified_indices = []

        for i, test_point in enumerate(self.x_test):
            true_label = self.y_test[i]
            prediction = self.predict_one(test_point)
            
            if prediction == true_label:
                correct_predictions += 1
            else:
                misclassified_indices.append(i)
                print(f"Misclassified sample {i}: Predicted '{prediction}', True Label was '{true_label}'")
        
        accuracy = (correct_predictions / len(self.x_test)) * 100
        print("\n--- Evaluation Summary ---")
        print(f"Total Test Samples: {len(self.x_test)}")
        print(f"Correct Predictions: {correct_predictions}")
        print(f"Final Accuracy: {accuracy:.2f}%")
        print(f"Indices of misclassified samples: {misclassified_indices}")

if __name__ == "__main__":
    knn = KNN(k=5)
    knn.classify_and_evaluate()