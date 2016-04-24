import subprocess
from pprint import pprint

import time

import subcommand
from elasticsearch import Elasticsearch

es = Elasticsearch('search-dungeon-qcc7an54euyyq4vnstm2j673ve.us-east-1.es.amazonaws.com:80')

while True:
    result = es.search(index="dungeon", doc_type="sensor_record",
                       body={"query": {"range": {"_timestamp": {"gte": "now-5s", "lte": "now"}}},
                             "filter": {"or": [{"range": {"distance": {"gt": 0}}}, {"range": {"distance2": {"gt": 0}}}]}})
    # pprint(result)
    if result['hits']['total']:
        print subprocess.check_output(["/usr/bin/say", "Amen"])

    time.sleep(1)

