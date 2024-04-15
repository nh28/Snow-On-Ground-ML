import os
from AddElements import AddElements
import pandas as pd
from Model import Model
from Query import Query


query = Query()
username = "PCHARSCHN"
password = "White16Pots"
connection, success = query.connect(username, password)
if success:
    
   excel_file_path = os.path.abspath("SOG_Phase4&5.xlsx") 
   excel_sheet = "Sheet1"

   df = pd.read_excel(excel_file_path, sheet_name=excel_sheet)

   """
   for index, row in df.iterrows():
      type = row['MEAS_TYPE_ID']
      if type == 951:
         df.loc[index] = AddElements.add(query, row, connection, 940, 941, 964, 948, 949, 950, 951, 951, 14910, 15498)
      elif type == 14910:
         df.loc[index] = AddElements.add(query, row, connection, 14899, 14900, 14923, 14907, 14908, 14909, 14910, 951, 14910, 15498)
      elif type == 15498:
         df.loc[index] = AddElements.add(query, row, connection, 15492, 15493, 15494, 15495, 15496, 15497, 15498, 951, 14910, 15498)

   df.to_excel(excel_file_path, sheet_name=excel_sheet, index=False)
   """  
   cleaned_df = df.drop(columns = ['STN_ID', 'LOCAL_DATE_VALUE', 'LOCAL_YEAR', 'LOCAL_DAY', 'LOCAL_HOUR', 'LOCAL_MINUTE', 'UTC_DATE_VALUE', 'MEAS_TYPE_ID', 'VALUE', 'FLAG', 'STATUS', 'SPATIAL_LOC_ID'])
   X = cleaned_df.drop(columns = ['Accurate'])

   # used for creating the model
   # y = cleaned_df['Accurate']

   # model = Model(X, y)
   # model.create_model()
   
   df['Accurate'] = Model.predict_data(X)

   df.to_excel(excel_file_path, sheet_name=excel_sheet, index=False)
   
   

else:
    print("Connection issue.")
