import os
import sys
import time
import traceback

from awsiot.greengrasscoreipc.clientv2 import GreengrassCoreIPCClientV2

from entities.lidar import Lidar
from services.lidar_service import LidarService

from dotenv import load_dotenv
load_dotenv()

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: Module %(module)s :: Line No %(lineno)s :: %(message)s')

def add_lidars(ip_addresses):
    return [Lidar(address) for address in ip_addresses]

def main():
    logging.info("Starting fetching lidar data")

    # Handling environment
    args = sys.argv[1:]
    py_env = "dev"
    ip_addresses = []
    ipc_client = None
    
    print(os.environ.get('ENVIRONMENT'))

    print("PRINTING STUFF")
    print(args)
    print(len(args))

    if len(args) != 0:
        py_env = "prod"
        ip_addresses = str(args[1]).split(";")
        ipc_client = GreengrassCoreIPCClientV2()
    else:
        ip_addresses = os.getenv("LIDAR_IPS").split(";")

    try:
        lidars = add_lidars(ip_addresses)
        lidar_service = LidarService(lidars, ipc_client, py_env)

        while True:
            lidar_service.run_data_handling()
            time.sleep(15)

    except Exception as e:
        logging.error("An error occurred: %s", e)
        traceback.print_exception()
        exit(1)

if __name__ == '__main__':
    main()