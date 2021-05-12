import json
import sys
import psycopg2
from common import get_payload_data, get_msg

def _check(in_stream):
    payload = json.load(in_stream)
    connection_info = get_payload_data(payload)

    try:
        conn = psycopg2.connect(user=connection_info.get("username"),
                                  password=connection_info.get("password"),
                                  host=connection_info.get("host"),
                                  port=connection_info.get("port"),
                                  database=connection_info.get("database"))
        cursor = conn.cursor()
        postgreSQL_select_Query = "select * from {} where processed = false".format(connection_info.get("table"))
        cursor.execute(postgreSQL_select_Query)
        unprocessed_records = cursor.fetchall()
        result = []
        for record in unprocessed_records:
            result.append({
                "id":record[0],
                "name": record[1],
                "processed": record[2]
            })
        return {result: result}
    except (Exception, psycopg2.DatabaseError) as error:
        get_msg(str(error))
    
    finally:
        if conn is not None:
            conn.close()
            get_msg('Database connection closed.')

if __name__ == "__main__":
    print(json.dumps(_check(sys.stdin)))