import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

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
