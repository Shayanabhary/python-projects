
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import hlines

# Read CSV (convert into a dataframe)
df = pd.read_csv(r"C:/Users/SHAYAN/Desktop/BTC-USD.csv")

# Display basic information about the dataset
days_count = len(df.index)
print(f"days count = {days_count}")
print("\n")
df["Date"] = pd.to_datetime(df["Date"])  # convert date column in-place

# Use pandas methods directly for clarity and precision
# stats = df.describe()

df.info()
print("\n")

# Means
open_mean = df["Open"].mean()
close_mean = df["Close"].mean()
volume_mean = df["Volume"].mean()
high_mean = df["High"].mean()
low_mean = df["Low"].mean()
print("open mean =", open_mean)
print("close mean =", close_mean)
print("volume mean =", volume_mean)
print("high mean =", high_mean)
print("low mean =", low_mean)
print()

# Standard deviations
open_std = df["Open"].std()
close_std = df["Close"].std()
volume_std = df["Volume"].std()
high_std = df["High"].std()
low_std = df["Low"].std()
std = {
    "open-std": open_std,
    "close-std": close_std,
    "volume-std": volume_std,
    "high-std": high_std,
    "low-std": low_std,
}
for key, value in std.items():
    print(f"{key}  {value}")
print()

# Variances
open_var = df["Open"].var()
close_var = df["Close"].var()
volume_var = df["Volume"].var()
high_var = df["High"].var()
low_var = df["Low"].var()
var = {
    "open-var": open_var,
    "close-var": close_var,
    "volume-var": volume_var,
    "high-var": high_var,
    "low-var": low_var,
}
for key, value in var.items():
    print(f"{key} {value}")
print()

# Medians
open_median = df["Open"].median()
close_median = df["Close"].median()
volume_median = df["Volume"].median()
high_median = df["High"].median()
low_median = df["Low"].median()
median = {
    "open-median": open_median,
    "close-median": close_median,
    "volume-median": volume_median,
    "high-median": high_median,
    "low-median": low_median,
}
for key, value in median.items():
    print(f"{key}  {value}")
print()

open_mode = df["Open"].mode()[0]
close_mode = df["Close"].mode()[0]
volume_mode = df["Volume"].mode()[0]
high_mode = df["High"].mode()[0]
low_mode = df["Low"].mode()[0]
mod = {
    "open-mode": open_mode,
    "close-mode": close_mode,
    "volume-mode": volume_mode,
    "high-mode": high_mode,
    "low-mode": low_mode,
}
for key, value in mod.items():
    print(f"{key}  {value}")
print()
# plotting data
plt.plot(df["Open"] , label="Open price" , color="blue"  )
plt.plot(open_mean, label="Open mean price" , color="green" )
plt.plot(open_std, label="Open std price" , color="red" )
plt.legend()
plt.show()
# plt.plot(df["Close"] , label="Close" , color="red" , linestyle="-" )
# plt.plot(close_mean, label="Close mean price" , color="green" , linestyle="-" )
# plt.plot(close_std, label="Close std price" , color=" blue" , linestyle="-" )
# plt.legend()
# plt.show()
# plt.plot(df["Volume"], label="Volume" , color="green" , linestyle="-" )
# plt.plot(volume_mean, label="Volume mean price" , color="yellow" , linestyle="-" )
# plt.plot(volume_std, label="Volume std price" , color="red" , linestyle="-" )
# plt.legend()
# plt.show()
# plt.plot(df["High"], label="High" , color="yellow" , linestyle="-" )
# plt.plot(high_mean, label="High mean price" , color="green" , linestyle="-" )
# plt.plot(high_std, label="High std price" , color="blue" , linestyle="-" )
# plt.legend()
# plt.show()
# plt.plot(df["Low"] , label="Low" , color="blue" , linestyle="-" )
# plt.plot(low_mean, label="Low mean price" , color="green" , linestyle="-" )
# plt.plot(low_std, label="Low std price" , color="red" , linestyle="-" )
# plt.legend()
# plt.show()


