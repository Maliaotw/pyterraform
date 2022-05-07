# pyterraform

update 

With python use terraform build VM.

## setting

conf/variables.tf
```
provider "vsphere" {
  user           = ""
  password       = ""
  vsphere_server = ""

  # If you have a self-signed cert
  allow_unverified_ssl = true
}
```

 
conf/settings.py
```
# setting vsphere network
NETWORK = {
    '192.168.13': {
        'network': 'VLAN13',
        'gateway': '192.168.13.1'
    },
    '192.168.10': {
        'network': 'VLAN10',
        'gateway': '192.168.10.1'
    }
}
```

## Use

import
```
from terraform import Create,Delete,Update
```

Create VM
```
host95 = Create(hostname='vm-test90',ipaddress='192.168.13.90')
host96 = Create(hostname='vm-test91',ipaddress='192.168.10.91')
```

Update VM
```
host95 = Update(hostname='vm-test90',ipaddress='192.168.13.90',vcpu='1',memory='4096',disk_size='150')
```

Delete VM
```
host95 = Delete(hostname='vm-test90')
host96 = Delete(hostname='vm-test91')
```

## Simple Log
```
2019/12/18 16:21:13 root     INFO     vm-test90	Create	{'hostname': 'vm-test90', 'ipaddress': '192.168.13.90', 'network': 'VLAN13', 'gateway': '192.168.13.1'}
2019/12/18 16:21:17 root     INFO     vm-test90 terraform init
2019/12/18 16:21:20 root     INFO     vm-test90 plan ok
2019/12/18 16:22:50 root     INFO     vm-test90 complete ok
2019/12/18 16:22:50 root     INFO     vm-test90 valid ok
2019/12/18 16:22:50 root     INFO     vm-test91	Create	{'hostname': 'vm-test91', 'ipaddress': '192.168.10.91', 'network': 'VLAN10', 'gateway': '192.168.10.1'}
2019/12/18 16:22:55 root     INFO     vm-test91 terraform init
2019/12/18 16:22:58 root     INFO     vm-test91 plan ok
2019/12/18 16:24:41 root     INFO     vm-test91 complete ok
2019/12/18 16:24:41 root     INFO     vm-test91 valid ok
2019/12/18 16:32:20 root     INFO     vm-test90	Update	{'hostname': 'vm-test90', 'ipaddress': '192.168.13.90', 'vcpu': '1', 'memory': '4096', 'disk_size': '150', 'network': 'VLAN13', 'gateway': '192.168.13.1'}
2019/12/18 16:32:20 root     INFO     vm-test90 terraform init
2019/12/18 16:32:22 root     INFO     vm-test90 plan ok
2019/12/18 16:33:41 root     INFO     vm-test90 complete ok
2019/12/18 16:33:41 root     INFO     vm-test90 valid ok
2019/12/18 16:33:41 root     INFO     vm-test90	Delete	{'hostname': 'vm-test90'}
2019/12/18 16:33:41 root     INFO     vm-test90 terraform init
2019/12/18 16:33:43 root     INFO     vm-test90 plan ok
2019/12/18 16:33:51 root     INFO     vm-test90 complete ok
2019/12/18 16:33:51 root     INFO     vm-test90 valid ok
2019/12/18 16:33:51 root     INFO     vm-test91	Delete	{'hostname': 'vm-test91'}
2019/12/18 16:33:51 root     INFO     vm-test91 terraform init
2019/12/18 16:33:53 root     INFO     vm-test91 plan ok
2019/12/18 16:34:01 root     INFO     vm-test91 complete ok
2019/12/18 16:34:01 root     INFO     vm-test91 valid ok

```