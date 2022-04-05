import mysql.connector

def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
    host="localhost",
    user="lucy",
    password="password123",
    database="MBTAdb"
    )

    mycursor = mydb.cursor()
    #complete the following line to add all the fields from the table
    sql = "insert into mbta_buses (id, longitude, latitude, direction_id, occupancy_status, current_status, current_stop_sequence, updated_at) values (%s, %s, %s, %s, %s, %s, %s, %s)"
    for mbtaDict in mbtaList:
        #complete the following line to add all the fields from the table
        val = (mbtaDict['id'], mbtaDict['longitude'], mbtaDict['latitude'], mbtaDict['direction_id'], mbtaDict['occupancy_status'], mbtaDict['current_status'], mbtaDict['current_stop_sequence'], mbtaDict['updated_at'])
        mycursor.execute(sql, val)

    mydb.commit()