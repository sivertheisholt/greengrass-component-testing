import sys
import time
import traceback
import requests

from awsiot.greengrasscoreipc.clientv2 import GreengrassCoreIPCClientV2
from awsiot.greengrasscoreipc.model import (
    UnauthorizedError,
    QOS
)

import json

def fetch_bitcoin_info():
    apiUri = "https://api.coindesk.com/v1/bpi/currentprice.json"
    res = requests.get(apiUri)
    return res.json()

def main():
    print('Starting to read bitcoin information')

    try:
        ipc_client = GreengrassCoreIPCClientV2()
        while True:
            bitcoinInfo = fetch_bitcoin_info()

            bitcoin = {
                "price": bitcoinInfo["bpi"]["EUR"]["rate"],
                "time": bitcoinInfo["time"]["updated"]
            }

            ipc_client.publish_to_iot_core(topic_name="bitcoin/info", payload=bytes(json.dumps(bitcoin), "utf-8"), qos=QOS.AT_LEAST_ONCE)
            time.sleep(60)

    except UnauthorizedError:
        print('Unauthorized error while publishing to topic.', file=sys.stderr)
        traceback.print_exc()
        exit(1)

    except Exception:
        print('Exception occurred', file=sys.stderr)
        traceback.print_exc()
        exit(1)

if __name__ == '__main__':
    main()
