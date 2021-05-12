import pprint
import sys

def get_or_default(dictionary, key, default=''):
    value = dictionary.get(key)
    if value:
        return value
    else:
        return default

def get_payload_data(payload):
  source = payload["source"]
  username = get_or_default(source, "username", "postgres")
  password = get_or_default(source, "password", "mysecretpassword")
  database = get_or_default(source, "database", "concourse-resource")
  table = get_or_default(source, "table", "records")
  host = source.get("host")
  port = source.get("port")
  connection_info = {
      "username": username,
      "password": password,
      "host": host,
      "port": port,
      "database": database,
      "table": table
  }
  return connection_info

def get_msg(msg, *args, **kwargs):
  if isinstance(msg, dict):
    pprint(msg, stream=sys.stderr)
  else:
    print(msg.format(*args, **kwargs), file=sys.stderr)