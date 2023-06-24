# Data Engineering Project
The aim of this project is to execute a modern data engineering workflow using various technologies, performed on a sample grocery store dataset.

## Data Source
- This dataset is a sample grocery store dataset that contains information on Order IDs, Categories and Subcategories, Profit and Sales, Region and City, etc.
- More information on the dataset can be found [here.](https://www.kaggle.com/datasets/mohamedharris/supermart-grocery-sales-retail-analytics-dataset)
- Provided by [Mohamed Harris.](https://www.kaggle.com/mohamedharris)
## Data Architecture
- [GCP Data Architecture](model_architecture/gcp_data_architecture.pdf)

## Data Model
- Data Model takes original data schema and follows fact and dimension table formatting.
- [Data Model](model_architecture/data_model.pdf).

## Technologies Utilized
- [Google Cloud Platform](https://cloud.google.com/gcp?utm_source=bing&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-e-dr-1605212&utm_content=text-ad-none-any-DEV_c-CRE_-ADGP_Desk+%7C+BKWS+-+EXA+%7C+Txt++_+General+GCP+-+Core-KWID_43700065593098574-kwd-77240903503381:loc-190&utm_term=KW_google+cloud+platform-ST_google+cloud+platform&gclid=46872ac7808b157bec584e50843fe9ea&gclsrc=3p.ds&msclkid=46872ac7808b157bec584e50843fe9ea&hl=en)
  - Google Storage
  - Compute Instance
  - BigQuery
  - Looker Studio
- [Mage Modern Data Engineering Pipeline Replacement for Airflow.](https://www.mage.ai/)

- **Python** for ETL
  - [ETL Scripts](etl_scripts)
  - [Pipeline](pipeline)
-  **SQL** on BigQuery
   - [Queries](queries)

## Dashboard
 - [Final Dashboard](dashboard/grocery_data_engineering_dashboard.pdf)
 - I have since shut down the VM, Storage, and BigQuery, so the interactive portion of the dashboard is unavailable.
