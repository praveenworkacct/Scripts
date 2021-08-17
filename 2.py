import oci
config = oci.config.from_file("~/.oci/config","DEFAULT")
identity = oci.identity.IdentityClient(config)

# Initialize service client with default config file
ocvp_client = oci.ocvp.SddcClient(config)

#Send the request to service
get_sddc_response = ocvp_client.get_sddc(
    sddc_id="ocid1.vmwaresddc.oc1.ap-tokyo-1.amaaaaaap77apcqaaa53sqwtop2ddmqsmsf4s3z532ezgwnfyxtmh4qhh3bq",
    opc_request_id="X00UHVDUAHLL33XEQT8W<unique_ID>")

# Get the data from response
print(get_sddc_response.data) 