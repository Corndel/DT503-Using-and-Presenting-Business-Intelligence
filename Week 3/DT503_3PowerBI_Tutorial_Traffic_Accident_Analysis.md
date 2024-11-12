# Power BI Tutorial for Traffic Accident Analysis

This step-by-step tutorial will guide you through setting up a Power BI dashboard using processed traffic accident data.
We’ll utliise PCA, factor analysis, cluster analysis and discriminant analysis results exported from Python to uncover accident patterns and support data-driven decision-making.

---

## 1. Export Processed Data from Python

### Why This Step?

To ensure Power BI can handle and visualise complex accident patterns efficiently, we first use Python to prepare key data transformations. If you haven't undertaken the DT503 week 3 Python activity yet, please do so before attempting this tutorial.
By reducing dimensionality (using PCA), clustering, and factor analysis, we simplify the data for better insights.

### Instructions

1. **Prepare Data to Export**:
   Complete the 'DT503_3_Traffic_Accident_Data_Analysis.ipynb' step through tutorial, ensuring you run each code cell in the notebook. - Verify that your dataset includes: - **PCA Components** (e.g., first 5 components from Principal Component Analysis), capturing main data patterns. - **Cluster Labels** (from KMeans clustering), categorising accidents into distinct profiles. - **Factor Scores** (from Factor Analysis), revealing underlying factors influencing accident patterns. - **Classification Labels** (from Discriminant Analysis), providing predicted clusters based on identified patterns.
2. **Export to CSV**:

   - Save the data as a CSV (e.g., `accident_analysis_export.csv`) for easy import into Power BI.

3. **Import Data into Power BI**:
   - In Power BI Desktop, go to **Home > Get Data > Text/CSV** and import your CSV file.
   - Check the **Data view** to confirm the fields are correctly loaded, including PCA components, clusters, and factor scores.

---

## 2. Create the Overview Page

### Purpose

The overview page provides high-level insights into accident frequency and trends. This page helps identify peak times and overall accident scale for strategic planning.

### Instructions

1. **Total Accidents**:

   - Create a **Card visual** to display the total number of accidents.
   - Use **Count of `accident_index`** to calculate this total.

2. **Monthly Trends**:
   - Add a **Line Chart** to track trends over time.
   - **X-axis**: From the `Date` drag `Month` to group data by month.
   - **Y-axis**: Use **Count of `accident_index`** to show the total accidents per month.

### Interpretation

- **Total Accidents**: Provides a quick snapshot of the overall accident count, setting the context for analysis.
- **Monthly Trends**: Identifies seasonal patterns or high-risk months, suggesting where targeted interventions (e.g., winter safety campaigns) may be beneficial.

---

## 3. Visualise PCA Components

### Purpose

Visualising PCA components reduces complexity, letting us focus on primary accident patterns by examining relationships between principal components.

### Instructions

1. **Scatter Plot**:

   - Create a **Scatter Chart** with PCA components.
   - **X-axis**: Set `PC1` (Principal Component 1).
   - **Y-axis**: Set `PC2` (Principal Component 2).
   - **Legend**: Drag `Cluster` to **Legend** to colour-code each cluster.

2. **Tooltip**:
   - Add fields like `accident_severity` or `number_of_casualties` to the **Tooltip** for extra detail on hover.

### Interpretation

- **Cluster Separation**: Observe if clusters separate distinctly, which can suggest unique accident profiles (e.g., different accident causes or severity levels).
- **Patterns by Cluster**: Identify if certain clusters show higher severities or casualties, helping prioritise interventions for those groups.

---

## 4. Visualise Cluster Analysis

### Purpose

Cluster analysis identifies distinct accident types or profiles. Visualising these clusters helps understand geographical accident patterns and profile high-risk areas.

### Instructions

1. **Map of Cluster Locations**:

   - Add a **Map visual** to show accident locations.
   - **Latitude**: Set `latitude`.
   - **Longitude**: Set `longitude`.
   - **Legend**: Use `Cluster` to differentiate clusters by colour.
   - **Bubble Size**: Set `number_of_casualties` or `accident_severity` in **Bubble Size** to represent accident impact.

