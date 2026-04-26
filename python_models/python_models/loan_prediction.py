import math
import random

# 1. Generate synthetic dataset (Pure Python implementation)
# Features: [Income, Credit_Score, Employment_Status, Loan_Amount]
# Employment Encoding: 0 = Unemployed, 1 = Self-Employed, 2 = Employed
def generate_data(num_samples=200):
    random.seed(42)
    dataset = []
    for _ in range(num_samples):
        income = random.randint(20000, 120000)
        credit = random.randint(300, 850)
        emp = random.choice([0, 1, 2])
        loan = random.randint(5000, 50000)
        
        # Create a logical rule for the synthetic target so the model can learn
        # Higher income, higher credit, and stable employment increase approval odds
        score = (income / 120000) * 0.4 + (credit / 850) * 0.4 + (emp / 2) * 0.2
        approved = 1 if score > 0.55 else 0 
        
        dataset.append(([income, credit, emp, loan], approved))
    return dataset

data = generate_data()

# Split into Training (80%) and Testing (20%) sets
train_size = int(len(data) * 0.8)
train_data = data[:train_size]
test_data = data[train_size:]

# 2. Custom K-Nearest Neighbors (KNN) Classifier
def euclidean_distance(row1, row2):
    # Normalize data on the fly so large numbers (like Income) don't overpower small numbers (like Emp Status)
    max_vals = [120000, 850, 2, 50000]
    distance = 0.0
    for i in range(len(row1)):
        norm1 = row1[i] / max_vals[i]
        norm2 = row2[i] / max_vals[i]
        distance += (norm1 - norm2) ** 2
    return math.sqrt(distance)

def predict_knn(train_set, test_row, k=5):
    distances = []
    for train_row, label in train_set:
        dist = euclidean_distance(test_row, train_row)
        distances.append((dist, label))
    
    # Sort by distance (closest neighbors first)
    distances.sort(key=lambda x: x[0])
    neighbors = distances[:k]
    
    # Majority vote
    votes = [label for _, label in neighbors]
    prediction = max(set(votes), key=votes.count)
    return prediction

# 3. Model Evaluation
print("--- Loan Approval Prediction System (Pure Python ML) ---")
correct = 0
for test_row, actual_label in test_data:
    prediction = predict_knn(train_data, test_row, k=5)
    if prediction == actual_label:
        correct += 1

accuracy = correct / float(len(test_data))
print(f"Model Accuracy (KNN Classification): {accuracy * 100:.2f}%\n")

# 4. Predict for a new test applicant
print("--- Testing a New Applicant ---")
test_income = 75000
test_credit = 720
test_emp_str = 'Employed'
test_emp_encoded = 2 # 2 maps to Employed
test_loan = 20000

print(f"Applicant Details: Income=${test_income}, Credit={test_credit}, Status={test_emp_str}, Loan=${test_loan}")

# Group applicant features into a list
new_applicant_features = [test_income, test_credit, test_emp_encoded, test_loan]

# Run prediction
result = predict_knn(train_data, new_applicant_features, k=5)

if result == 1:
    print("Result: Loan APPROVED")
else:
    print("Result: Loan REJECTED")
