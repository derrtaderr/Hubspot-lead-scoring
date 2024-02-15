from azureml.core import Workspace, Experiment
from azureml.train.automl import AutoMLConfig
import pandas as pd

# Load data
leads_df = pd.read_csv('leads_data.csv')

automl_workspace = Workspace.from_config()  # Ensure you have a config.json file

automl_config = AutoMLConfig(task='classification',
                             primary_metric='AUC_weighted',
                             training_data=leads_df,
                             label_column_name='converted',
                             n_cross_validations=5)

experiment = Experiment(automl_workspace, "hubspot-lead-scoring")
run = experiment.submit(automl_config, show_output=True)
