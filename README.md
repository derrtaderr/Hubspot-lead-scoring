# Auto ML for Superior Lead Scoring in HubSpot

## Overview

This project showcases how to use Auto ML to improve lead scoring in HubSpot for Account-Based Marketing (ABM) campaigns. By integrating rich engagement data with machine learning, we aim to predict which leads are most likely to convert, allowing for more efficient and effective marketing efforts.

## Features

- **Data Extraction**: Scripts to extract engagement metrics and other relevant data from HubSpot.
- **Model Training**: Use of Azure's AutoML to train a model capable of predicting lead conversion.
- **Model Prediction**: Application of the trained model to score new leads and update their scores in HubSpot.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- A HubSpot account with API access
- An Azure account with an Azure ML workspace

### Installation

1. **Clone the repository to your local machine:**
   
   ```shell
   git clone https://github.com/yourusername/hubspot-lead-scoring.git

2. **Navigate to the project directory:**

   ```shell
   cd hubspot-lead-scoring

4. **Install the required dependencies:**

   ```shell
    pip install -r requirements.txt
## Configuration

- **HubSpot API Key**: Replace `'your-hubspot-api-key'` in the `data_extraction/extract_data.py` and `model_prediction/predict_scores.py` scripts with your actual HubSpot API key.
- **Azure ML Workspace**: Ensure you have a `config.json` file from your Azure ML workspace in the project directory for use in `model_training/train_model.py`.

## Usage

### Extracting Data from HubSpot
  
 ```
  python data_extraction/extract_data.py
 ```
This script extracts engagement data from HubSpot and saves it to `leads_data.csv`.

### Training the Auto ML Model

  ```
     python model_training/train_model.py
  ``` 
This command trains the lead scoring model using Azure AutoML.

### Scoring Leads and Updating HubSpot

  ```
  python model_prediction/predict_scores.py
  ``` 
Use this script to score new leads using the trained model and update their scores in HubSpot.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is open source and available under the MIT License.
