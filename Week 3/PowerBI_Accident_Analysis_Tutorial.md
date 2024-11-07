
# Power BI Accident Analysis and Statistical Insight Dashboard

## Introduction

This guide will walk you through creating an advanced Traffic Accident Analysis Dashboard in Power BI Desktop. We’ll cover data import, cleaning, advanced DAX functions, conditional formatting, KPI indicators, and custom visualisation using Python.

---

## Part 1: Data Import and Preparation

### 1.1 Setting Up Power BI Desktop

1. Open Power BI Desktop.
2. Go to **File** > **Save As** to save your file with the name "Accident_Analysis_Dashboard.pbix" in a location of your choice.

### 1.2 Importing and Renaming the Data

1. Click on **Get Data** and choose **Text/CSV**.
2. Locate and select the `dft-road-casualty-statistics-collision-2023.csv` file.
3. In the data preview window, ensure columns are correctly recognised, then click **Load**.
4. Once loaded, navigate to the **Fields** pane, right-click on the imported table (`dft-road-casualty-statistics-collision-2023`), and choose **Rename**.
5. Rename the table to **AccidentData**. This renaming makes it easier to reference the table in formulas and scripts.

### 1.3 Data Cleaning and Transformation

To prepare data for analysis, follow these steps:

1. Go to **Transform Data** to open Power Query Editor.
2. **Rename Columns**: Rename columns for clarity (e.g., rename `Accident Severity` to `Severity`, `Accident Date` to `Date`).
3. **Set Data Types**:
   - Set **Date** as Date.
   - Set **Latitude** and **Longitude** as Decimal Numbers.
   - Set **Severity** as Whole Number.
4. **Filter Data**: Optionally, filter out irrelevant or incomplete records, such as those missing location data.
5. Click **Close & Apply** to load the cleaned data into Power BI.

---

## Part 2: Advanced Statistical Analysis with DAX

With the data prepared, we’ll use DAX to create statistical insights, along with visuals to better interpret these insights.

### 2.1 Average Accident Severity by Location

**Objective**: Calculate and visualise the average accident severity for each location.

1. **Create a New Measure**:
   - Go to **Modelling** > **New Measure**.
   - Enter the following formula:
     ```DAX
     AverageSeverity = AVERAGE(AccidentData[Severity])
     ```
   - Press **Enter** to save the measure.

2. **Visualise Average Severity by Location**:
   - In the **Visualisations** pane, select the **Table** visual.
   - Drag the **Latitude** and **Longitude** fields to the **Values** area to represent each unique accident location.
   - Drag the **AverageSeverity** measure to the **Values** area.
   - This will display the average severity for each location in a table format, making it easy to compare accident severity across different locations.

### 2.2 Monthly Accident Count

**Objective**: Track accident frequency over time by calculating monthly accident counts and displaying this as a line chart.

1. **Create a Monthly Accident Count Measure**:
   - Go to **Modelling** > **New Measure**.
   - Use this formula to create the count of accidents by month:
     ```DAX
     MonthlyAccidentCount = COUNTROWS(SUMMARIZE(AccidentData, AccidentData[Month], AccidentData[AccidentID]))
     ```
   - Press **Enter** to save the measure.

2. **Create a Line Chart for Monthly Accident Trends**:
   - In the **Visualisations** pane, select the **Line Chart**.
   - Drag the **Month** field to the **X-axis**.
   - Drag the **MonthlyAccidentCount** measure to the **Values** field.
   - This line chart will show accident trends over time, with peaks and dips representing monthly variations.

3. **Format the Chart**:
   - Go to **Format** > **Data labels** and turn them on for better readability.
   - Adjust the **X-axis** and **Y-axis** settings to ensure all data points are visible.

### 2.3 Year-Over-Year Comparison

**Objective**: Compare accident rates between years by creating a Year-Over-Year (YoY) measure and visualising it with a column chart.

