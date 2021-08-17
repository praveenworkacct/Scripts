#This will pull the SDDC information and put it in a file.

import oci
import sys

config = oci.config.from_file("~/.oci/config","DEFAULT")
identity = oci.identity.IdentityClient(config)

# Initialize service client with default config file
ocvp_client = oci.ocvp.SddcClient(config)


#Take user inputs | This will prompt the user to enter the SDDC OCID
id = input("Enter the SDDC OCID:")
print("The provided SDDC ID is:", id)

#Send the request to service
get_sddc_response = ocvp_client.get_sddc(
    sddc_id=id,
    opc_request_id="X00UHVDUAHLL33XEQT8W<unique_ID>")


#Better to mention the path here
sys.stdout = open("output.csv", "w")
# Get the data from response
print(get_sddc_response.data) 
sys.stdout.close()