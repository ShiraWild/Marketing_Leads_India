# Interview_buzer-ai
candidate: Shira Wild 

Files decription:

1. "build_the_model.ipynb" - this file contains the whole data science process - Preprocessing for train and test data, transformations, feature selections, 
building the final model by using search grid for tuning different models and parameters and evaluation phase for the final model.

2. "leads_predictions.csv" - a csv file containing the predictions for the test data. The file contains two columns: lead_id - the id of the lead, 
and score - the predicted score for the lead.

3. "leads_predictions_todb.py" - a python file containing the connection to the database, stored in pgadmin (postgresql) and the
insertion of the predictions of the test data to a table named "Predictions" in the database "Leads". 

4. "db_after_insert.pdf" - a pdf file containing snapshots of the database after the insertion of the predictions rows.

