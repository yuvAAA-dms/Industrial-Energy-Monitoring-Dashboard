import pandas as pd

# Load Dataset
df = pd.read_csv("industrial_energy_data.csv")
print(df.columns.tolist())

# BASIC DATA PREVIEW

print("FIRST 5 RECORDS:")
print(df.head())

# TOTAL ENERGY CONSUMED

print("\nTOTAL ENERGY CONSUMED (kWh):")
print(df["Energy_kWh"].sum())

# AVERAGE POWER FACTOR

print("\nAVERAGE POWER FACTOR:")
print(round(df["Power_Factor"].mean(), 2))

# MAXIMUM ENERGY CONSUMPTION

print("\nMAXIMUM ENERGY CONSUMPTION:")
print(df["Energy_kWh"].max())

# TOTAL ENERGY COST

print("\nTOTAL ENERGY COST:")
print(df["Energy_Cost"].sum())

# DEPARTMENT WISE CONSUMPTION

print("\nDEPARTMENT WISE ENERGY CONSUMPTION:")
print(df.groupby("Department")["Energy_kWh"].sum())

# MACHINE WISE CONSUMPTION

print("\nMACHINE WISE ENERGY CONSUMPTION:")
print(df.groupby("Machine_Name")["Energy_kWh"].sum())

# SHIFT WISE CONSUMPTION

print("\nSHIFT WISE ENERGY CONSUMPTION:")
print(df.groupby("Shift")["Energy_kWh"].sum())

# LOW POWER FACTOR MACHINES

low_pf = df[df["Power_Factor"] < 0.85]

print("\nLOW POWER FACTOR MACHINES:")
print(low_pf[["Machine_Name","Power_Factor","Energy_kWh"]])

# LOW VOLTAGE MACHINES

low_voltage = df[df["Voltage"] < 405]

print("\nLOW VOLTAGE MACHINES:")
print(low_voltage[["Machine_Name","Voltage","Energy_kWh"]])

# ANOMALY DETECTION

anomalies = df[
    (df["Power_Factor"] < 0.85) |
    (df["Voltage"] < 405)
]

print("\nANOMALY RECORDS:")
print(anomalies[[
    "Machine_Name",
    "Department",
    "Energy_kWh",
    "Power_Factor",
    "Voltage"
]])

# TOP ENERGY CONSUMING MACHINES😭

print("\nTOP 5 ENERGY CONSUMING MACHINES: ")

top_machines = (
    df.groupby("Machine_Name")["Energy_kWh"].sum().sort_values(ascending=False).head(5))
print(top_machines)

# HIGHEST COST MACHINE

highest_cost = df.loc[df["Energy_Cost"].idxmax()]

print("\nHIGHEST COST MACHINE:")
print(highest_cost[["Machine_Name","Energy_Cost"]])

# STATUS COUNT ANALYSIS

print("\nSTATUS COUNT:")
print(df["Status"].value_counts())

# DEPT WISE COST

print("\nDEPARTMENT COST:")
print(df.groupby("Department")["Energy_Cost"].sum())

# HIGHEST ENERGY CONSUMING DEPT

highest_dept = df.groupby("Department")["Energy_kWh"].sum().idxmax()

print("\nHIGHEST ENERGY CONSUMING DEPARTMENT:")
print(highest_dept)

# HIGHEST ENERGY CONSUMING SHIFT

highest_shift = df.groupby("Shift")["Energy_kWh"].sum().idxmax()

print("\nHIGHEST ENERGY CONSUMING SHIFT:")
print(highest_shift)

# MACHINE EFFICIENCY ANALYSIS

df["Energy_per_Hour"] = df["Energy_kWh"] / df["Hours_Operated"]

print("\nTOP 5 LEAST EFFICIENT MACHINES:")

print(
    df.groupby("Machine_Name")["Energy_per_Hour"]
      .mean()
      .sort_values(ascending=False)
      .head(5)
)

# CRITICAL MACHINES

critical = df[df["Status"]=="Critical"]

print("\nCRITICAL MACHINES:")
print(
    critical[
        ["Machine_Name",
         "Department",
         "Energy_kWh",
         "Power_Factor",
         "Voltage"]
    ]
)