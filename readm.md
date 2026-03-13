# TTC Subway Delay Data — Preprocessing & Exploratory Analysis

**Author:** Umniyah Aalam
**Date:** February 2026  
**Dataset:** Toronto Transit Commission (TTC) subway delay records, 2024–2025  

## Objective

Prepare TTC subway delay data for a regression model that predicts **delay duration in minutes** for a given line, station, time, and day.

## Approach

| Step | Description |
|------|-------------|
| **1. Data Loading** | Combine 2024 (Excel) and 2025 (CSV) delay records into a single dataset |
| **2. Data Cleaning** | Standardize line names, remove invalid records, handle outliers, drop irrelevant columns |
| **3. Feature Engineering** | Extract temporal features, compute historical average delays per route/time |
| **4. Correlation Analysis** | Identify data leakage, multicollinearity, and useful predictors |
| **5. Exploratory Data Analysis** | Visualize delay patterns by time, day, line, station, and incident code |
| **6. Export** | Save the cleaned dataset for model training |

## Target Variable

`min_delay_capped` — delay in minutes, capped at 60 to mitigate extreme outliers.

---