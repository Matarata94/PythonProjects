import pandas as pd

#Reading from CSV FIle
csv = pd.read_csv('CSV_Working/test.csv', names=['Matarata','Matara','Mata','Ma'], header=0, usecols=[2,3])
print(csv)
print("----------------------------------------")
#Writing to CSV file
csv.to_csv('CSV_Working/test2.csv')
print(pd.read_csv('CSV_Working/test2.csv'))
print("----------------------------------------")
users = pd.read_csv('CSV_Working/u.user', sep='|', names=["User ID", "Age", "Gender", "Occupation", "Zip Code"])
print(users.set_index("User ID").head(6))
print("----------------------------------------")
print(users.set_index("User ID").tail(4))
print("----------------------------------------")
print(users["Gender"].head(5))
print("----------------------------------------")
print(users[users.Age > 25].set_index("User ID").head())
print("----------------------------------------")
print(users.dtypes)
print("----------------------------------------")
print(users.describe())