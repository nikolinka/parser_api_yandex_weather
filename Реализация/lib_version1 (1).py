import psycopg2

class SQL_connect :
    # Способ создания объекта (конструктор)
    def __init__(self, username, password,  database, port , host = '127.0.0.1'):         
        self.host= host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
    
    def PostgreSQL_connect(self):
        try:
            connection = psycopg2.connect(
                host = self.host,
                user = self.username,
                password = self.password,
                database = self.database)
            cursor = connection.cursor()
            print("successfully connected...")
            return connection, cursor
        except Exception as ex:
            print("Connection refused...")
            print(ex)
            
class SQL_request_INSERT:
    def __init__(self, connection, cursor, data):
        self.data = data
        self.cursor = cursor
        self.connection = connection   
        
    def CreateNewWeather(self):
        try:
            self.cursor.execute("select max(idweather) from telemetryweather;")
            id = self.cursor.fetchone()
            self.connection.commit()
            idweather = id[0]
            if (idweather == None):
                idweather = 1
            else:
                idweather = id[0]+1
            print (idweather)

            self.cursor.execute(f"select idobject from catalogobject where name = '{self.data[0]}';")
            id1 = self.cursor.fetchone()
            self.connection.commit()
            idobject = id1[0]

            self.cursor.execute(f"select idroute from catalogroute where route_number = '{self.data[1]}';")
            id2 = self.cursor.fetchone()
            self.connection.commit()
            idroute = id2[0]

            self.cursor.execute(f"select idstatus from catalogstatus where value = '{self.data[2]}';")
            id3 = self.cursor.fetchone()
            self.connection.commit()
            idstatus = id3[0]

            query = f"INSERT INTO telemetryweather (idweather, idobject, idroute, idstatus, recordtime, temperature, humidity, pressure, wind, sky, wave) VALUES ({idweather}, {idobject}, {idroute}, {idstatus}, {self.data[3]}, {self.data[4]}, {self.data[5]}, {self.data[6]}, {self.data[7]}, {self.data[8]}, {self.data[9]} );"
            self.cursor.execute(query)
            self.connection.commit()
            print('insert succesfully ')

            self.cursor.execute(f"SELECT * from telemetryweather WHERE idweather = {idweather};")
            data = self.cursor.fetchall()
            self.connection.commit()
            return data
        except Exception as ex:
            print("Request incorrect ...")
            print(ex)
