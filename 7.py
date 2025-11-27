'''SVD algorithm and Surprise library to predict missing reviews in movielens.'''
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import accuracy

# -----------------------------
# Load MovieLens 100k dataset
# -----------------------------
data = Dataset.load_builtin('ml-100k')

# Split into train and test
trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

# -----------------------------
# SVD Matrix Factorization Model
# -----------------------------
model = SVD()   # default SVD parameters

# Train the model
model.fit(trainset)

# Predict on the test set
predictions = model.test(testset)

# -----------------------------
# Evaluate Using RMSE
# -----------------------------
rmse = accuracy.rmse(predictions)
print("Final RMSE:", rmse)
