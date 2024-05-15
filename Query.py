import oracledb
import pandas as pd
import logging

class Query:
    def __init__(self):
        """
        Initialize a new instance of Query.

        Parameters:
        None
        """
        self.driver = 'oracle'
        self.ARKEON_host = 'ARC-CLUSTER.CMC.EC.GC.CA'
        self.ARKEON_port = '1521'
        self.ARKEON_service = 'archive.cmc.ec.gc.ca'

    def connect(self, usern, passw):
        """
        Connect to database.

        Parameters:
        usern: Username that the user entered.
        passw: Password that the user entered.

        Returns:
        src_conn, bool: The connection to the database and True if the connection was successful. Else it returns None, False.
        """
        try:
            src_conn = oracledb.connect(
                user = usern,
                password = passw,
                host = self.ARKEON_host,
                port = self.ARKEON_port,
                service_name = self.ARKEON_service
            )
            return src_conn, True
        except oracledb.DatabaseError as err:
            error, = err.args
            logging.error('Unable to establish connection, due to: %s', error.message)
            return None, False


    def get_value(self, connection, id, yr, mo, day, meas):
        """
        Turn the SQL query into a DataFrame.

        Parameters:
        connection: The arkeon connection.
        id: The station id.
        yr: The year.
        mo: The month.
        day: The day.
        meas: The MEAS_TYPE_ID.

        Returns:
        pd.DataFrame(rows, columns = column_headers): A DataFrame of the normals query, and returns None if it is an empty dataframe.
        """
        if connection is None:
            logging.error('No database connection established.')
            return None
        
        query =\
        '''
        SELECT
            *
        FROM
            archive.obs_data  
        WHERE
            STN_ID = :id AND
            LOCAL_YEAR = :yr AND
            LOCAL_MONTH = :mo AND
            LOCAL_DAY = :day AND 
            MEAS_TYPE_ID = :meas

        '''
        

        cursor = connection.cursor()

        if cursor is not None:
            logging.info('Executing query...')
            logging.info(query)
            try:
                cursor.execute(query, id=id, yr=yr, mo=mo, day=day, meas=meas)
            except Exception as err:
                msg = 'Unable to execute query, due to: %s' % str(err)
                logging.error(msg)
                return None
            logging.info('Query execution complete.')
        else:
            logging.error('Unable to execute query, due to: no cursor.')
            return None
        
        column_headers = [desc[0] for desc in cursor.description]
        rows = []
        for row in cursor:
            rows.append(row)
            
        cursor.close()
        logging.info('Cursor closed.')

        if len(rows) == 0:  
            return None
        else:
            return pd.DataFrame(rows, columns=column_headers)
