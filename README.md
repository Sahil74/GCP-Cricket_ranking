# Cricket Data Pipeline and Visualization

## Project Overview

- This project automates the extraction, transformation, and loading (ETL) of cricket data using the Cricbuzz API. The entire workflow is designed to run seamlessly, with data being extracted, processed, and visualized using Google Cloud services. The final output is a set of visualizations in Looker Studio, providing insights into cricket data.

## Key Features

- Data Extraction: Utilized Cricbuzz API in Python to extract cricket data.
- Data Storage: Stored the extracted data as CSV files in a Google Cloud Storage bucket.
- Data Pipeline: Used Google Cloud Dataflow for ETL (Extract, Transform, Load) operations, transforming the data and - loading it into BigQuery.
- Automation: Automated the entire process using Google Cloud Composer. A Python script triggers the workflow, which ---extracts data, uploads it to the cloud, processes it, and loads it into BigQuery.
- Data Visualization: Leveraged Looker Studio to create visualizations from the BigQuery dataset.

## Project Architecture

## Prerequisites

- Python 3.x installed on your local machine.
- Google Cloud Platform account with access to Cloud Storage, BigQuery, Dataflow, and Cloud Composer.
- Cricbuzz API access for data extraction.

## Usage

- Automated ETL Process: By running the provided Python script, the entire process from data extraction to loading into BigQuery is automated.
- Visualization: Use Looker Studio to visualize and analyze the cricket data.