2. **Cluster Summary Metrics**:

   - Use **Card visuals** or a **Table** to display summary statistics for each cluster, such as average severity or casualty counts.

3. **Interactive Filtering**:
   - Add a **Slicer** for `Cluster` to filter visuals by cluster.

### Interpretation

- **High-Risk Areas**: Identify locations where severe or high-casualty accidents are concentrated, allowing targeted measures in these areas.
- **Cluster Profiles**: Summarise each cluster’s characteristics, such as average severity or location type, to understand different accident profiles.

---

## 5. Visualise Factor Analysis with Bar Charts

### Purpose

Factor Analysis reveals latent patterns by grouping related variables. This section helps interpret the key accident characteristics by factor, especially across different clusters.

### Instructions

1. **Bar Charts for Factor Scores**:

   - For each factor (e.g., `Factor1`, `Factor2`), create a separate bar chart.
   - **X-axis**: Set `Cluster` to group data by cluster.
   - **Y-axis**: Set each chart’s `Y-axis` to a specific factor score (e.g., `Factor1`).

2. **Arrange Charts**:
   - Arrange the bar charts side-by-side or stacked to compare factors across clusters.

### Interpretation

- **Factor Patterns**: Identify which factors are most significant for each cluster, offering insights into accident causes (e.g., road type or weather conditions).
- **Cluster-Specific Factors**: Recognise clusters where certain factors dominate, informing targeted strategies (e.g., improved signage on dangerous roads if road type is a key factor).

---

## 6. Visualise Discriminant Analysis Results

### Purpose

This step evaluates the accuracy of the Discriminant Analysis model by comparing original clusters to model-predicted clusters, showing how well each accident type is classified.

### Instructions

1. **Confusion Matrix Using a Matrix Visual**:

   - Select the **Matrix visual** to create a confusion matrix.
   - **Rows**: Drag `Cluster` (original cluster labels).
   - **Columns**: Drag `Classification_Label` (predicted cluster from Discriminant Analysis).
   - **Values**: Add `Count of accident_index` to count each actual-predicted pair.

2. **Interpret the Confusion Matrix**:

   - Diagonal cells show correct classifications, where predicted matches actual clusters.
   - Off-diagonal cells highlight misclassifications.

3. **Accuracy Summary (Optional)**:
   - Use **Card visuals** to display overall accuracy and per-cluster accuracy.

### Interpretation

- **Model Accuracy**: High accuracy indicates reliable classification, especially if most values fall along the diagonal.
- **Cluster Challenges**: Misclassifications (off-diagonal values) show clusters that may overlap, suggesting areas to refine the model or analysis.

---

## 7. Dashboard Summary and Presentation

### Purpose

Summarising and interpreting the dashboard insights makes the analysis actionable, allowing stakeholders to address high-risk factors and improve road safety.

### Summary of Insights

1. **Accident Frequency and Timing**: Use the Overview page to highlight total accident counts and monthly peaks, guiding time-based interventions.
2. **Accident Profiles by Cluster**: The PCA and Cluster Analysis sections reveal different accident profiles, helping to target interventions by profile.
3. **Key Accident Factors**: Factor Analysis insights identify influential variables, enabling focused efforts (e.g., improving lighting or signage).
4. **Predictive Reliability**: Discriminant Analysis results demonstrate model accuracy, showing where the classification model is most effective.

### Recommendations

- **High-Risk Months**: Suggest seasonal campaigns or resources based on monthly trends.
- **Geographic Hotspots**: Address high-casualty locations identified in the map visualisation with targeted improvements.
- **Cluster-Specific Actions**: Implement tailored measures for each cluster type, such as enhancing road conditions in areas with high accident severity scores.

This tutorial offers a structured approach to understanding accident data and driving safety-focused insights with Power BI.
