import pyodbc


# table retrieved from database by query
class Table:
    def __init__(self, columns, data, types=None):
        self.__columns = columns
        self.__data = data
        self.__types = types

    @property  # content values as tuple of tuple
    def Data(self):
        return self.__data

    @property  # column labels as tuple
    def Columns(self):
        return self.__columns

    @property  # field types as tuple
    def Types(self):
        return self.__types

    @property  # number of fields
    def ColsCount(self):
        return len(self.__columns)

    @property  # number of records retrieved
    def RowsCount(self):
        return len(self.__data)


class Database:
    def __init__(self, conn_str):
        self.__conn = pyodbc.connect(conn_str, autocommit=True)
        # ::check if connection succeeded

    def Close(self):
        self.__conn.close()

    @property
    def Connection(self):
        return self.__conn

    def GetQuery(self, query_str):
        cursor = self.Connection.cursor()
        cursor.execute(query_str)
        desc = cursor.description
        cols = []
        types = []
        for d in desc:
            cols.append(d[0])  # column label
            types.append(d[1])  # column value type
        records = cursor.fetchall()
        cursor.close()
        return Table(tuple(cols), tuple(records), tuple(types))

    def GetFullTable(self, table_name):
        return self.GetQuery('SELECT * FROM %s' % table_name)

    def RunQuery(self, query):
        cursor = self.Connection.cursor()
        cursor.execute(query)
        cursor.close()

