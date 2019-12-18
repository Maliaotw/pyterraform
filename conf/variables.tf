provider "vsphere" {
  user           = ""
  password       = ""
  vsphere_server = ""

  # If you have a self-signed cert
  allow_unverified_ssl = true
}

variable "template" {}
variable "dc" {}
variable "datastore" {}
variable "network" {}
variable "hostname" {}
variable "vcpu" {}
variable "memory" {}
variable "disk_size" {}
variable "domain" {}
variable "vsphere_resource_pool" {}
variable "ipaddress" {}
variable "netmask" {}
variable "gateway" {}
variable "dns" {}
