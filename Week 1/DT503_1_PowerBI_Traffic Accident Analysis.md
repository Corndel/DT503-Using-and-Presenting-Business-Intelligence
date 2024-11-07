# PowerBI Traffic Accident Analysis Dashboard

## Introduction

Welcome to this comprehensive guide on creating a Traffic Accident Analysis Dashboard using PowerBI. This tutorial will walk you through the process of importing data, creating measures, and building an informative dashboard. By the end of this guide, you'll have a powerful tool for analysing road traffic accidents.

## Part 1: Data Import and Preparation

### 1.1 Creating a New Power BI File

Let's begin by setting up our PowerBI environment:

1. Launch Power BI Desktop on your computer.
2. Navigate to File → Save As.
3. Name your file "Traffic_Accident_Analysis.pbix".
4. Choose a suitable location on your computer to save the file.

### 1.2 Importing Data

Now, let's bring our accident data into PowerBI:

1. In PowerBI, click on the 'Get Data' button.
2. From the options, select Text/CSV.
3. Browse to the location of your accident data CSV file and select it.
4. In the Preview window that appears, ensure the following settings:
   - Delimiter: Comma
   - Data Type Detection: First 200 rows
5. Once you've verified these settings, click 'Transform Data'.

### 1.3 Setting Data Types

Proper data types are crucial for accurate analysis. Let's set them for our key columns:

1. accident_index: Set to Text
2. accident_year: Set to Integer Number
3. date: Set to Date
4. time: Set to Time
5. accident_severity: Set to Integer Number

To change a data type, click on the icon next to the column name and select the appropriate type from the dropdown menu.

### 1.4 Creating Custom Columns

To enhance our analysis, we'll create two custom columns:

1. DayOfTheWeek:

   - Click 'Add Column' → 'Custom Column'
   - Name the new column "DayOfTheWeek"
   - Use the following formula:
     ```
     = if [day_of_week] = 1 then "Monday"
     else if [day_of_week] = 2 then "Tuesday"
     else if [day_of_week] = 3 then "Wednesday"
     else if [day_of_week] = 4 then "Thursday"
     else if [day_of_week] = 5 then "Friday"
     else if [day_of_week] = 6 then "Saturday"
     else "Sunday"
     ```

2. SeverityDesc:
   - Again, click 'Add Column' → 'Custom Column'
   - Name this column "SeverityDesc"
   - Use the following formula:
     ```
     = if [accident_severity] = 1 then "Fatal"
     else if [accident_severity] = 2 then "Serious"
     else "Slight"
     ```

These custom columns will allow us to display more meaningful information in our visualisations.

### 1.5 Renaming and Filtering the Query

To keep our work organised:

1. Rename your query to 'Accidents'. This provides a clearer, more concise name than the original file name.
2. To manage the dataset size, filter the data to focus on a single 'police_force' region.
3. After making these changes, click 'Close & Apply' to return to the main PowerBI interface.

## Part 2: Creating Base Measures

Measures are essential for creating dynamic visualisations. Let's create some key measures:

1. Total Accidents:

   - Formula: `TotalAccidents = COUNT(Accidents[accident_index])`
     This measure counts the total number of accidents in our dataset.

2. Total Casualties:

   - Formula: `TotalCasualties = SUM(Accidents[number_of_casualties])`
     This measure sums up all casualties across all accidents.

3. Average Severity:

   - Formula: `AvgSeverity = AVERAGE(Accidents[accident_severity])`
     This measure calculates the average severity of accidents.

4. Accidents Per Day:
   - Formula: `AccidentsPerDay = DIVIDE(COUNT(Accidents[accident_index]),DISTINCTCOUNT(Accidents[date])`
     This measure calculates the average number of accidents per day.

To create these measures:

1. Click on 'New Measure' in the Home tab.
2. Enter the formula for each measure.
3. Name each measure appropriately.

## Part 3: Building the Overview Page

Now, let's create our dashboard:

### 3.1 Adding KPI Cards

At the top of our dashboard, we'll add four card visuals to display our key metrics:

1. From the Visualisations pane, select the Card visual four times.
2. For each card, drag the corresponding measure:
   - Total Accidents
   - Total Casualties
   - Average Severity
   - Accidents Per Day

### 3.2 Adding Plot Breakdowns

Let's add some charts to provide more detailed insights:

1. Line Chart: Accidents Over Time

   - Add a Line Chart visual
   - Set X-axis to 'date'
   - Set Y-axis to 'Count of accident_index'
   - In the Format tab:
     - Set aggregation to monthly
     - Add data labels for clarity

2. Column Chart: Day of Week Analysis

   - Add a Column Chart visual
   - Set X-axis to 'day_of_week'
   - Set Y-axis to 'Count of accident_index'

3. Donut Chart: Accident Severity Breakdown
   - Add a Donut Chart visual
   - Set Legend to 'SeverityDesc'
   - Set Values to 'Count of accident_index'

### 3.3 Adding Titles and Descriptions

To make our dashboard more user-friendly:

1. Add a text box at the top of the page.
2. Enter the title: '2023 Road Traffic Accidents Dashboard'
3. Format the title to stand out (e.g., larger font size, bold).

### 3.4 Ensuring Format Consistency

For a professional look:

1. Review all visuals:
   - Use a consistent colour scheme
   - Align elements neatly
   - Ensure proper spacing between elements
   - Verify that all labels are clear and readable

## Conclusion

Congratulations! You've now created a comprehensive Traffic Accident Analysis Dashboard in PowerBI. This dashboard provides valuable insights into accident patterns, severity and trends over time. Remember to save your work regularly.

### Activity

Take a moment to explore your dashboard. What insights can you gather about traffic accidents in your chosen police force region? Are there any particular days or times when accidents are more frequent? How might this information be useful for improving road safety?
