# Spam-Transaction-Detection-using-Isolation-Forest
Spam Transaction Detection using Isolation Forest project using MySQL and Python:

# 🚨 Spam Transaction Detection using Isolation Forest

This project detects potentially spam or anomalous financial transactions using the **Isolation Forest** algorithm. It connects to a MySQL database, retrieves transaction records, and flags suspicious activity based on transaction amount and timestamp.

## 📌 Features

- Connects to a MySQL database and reads transaction data using SQL.
- Uses `IsolationForest` from `scikit-learn` for unsupervised anomaly detection.
- Identifies potentially spammy or fraudulent transactions.
- Outputs suspicious transactions for further investigation.

## 🛠️ Tech Stack

- **Python 3**
- **MySQL**
- **Pandas**
- **Scikit-learn**
- **MySQL Connector**

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/spam-transaction-detector.git
   cd spam-transaction-detector
   
2. **Install required libraries**

 ```bash
pip install mysql-connector-python pandas scikit-learn numpy scipy

3. **Configure Database Credentials**

Open the script and replace:
python
conn = mysql.connector.connect(
    host="your_host",
    user="your_user",
    password="your_password",
    database="your_db"
)

🧪 How It Works
1. Fetches data from transactions table with user_id, amount, and timestamp.
2. Converts timestamp to numeric format (Unix epoch).
3. Trains an Isolation Forest model using amount and timestamp.
4. Predicts anomalies: -1 for spam, 1 for normal.
5. Filters and prints suspicious transactions.

🚀 Run the Script
 ```bash
python detect_spam_transactions.py

📊 Sample Output

   user_id  amount     timestamp  anomaly_score
3        4  9500.0  1.697515e+09             -1
7        8  12000.0 1.697530e+09             -1

📁 File Structure
.
├── detect_spam_transactions.py   # Main detection script
└── README.md                     # Project overview

✅ Example SQL Table (for testing)
sql

CREATE TABLE transactions (
    user_id INT,
    amount FLOAT,
    timestamp DATETIME
);

📌 Notes
1. This is an unsupervised model — no labels required.
2. contamination=0.05 assumes 5% of transactions are spammy. Adjust as needed.
3. Ensure the timestamp format in your DB is convertible by pandas.to_datetime().
