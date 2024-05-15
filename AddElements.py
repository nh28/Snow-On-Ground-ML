import pandas as pd
from datetime import datetime, timedelta

class AddElements:
   
    @staticmethod
    def add(query, row, connection, a, b, c, d, e, f, g, h, i, j):
        """
        Fill in the input row by fething data from the archive based on the station, year, day, month, and meas type id.

        Parameters:
        query: A Query object used to access ARKEON.
        row: The given row in the excel file.
        connection: The connection to ARKON needed to use query.
        a: Max Temp MEAS_TYPE_ID.
        b: Min Temp MEAS_TYPE_ID.
        c: Mean Temp MEAS_TYPE_ID.
        d: Total Rain MEAS_TYPE_ID.
        e: Total Snow MEAS_TYPE_ID.
        f: Total Precipitation MEAS_TYPE_ID.
        g: 	Snow on Grnd MEAS_TYPE_ID.
        h: DLY04 Snow MEAS_TYPE_ID.
        i: DLY02 Snow MEAS_TYPE_ID.
        j: DLY44 Snow MEAS_TYPE_ID.


        Returns:
        row: The filled in row with all the information from ARKEON.
        """
        try:
            station = row['STN_ID']
            year = row['LOCAL_YEAR']
            day = row['LOCAL_DAY']
            month = row['LOCAL_MONTH']
            date = datetime.strptime(row['LOCAL_DATE_VALUE'].strftime('%m/%d/%Y'), '%m/%d/%Y')
            day_1_before = date - timedelta(days=1)
            day_2_before = date - timedelta(days=2)
            day_3_before = date - timedelta(days=3)
            day_1_after = date + timedelta(days=1)
            day_2_after = date + timedelta(days=2)
            day_3_after = date + timedelta(days=3)
            
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
                value = query.get_value(connection, station, day_1_after.year, day_1_after.month, day_1_after.day, g)
                row['Snow on Grnd +1'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Snow on Grnd +1: {e}")
                row['Snow on Grnd +1'] = None
            
            try:
                value = query.get_value(connection, station, day_2_after.year, day_2_after.month, day_2_after.day, g)
                row['Snow on Grnd +2'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Snow on Grnd +2: {e}")
                row['Snow on Grnd +2'] = None
            
            try:
                value = query.get_value(connection, station, day_3_after.year, day_3_after.month, day_3_after.day, g)
                row['Snow on Grnd +3'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Snow on Grnd +3: {e}")
                row['Snow on Grnd +3'] = None
            
            try:
                value = query.get_value(connection, station, year, month, day, 1982)
                row['Drizzle'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Drizzle: {e}")
                row['Drizzle'] = None
            
            """ No Data
            try:
                value = query.get_value(connection, station, year, month, day, 1984)
                row['Freezing Drizzle'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Freezing Drizzle: {e}")
                row['Freezing Drizzle'] = None
            """

            try:
                value = query.get_value(connection, station, year, month, day, 1980)
                row['Rain'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Rain: {e}")
                row['Rain'] = None

            try:
                value = query.get_value(connection, station, year, month, day, 1983)
                row['Freezing Rain'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Freezing Rain: {e}")
                row['Freezing Rain'] = None
            
            try:
                value = query.get_value(connection, station, year, month, day, 1985)
                row['Snow'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Snow: {e}")
                row['Snow'] = None

            try:
                value = query.get_value(connection, station, year, month, day, 1986)
                row['Snow Grains'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Snow Grains: {e}")
                row['Snow Grains'] = None

            try:
                value = query.get_value(connection, station, year, month, day, 1988)
                row['Ice Pellets'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Ice Pellets: {e}")
                row['Ice Pellets'] = None

            try:
                value = query.get_value(connection, station, year, month, day, 1981)
                row['Rain Showers'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Rain Showers: {e}")
                row['Rain Showers'] = None

            try:
                value = query.get_value(connection, station, year, month, day, 1990)
                row['Snow Showers'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Snow Showers: {e}")
                row['Snow Showers'] = None

            try:
                value = query.get_value(connection, station, year, month, day, 1992)
                row['Hail'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Hail: {e}")
                row['Hail'] = None

            try:
                value = query.get_value(connection, station, year, month, day, 1997)
                row['Blowing Snow'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Blowing Snow: {e}")
                row['Blowing Snow'] = None

            try:
                value = query.get_value(connection, station, year, month, day, 1979)
                row['Thunderstorm'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Thunderstorm: {e}")
                row['Thunderstorm'] = None

            try:
                value = query.get_value(connection, station, year, month, day, 1991)
                row['Snow Pellet'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Snow Pellet: {e}")
                row['Snow Pellet'] = None

            try:
                value = query.get_value(connection, station, year, month, day, 1989)
                row['Ice Pellet Showers'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Ice Pellet Showers: {e}")
                row['Ice Pellet Showers'] = None
            
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
