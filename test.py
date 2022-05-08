from terraform import Create, Delete, Update, CustomIPCreate

# Create VM

host95 = Create(
    hostname='vm-test90',
    ipaddress='192.168.13.90',
    vcenter_server='vcenter_server',
    vcenter_user='vcenter_server',
    vcenter_pass='vcenter_pass'
)
host96 = Create(hostname='vm-test91', ipaddress='192.168.13.91')
host97 = Create(hostname='vm-test92', ipaddress='192.168.10.90')

# CustomIPCreate

CustomIPCreate()

# Update VM
# host95 = Update(hostname='vm-test90',ipaddress='192.168.13.90',vcpu='1',memory='4096',disk_size='150')
#
# # Delete VM
# host95 = Delete(hostname='vm-test90')
# host96 = Delete(hostname='vm-test91')
