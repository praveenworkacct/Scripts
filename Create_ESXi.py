# This will create a ESXi host. You need to enter the SDDC ID and the display name(dname is not mandatory).

import oci
import sys


config = oci.config.from_file("~/.oci/config","DEFAULT")
identity = oci.identity.IdentityClient(config)


# Initialize service client with default config file
ocvp_client = oci.ocvp.EsxiHostClient(config)


#Take user inputs | This will prompt the user to request the details of ESXi host

sid = input("Enter the SDDC OCID:")
dname = input("Enter the name for your ESXi host:")
print("The SDDC you provided is ", sid)
print("The name of the ESXi host is :", dname)


# Send the request to service, some parameters are not required, see API
# doc for more info
create_esxi_host_response = ocvp_client.create_esxi_host(
    create_esxi_host_details=oci.ocvp.models.CreateEsxiHostDetails(
        sddc_id=sid,
        display_name=dname,
        #current_sku="THREE_YEARS",
        #next_sku="HOUR",
        #freeform_tags={
            #'EXAMPLE_KEY_gqIIr': 'EXAMPLE_VALUE_EDoSvyyC4dRVMfSPaErN'},
        #defined_tags={
        #    'EXAMPLE_KEY_MWQzl': {
        #        'EXAMPLE_KEY_Wc0Rz': 'EXAMPLE--Value'}}),
    ))
    #opc_retry_token="EXAMPLE-opcRetryToken-Value",
    #opc_request_id="1HAC6O2RTMND9PFVAFRK<unique_ID>")

# Get the data from response
print(create_esxi_host_response.headers)
