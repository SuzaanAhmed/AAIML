import csv
import matplotlib.pyplot as plt
import math
import seaborn as sns

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
print(f"Test data size:{len(test_data)}")

def plot():
    iris_df = sns.load_dataset('iris')

    sns.pairplot(iris_df, hue='species', markers=["o", "s", "D"])

    plt.suptitle('Pair Plot of the Iris Dataset', y=1.02) # Add a title above the plot
    plt.show()


# math.exp(1)
def euclidean_distance(point1, point2):
    return math.sqrt(math.exp(point1-point2,2))

if __name__=="__main__":
    print(f"Prediction for {labels[0][0]}:{test_data[0][0]}")