import os

for file in os.listdir("./reports"):
    if file.endswith(".csv"):
        print(os.path.join("./reports", file))
