# pip install mysql-connector-python pandas scikit-learn numpy scipy
import pandas as pd
import mysql.connector
from sklearn.ensemble import IsolationForest
conn = mysql.connector.connect(host="your_host", user="your_user", password="your_password", database="your_db")
query = "SELECT user_id, amount, timestamp FROM transactions"
df = pd.read_sql(query, conn)
conn.close()
df["timestamp"] = pd.to_datetime(df["timestamp"]).astype(int) / 10**9
iso_forest = IsolationForest(contamination=0.05, random_state=42)
df["anomaly_score"] = iso_forest.fit_predict(df[["amount", "timestamp"]])
spam_transactions = df[df["anomaly_score"] == -1]
print(spam_transactions)
