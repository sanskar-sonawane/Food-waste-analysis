import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("PG WASTE FOOD ANALYZER STARTED")

df = pd.read_csv("DATA.CSV")


print(df.head())

print(df.shape)


df.info()


print(df.isnull().sum())


print(df.duplicated().sum())


print(df.dtypes)


df["Date"] = pd.to_datetime(df["Date"])

print(df.describe())

df["Waste_Percentage"] = (
    df["Waste_Qty_kg"] / df["Prepared_Qty_kg"]
) * 100

print(df.head())

meal_waste = df.groupby("Meal")["Waste_Qty_kg"].mean() #Breakfast ki rows ek group, Lunch ki rows ek group, Dinner ki rows ek group.And only waste column 

print("\nAverage waste by meal:")
print(meal_waste)


meal_waste = meal_waste.sort_values(ascending=False)  #meals order fixed nahi hai. Ab hum highest waste → lowest waste arrange karenge.

print("\nMeal-wise waste from highest to lowest:")
print(meal_waste)

total_waste = df["Waste_Qty_kg"].sum() #Waste wali poori column. aur sabo add krenge

print("\nTotal food waste:")
print(total_waste, "kg")

average_waste = df["Waste_Qty_kg"].mean()

print("\nAverage food waste:")
print(average_waste, "kg")

food_waste = df.groupby("Food_Item")["Waste_Qty_kg"].mean()

print("\nAverage waste by food item:")
print(food_waste)


day_waste = df.groupby("Day")["Waste_Qty_kg"].mean()   #har din kitna waste hua hai uska hisab 

print("\nAverage waste by day:")
print(day_waste)



df["Waste_Per_Person"] = (        # Step 17: Waste per person
    df["Waste_Qty_kg"] / df["People"]
)

print("\nWaste per person:")
print(df[["Meal", "Food_Item", "Waste_Qty_kg", "People", "Waste_Per_Person"]])



calculated_waste = (                        #  Check data consistency
    df["Prepared_Qty_kg"] - df["Consumed_Qty_kg"]
)

df["Calculated_Waste"] = calculated_waste

print("\nData consistency check:")
print(
    df[
        [
            "Prepared_Qty_kg",
            "Consumed_Qty_kg",
            "Waste_Qty_kg",
            "Calculated_Waste"
        ]
    ]
)




consistent_rows = (                  # Check consistency
    df["Waste_Qty_kg"] == df["Calculated_Waste"]
)

print("\nConsistency check:")
print(consistent_rows)

print("\nNumber of inconsistent rows:")
print((~consistent_rows).sum())


# Visualize average waste by meal

plt.figure(figsize=(8, 5))

plt.bar(meal_waste.index, meal_waste.values)

plt.xlabel("Meal")
plt.ylabel("Average Waste (kg)")
plt.title("Average Food Waste by Meal")

plt.show()
 
daily_waste = df.groupby("Date")["Waste_Qty_kg"].sum()

plt.figure(figsize=(8, 5))

plt.plot(daily_waste.index, daily_waste.values, marker="o")

plt.xlabel("Date")
plt.ylabel("Total Waste (kg)")
plt.title("Daily Food Waste Trend")

plt.xticks(rotation=45)

plt.show()

daily_waste = df.groupby("Date")["Waste_Qty_kg"].sum()

plt.figure(figsize=(8, 5))

plt.plot(daily_waste.index, daily_waste.values, marker="o")

plt.xlabel("Date")
plt.ylabel("Total Waste (kg)")
plt.title("Daily Food Waste Trend")

plt.xticks(rotation=45)

plt.show()

#  Prepared vs Consumed vs Waste

comparison = df[[
    "Prepared_Qty_kg",
    "Consumed_Qty_kg",
    "Waste_Qty_kg"
]].sum()

print("\nTotal Prepared, Consumed and Waste:")
print(comparison)

plt.figure(figsize=(8, 5))

plt.bar(
    comparison.index,
    comparison.values
)

plt.xlabel("Food Quantity")
plt.ylabel("Quantity (kg)")
plt.title("Total Prepared vs Consumed vs Waste")

plt.xticks(rotation=20)

plt.show()

# Prepared vs Consumed vs Waste

comparison = df[[
    "Prepared_Qty_kg",
    "Consumed_Qty_kg",
    "Waste_Qty_kg"
]].sum()

print("\nTotal Prepared, Consumed and Waste:")
print(comparison)

plt.figure(figsize=(8, 5))

plt.bar(
    comparison.index,
    comparison.values
)

plt.xlabel("Food Quantity")
plt.ylabel("Quantity (kg)")
plt.title("Total Prepared vs Consumed vs Waste")

plt.xticks(rotation=20)

plt.show()

# Final project insights

highest_waste_meal = meal_waste.idxmax()
highest_waste_meal_value = meal_waste.max()

highest_waste_food = food_waste.idxmax()
highest_waste_food_value = food_waste.max()

highest_waste_day = day_waste.idxmax()
highest_waste_day_value = day_waste.max()

print("\n--- FINAL INSIGHTS ---")

print(
    "Meal with highest average waste:",
    highest_waste_meal,
    "(", highest_waste_meal_value, "kg )"
)

print(
    "Food item with highest average waste:",
    highest_waste_food,
    "(", highest_waste_food_value, "kg )"
)

print(
    "Day with highest average waste:",
    highest_waste_day,
    "(", highest_waste_day_value, "kg )"
)

print(
    "Total food waste:",
    total_waste,
    "kg"
)

print(
    "Average food waste per entry:",
    average_waste,
    "kg"
)

