import os
import pandas as pd
import sys
import time

selected_columns = ['VendorID', 'payment_type', 'tip_amount']

start = time.perf_counter()
df_parquet = pd.read_parquet("yellow_tripdata_2023-01.parquet")  # , columns=selected_columns)
end = time.perf_counter()
print(end - start)
# print(df_parquet)
print(df_parquet.columns)

if not os.path.exists("./yellow_tripdata_2023-01.csv"):
    df_parquet.to_csv("yellow_tripdata_2023-01.csv")

start = time.perf_counter()
df_csv = pd.read_csv("yellow_tripdata_2023-01.csv")  # , usecols=selected_columns)
end = time.perf_counter()
print(end - start)

print(str(round(sys.getsizeof(df_parquet) / (1024 * 1024))) + " Mb")
print(str(round(sys.getsizeof(df_csv) / (1024 * 1024))) + " Mb")

#Convert a csv to parquet
# df_parquet2 = df_csv.to_parquet("yellow_tripdata_2023-01_duplicate.parquet")