1. **Create a YoY Accident Count Measure**:
   - Go to **Modelling** > **New Measure**.
   - Use the following DAX formula:
     ```DAX
     YoY_Accident_Count = CALCULATE(COUNT(AccidentData[AccidentID]), SAMEPERIODLASTYEAR(AccidentData[Date]))
     ```
   - Press **Enter** to save the measure.

2. **Create a Clustered Column Chart for Year-to-Year Comparison**:
   - In the **Visualisations** pane, select the **Clustered Column Chart**.
   - Drag the **Year** field to the **X-axis** to represent each year in the dataset.
   - Drag both the **MonthlyAccidentCount** and **YoY_Accident_Count** measures to the **Values** area.
   - This chart will display columns for each year, allowing you to visually compare accident counts across years.

3. **Customise the Chart**:
   - Go to **Format** > **Data colours** to apply different colours to each measure, making it easy to distinguish between actual counts and YoY comparisons.
   - Optionally, turn on **Data labels** for each column to make year-over-year differences clear at a glance.

---

## Part 3: Conditional Formatting and KPI Indicators

Enhance the visuals with conditional formatting and KPI indicators to highlight high-risk areas.

### 3.1 Conditional Formatting for Accident Severity

1. Select a **Map** or **Table** visual showing accident locations.
2. Go to **Format** > **Data Colours** and set a colour scale based on **Severity**:
   - Darker shades for higher severity levels.
   - Lighter shades for lower severity levels.
3. This helps quickly identify high-severity areas on the map.

### 3.2 KPI Indicators for Accident Frequency

1. Add a **KPI** visual to monitor accident frequency against targets.
2. Set **Indicator** to the **MonthlyAccidentCount** measure.
3. Set **Target** as a benchmark (such as last year’s average) and enable trend formatting.
4. This KPI will give a clear visual of changes in accident rates over time.

---

## Part 4: Custom Analysis with Python in Power BI

Incorporate Python for more advanced statistical analysis and custom visuals.

### 4.1 Enabling Python in Power BI

1. Go to **File** > **Options and Settings** > **Options**.
2. Under **Python scripting**, set the Python home directory to your Python installation location (e.g., `C:\Python38`).
3. Ensure you have libraries like `pandas`, `matplotlib`, and `seaborn` installed.

### 4.2 Adding a Python Visual

1. In the **Visualisations** pane, select the **Python visual**.
2. Drag fields like `Severity`, `Latitude`, `Longitude`, and `Date` into the **Values** area.
3. Power BI will automatically create a DataFrame named `dataset` from the selected fields.

### 4.3 Python Script for Accident Severity Analysis

Here’s an example script to compare high vs. low severity accidents:

```python
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Data preparation
high_severity = dataset[dataset['Severity'] > 3]['AccidentCount']
low_severity = dataset[dataset['Severity'] <= 3]['AccidentCount']
t_stat, p_val = ttest_ind(high_severity, low_severity)

# Visualisation
plt.figure(figsize=(8, 5))
plt.text(0.1, 0.6, f"T-statistic: {t_stat:.2f}
P-value: {p_val:.4f}", fontsize=12)
plt.axis('off')
plt.title("Statistical Analysis: High vs. Low Severity Accidents")
plt.show()
```

4. Run the script to display the statistical analysis result within Power BI.

### 4.4 Python Heatmap for Accident Density

1. Add **Date** and **Location** fields to the Python visual.
2. Use this code to generate a heatmap of accident density:

   ```python
   import seaborn as sns

   plt.figure(figsize=(10, 6))
   heatmap_data = dataset.pivot_table(index='Date', columns='Location', values='AccidentCount', aggfunc='sum')
   sns.heatmap(heatmap_data, cmap='Reds', annot=True, fmt=".0f")
   plt.title("Accident Density Heatmap")
   plt.show()
   ```

---

## Conclusion

By following these steps, you’ve built a powerful, insightful dashboard that combines statistical analysis, DAX functions, conditional formatting, KPIs, and custom Python visualisation. This dashboard enables deep insights into traffic accidents, helping you identify patterns and trends for effective decision-making.
