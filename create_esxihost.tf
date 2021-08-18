## Change the test_esxi_host to the name you wish to give for the new ESXi host you want to create
## replace the sddc_id to the OCID of your SDDC

resource "oci_ocvp_esxi_host" "test_esxi_host" {
    #Required
    sddc_id = "ocid1.vmwaresddc.oc1.eu-frankfurt-1.amaaaaaa6drgbxiat6sqhq6r3edxklrbvoyta44qjzake7wkoxlmiqvmtb3q"

    #Optional
    #defined_tags = {"Operations.CostCenter"= "42"}
    #display_name = var.esxi_host_display_name
    #freeform_tags = {"Department"= "Finance"}
}
 