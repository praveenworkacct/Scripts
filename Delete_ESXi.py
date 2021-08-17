#This script will delete the ESXi host. Input the ESXi host OCID

import oci
import sys

# Create a default config using DEFAULT profile in default location
config = oci.config.from_file()


# Initialize service client with default config file
ocvp_client = oci.ocvp.EsxiHostClient(config)


sid = input("Enter the SDDC OCID:")
print("The OCID of the ESXi that you want to delete is:", sid)

# Send the request to service, some parameters are not required, see API
# doc for more info
delete_esxi_host_response = ocvp_client.delete_esxi_host(
    esxi_host_id=sid,
    if_match="EXAMPLE-ifMatch-Value",
    opc_request_id="LQZOYKRPO0YBOXSHIK4F<unique_ID>")

# Get the data from response
print(delete_esxi_host_response.headers)