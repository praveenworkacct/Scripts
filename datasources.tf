
## Enter the esxi host OCID to terminalte the ESXi host from the SDDC cluster

data "oci_ocvp_esxi_host" "OCVS-Demo1-1" {
    #Required
    esxi_host_id = "ocid1.instance.oc1.eu-frankfurt-1.antheljs6drgbxicldzoidau5ph7euuw65eab62zh2j4mbhyyqfvy5u556zq"
}