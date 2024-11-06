# PowerBI Traffic Accident Statistical Analysis: A Comprehensive Guide

## Introduction

This tutorial will guide you through using Power BI's Data Analysis Expressions (DAX) for complex data modelling and advanced exploratory data analysis (EDA). You’ll also learn to apply statistical tests like hypothesis testing and ANOVA directly within Power BI to gain insights from a sample dataset on traffic accidents.

## Part 1: Data Import and Statistical Foundation

### 1.1 Creating Your Statistical Environment

Let's begin by setting up our PowerBI workspace:

1. Launch Power BI Desktop on your computer.
2. Navigate to File → Save As.
3. Name your file "Traffic_Statistical_Analysis.pbix".
4. Choose a suitable location on your computer to save the file.

### 1.2 Importing Data

Now, let's bring our accident data into PowerBI:

1. Click on the 'Get Data' button.
2. Select Text/CSV.
3. Browse to your accident data file.
4. In the Preview window, verify these settings:
   - Delimiter: Comma
   - Data Type Detection: Based on entire dataset
5. Click 'Transform Data'.

### 1.3. **Choose Only the Required Columns**:

- Identify and select the required columns for this tutorial:
  - `accident_index`
  - `accident_severity`
  - `number_of_vehicles`
  - `day_of_week`
  - `latitude`
  - `longitude`
  - `local_authority_district`
- To select multiple columns, hold down the **Ctrl** key and click on each required column.

### 1.4. **Remove Unselected Columns**:

- With the required columns selected, go to the **Home** tab in Power Query Editor.
- Click **Remove Columns > Remove Other Columns**. This will delete all columns except the ones you selected.

### 1.5. **Check Data Types**

Proper data types are crucial for accurate analysis. Let's set them for our key columns:

1. accident_severity: Whole Number
2. number_of_casualties: Whole Number
3. latitude: Decimal Number
4. longitude: Decimal Number
5. date: Date
6. time: Time

To change a data type, click the data type icon next to each column name.

### 1.6. **Confirm and Apply Changes**:

- Review your dataset to ensure only the necessary columns remain.
- Once confirmed, click **Close & Apply** in the top-left corner to apply your changes

### 1.7. **Renaming the Data Table in Power BI**

Renaming your data table to something more intuitive helps keep your Power BI project organised and makes it easier to reference the table in measures and visuals. Here’s how to change the table name from `dft-road-casualty-statistics-collision-2023` to `Accidents`.

**Steps to Rename the Data Table**

1. **Open Fields Pane**:

   - In Power BI Desktop, locate the **Fields** pane on the right side of the window.
   - Find the table named `dft-road-casualty-statistics-collision-2023`.

2. **Rename the Table**:

   - Right-click on the table name (`dft-road-casualty-statistics-collision-2023`).
   - Select **Rename** from the context menu.
   - Type the new name: `Accidents`.
   - Press **Enter** to save the new name.

3. **Confirm the Change**:
   - Check that the table name in the **Fields** pane now shows as `Accidents`.
   - Any references to this table in existing visuals or measures will automatically update to the new name.

## Part 2: Setting Up the Dataset and Initial EDA

### 2.1 Creating Basic Measures in DAX

1. **Define basic measures to assist with further analysis:**

- **Total Accidents**:
  ```DAX
  Total Accidents = COUNT('Accidents'[accident_index])
  ```
- **Average Vehicles per Accident**:
  ```DAX
  Avg Vehicles = AVERAGE('Accidents'[number_of_vehicles])
  ```

2. **Visualising Basic Measures:**

- **Total Accidents**: Create a **Card** visual by selecting the _Total Accidents_ measure to display the total count of accidents.
- **Average Vehicles per Accident**: Create another **Card** visual for _Avg Vehicles_ to show the average number of vehicles involved in accidents.

---

### Part 3: Advanced Exploratory Data Analysis (EDA)

#### 3.1 Multivariate Analysis

We’ll start by analysing how multiple variables interact, such as `day_of_week` with `accident_severity`.

1. **Create a Measure for Severity by Day**:
   ```DAX
   Severity by Day =
   CALCULATE(
       AVERAGE('Accidents'[accident_severity]),
       ALLEXCEPT('Accidents', 'Accidents'[day_of_week])
   )
   ```
