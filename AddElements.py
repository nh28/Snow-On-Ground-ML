import pandas as pd
from datetime import datetime, timedelta

class AddElements:
   
    @staticmethod
    def add(query, row, connection, a, b, c, d, e, f, g, h, i, j):
        try:
            station = row['STN_ID']
            year = row['LOCAL_YEAR']
            day = row['LOCAL_DAY']
            month = row['LOCAL_MONTH']
            date = datetime.strptime(row['LOCAL_DATE_VALUE'].strftime('%m/%d/%Y'), '%m/%d/%Y')
            day_1_before = date - timedelta(days=1)
            day_2_before = date - timedelta(days=2)
            day_3_before = date - timedelta(days=3)

            try:
                value = query.get_value(connection, station, year, month, day, a)
                row['Max Temp'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Max Temp: {e}")
                row['Max Temp'] = None
            
            try:
                value = query.get_value(connection, station, year, month, day, b)
                row['Min Temp'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Min Temp: {e}")
                row['Min Temp'] = None
            
            try:
                value = query.get_value(connection, station, year, month, day, c)
                row['Mean Temp'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Mean Temp: {e}")
                row['Mean Temp'] = None
            
            try:
                value = query.get_value(connection, station, year, month, day, d)
                row['Total Rain'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Total Rain: {e}")
                row['Total Rain'] = None
            
            try:
                value = query.get_value(connection, station, year, month, day, e)
                row['Total Snow'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Total Snow: {e}")
                row['Total Snow'] = None
            
            try:
                value = query.get_value(connection, station, year, month, day, f)
                row['Total Precipitation'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Total Precipitation: {e}")
                row['Total Precipitation'] = None
            
            try:
                value = query.get_value(connection, station, day_1_before.year, day_1_before.month, day_1_before.day, g)
                row['Snow on Grnd -1'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Snow on Grnd -1: {e}")
                row['Snow on Grnd -1'] = None
            
            try:
                value = query.get_value(connection, station, day_2_before.year, day_2_before.month, day_2_before.day, g)
                row['Snow on Grnd -2'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Snow on Grnd -2: {e}")
                row['Snow on Grnd -2'] = None
            
            try:
                value = query.get_value(connection, station, day_3_before.year, day_3_before.month, day_3_before.day, g)
                row['Snow on Grnd -3'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Snow on Grnd -3: {e}")
                row['Snow on Grnd -3'] = None
            
            try:
                value = query.get_value(connection, station, year, month, day, h)
                row['DLY04 Snow'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching DLY04 Snow: {e}")
                row['DLY04 Snow'] = None
            
            try:
                value = query.get_value(connection, station, year, month, day, i)
                row['DLY02 Snow'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching DLY02 Snow: {e}")
                row['DLY02 Snow'] = None
            
            try:
                value = query.get_value(connection, station, year, month, day, j)
                row['DLY44 Snow'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching DLY44 Snow: {e}")
                row['DLY44 Snow'] = None
        
        except Exception as e:
            print(f"Error processing row: {e}")
            # Handle any other errors that may occur during row processing
        
        return row
