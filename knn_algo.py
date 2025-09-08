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
print(f"Train data size:{len(test_data)}")
iris_df = sns.load_dataset('iris')

# --- 2. Create the Pair Plot ---
# This single line of code generates the entire grid of plots.
# 'hue="species"' tells Seaborn to color the data points based on the flower species,
# which allows us to see the relationships for each class.
sns.pairplot(iris_df, hue='species', markers=["o", "s", "D"])

# --- 3. Display the Plot ---
plt.suptitle('Pair Plot of the Iris Dataset', y=1.02) # Add a title above the plot
plt.show()



def euclidean_distance(point1, point2):
    distance = 0
    for i in range(len(train_data)):
        for j in range(1,):
            distance=math.sqrt(point1-point2)**2