2. **Visualise Severity by Day**:
   - Add a **Bar Chart** from the _Visualizations_ pane.
   - Set `day_of_week` on the x-axis and the `Severity by Day` measure as the y-axis.
   - This will show the average accident severity for each day of the week, allowing you to observe trends over time.

#### 3.2 Dimensionality Reduction

Use a measure to approximate dimensionality reduction by summarising accident severity across combined categories.

1. **Create an Aggregated Severity Measure**:
   ```DAX
   Aggregated Severity =
   SUMX(
       'Accidents',
       'Accidents'[accident_severity] * 'Accidents'[number_of_vehicles]
   )
   ```
2. **Visualise Aggregated Severity by Location on a Map**:
   - Add a **Map** visual from the _Visualizations_ pane.
   - Drag `latitude` to _Latitude_ and `longitude` to _Longitude_.
   - Set the `Aggregated Severity` measure to the _Size_ field, adjusting the size of each point based on accident severity.
   - Format the map by applying a colour scale in the _Data colors_ section, which can help in identifying clusters of high-severity accidents.

---

### Part 4: Statistical Analysis with DAX

#### 4.1 Hypothesis Testing: Comparing Severity on Weekdays vs Weekends

1. **Create a `Day Type` Column in the `Accidents` Table**:

   - In the **Accidents** table, create a calculated column to label each row as either "Weekday" or "Weekend" based on the `day_of_week` value.
   - Go to the **Modeling** tab and select **New Column**.
   - Enter the following DAX formula:
     ```DAX
     Day Type =
     IF(
         'Accidents'[day_of_week] <= 5,
         "Weekday",
         "Weekend"
     )
     ```
   - This will create a `Day Type` column that dynamically assigns "Weekday" to records with `day_of_week` values of 1 to 5, and "Weekend" to records with `day_of_week` values of 6 or 7.

2. **Create Measures for Weekday and Weekend Severity**:

   - With the `Day Type` column in place, you can now calculate the average severity for each day type.
   - Define the following DAX measures:

     ```DAX
     Weekday Severity =
     CALCULATE(
         AVERAGE('Accidents'[accident_severity]),
         'Accidents'[Day Type] = "Weekday"
     )
     ```

     and:

     ```DAX
     Weekend Severity =
     CALCULATE(
       AVERAGE('Accidents'[accident_severity]),
       'Accidents'[Day Type] = "Weekend"
     )
     ```

3. **Visualise Weekday vs Weekend Severity**:
   - Create a **Clustered Bar Chart**.
   - Drag the new `Day Type` column to the **X-Axis**.
   - Add `Weekday Severity` and `Weekend Severity` as **Values** on the **Y-Axis**.
   - Ensure that the chart is set to display average severity, not a count of values.

**Interpreting the Results**:

- If you observe similar values for `Weekday Severity` and `Weekend Severity` (e.g., 2.7 and 2.8), this could indicate that accident severity does not vary significantly between weekdays and weekends in the dataset. This is not unusual if the dataset reflects homogeneous accident severity.
- **Next Steps**:
  - Consider increasing decimal places in **Data Labels** to emphasise minor differences.
  - Use other dimensions such as **local authority district** or **road type** for more granularity.
  - For statistical significance testing, consider exporting the data for t-testing in a tool like Excel, R, or SPSS.

## Part 5: ANOVA for Accident Severity Across Days

Use DAX to compare severity across multiple days using a variance measure.

### 5.1 **Create a Variance Measure for Severity by Day**:

```DAX
Variance in Severity =
VAR SeverityMean = AVERAGE('Accidents'[accident_severity])
RETURN
    SUMX(
        'Accidents',
        POWER('Accidents'[accident_severity] - SeverityMean, 2)
    )
```

2. **Visualise Variance by Day**:
   - Add a **Line Chart** and place `day_of_week` on the x-axis and `Variance in Severity` on the y-axis.
   - This visual will highlight which days show higher variance in accident severity, which may indicate inconsistencies worth investigating.

---

## Part 6: Recap and Next Steps

By completing this tutorial, you now have experience:

- Creating complex DAX measures to analyse and summarise accident data.
- Performing multivariate analysis and dimensionality reduction.
- Applying statistical concepts, like hypothesis testing and ANOVA, using DAX measures.

**Activity**: Test different groupings of `local_authority_district` and `accident_severity` to explore if certain regions show higher variances in accident severity, suggesting targeted intervention.

This tutorial should support your understanding of DAX and Power BI for robust EDA and statistical analysis, enhancing data-driven decision-making.
