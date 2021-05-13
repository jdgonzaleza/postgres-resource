import json
import psycopg2
import sys
from common import get_payload_data, get_msg

def _in(in_stream):
    payload = json.load(in_stream)
    return run(payload)

def run(payload):
    connection_info = get_payload_data(payload)
    try:
        conn = psycopg2.connect(user=connection_info.get("username"),
                                  password=connection_info.get("password"),
                                  host=connection_info.get("host"),
                                  port=connection_info.get("port"),
                                  database=connection_info.get("database"))
        cursor = conn.cursor()
        records_to_be_seen = payload.get('version')
        cursor.execute("UPDATE records SET seen = {} WHERE id = {}".format("true", records_to_be_seen.get('version')))
        conn.commit()                  
        return {"results": records_to_be_seen}
    except (Exception, psycopg2.DatabaseError) as error:
        get_msg(str(error))
         
    finally:
        if conn is not None:
            conn.close()
            get_msg('Database connection closed.')

if __name__ == "__main__":
    print(json.dumps(_in(sys.stdin, sys.argv[1])))