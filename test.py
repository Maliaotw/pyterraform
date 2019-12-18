
from terraform import Create,Delete,Update

# Create VM

host95 = Create(hostname='vm-test90',ipaddress='192.168.13.90')
host96 = Create(hostname='vm-test91',ipaddress='192.168.13.91')
host97 = Create(hostname='vm-test92',ipaddress='192.168.10.90')

# Update VM
# host95 = Update(hostname='vm-test90',ipaddress='192.168.13.90',vcpu='1',memory='4096',disk_size='150')
#
# # Delete VM
# host95 = Delete(hostname='vm-test90')
# host96 = Delete(hostname='vm-test91')

