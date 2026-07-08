import pandas as pd
import random

machines = [
    ("M001","Boiler-1",22,"Manufacturing"),
    ("M002","Boiler-2",24,"Manufacturing"),
    ("M003","Lathe-1",30,"Manufacturing"),
    ("M004","Lathe-2",28,"Manufacturing"),
    ("M005","Compressor-1",15,"CNC"),
    ("M006","Compressor-2",17,"Testing"),
    ("M007","Cooling-1",8,"Testing"),
    ("M008","Cooling-2",9,"Maintenance"),
    ("M009","Milling-1",25,"Utilities"),
    ("M010","Milling-2",27,"Utilities"),
    ("M011","Boiler-3",21,"Manufacturing"),
    ("M012","Boiler-4",23,"Manufacturing"),
    ("M013","Lathe-3",29,"Manufacturing"),
    ("M014","Lathe-4",31,"CNC"),
    ("M015","Compressor-3",16,"CNC"),
    ("M016","Compressor-4",18,"Testing"),
    ("M017","Cooling-3",10,"Testing"),
    ("M018","Cooling-4",11,"Maintenance"),
    ("M019","Milling-3",26,"Utilities")
]

rows = []

for i in range(500):

    machine = random.choice(machines)

    machine_id = machine[0]
    machine_name = machine[1]
    rated_power = machine[2]
    department = machine[3]

    day = random.randint(1,31)

    date = f"{day:02d}-05-2026"

    shift = random.choice([
        "Morning",
        "Afternoon",
        "Night"
    ])

    hours = random.randint(4,12)

    energy = rated_power * hours

    anomaly = random.random()

    if anomaly < 0.80:

        pf = round(random.uniform(0.90,0.99),2)

        voltage = random.randint(410,420)

        status = "Normal"

    elif anomaly < 0.95:

        pf = round(random.uniform(0.85,0.89),2)

        voltage = random.randint(395,409)

        status = "Warning"

    else:

        pf = round(random.uniform(0.70,0.84),2)

        voltage = random.randint(360,394)

        status = "Critical"

    cost_per_unit = 8

    energy_cost = energy * cost_per_unit

    rows.append([
        date,
        shift,
        department,
        machine_id,
        machine_name,
        rated_power,
        hours,
        energy,
        pf,
        voltage,
        cost_per_unit,
        energy_cost,
        status
    ])

df = pd.DataFrame(rows, columns=[
    "Date",
    "Shift",
    "Department",
    "Machine_ID",
    "Machine_Name",
    "Rated_power_kW",
    "Hours_Operated",
    "Energy_kWh",
    "Power_Factor",
    "Voltage",
    "Cost_Per_Unit",
    "Energy_Cost",
    "Status"
])

df.to_csv("industrial_energy_data.csv", index=False)

print("500 rows generated successfully")