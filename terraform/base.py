import os
import subprocess
import re
from conf import settings
import logging


class Base:
    BASE_DIR = settings.BASE_DIR
    status = False

    @property
    def hostname(self):
        hostname = self.vars.get('hostname')
        if hostname:
            return hostname
        else:
            raise Exception("no hostname")

    @property
    def path(self):
        data = {
            'base': self.BASE_DIR,
            'conf': os.path.join(self.BASE_DIR, 'conf'),
            'files': os.path.join(self.BASE_DIR, 'files'),
            'host': os.path.join(self.BASE_DIR, 'files', self.hostname)
        }
        return data

    def create_host_dir(self):
        if os.path.exists(self.path['host']):
            # print("更新host目錄")
            pass
        else:
            # print("新建host目錄")
            os.mkdir(self.path['host'])


class Network:

    def get_vars(self,ip):

        for key in settings.NETWORK.keys():
            if key in ip:
                return settings.NETWORK.get(key)



class Terraform(Base,Network):

    def __init__(self, **kwargs):
        '''
        hostname='vm-test87',ipaddress='192.168.10.87'
        '''

        self.vars = kwargs
        ipaddress = self.vars.get('ipaddress')
        if ipaddress:
            net_vars = self.get_vars(ipaddress)
            self.vars.update(net_vars)

        logging.info("%s\t%s\t%s" % (self.hostname, self.__class__.__name__,kwargs))
        self.run()

    def run(self):
        pass

    def complete(self,ret):
        if 'complete' in ret:
            logging.info('%s complete ok' % self.hostname)
        else:
            logging.info('%s complete error' % self.hostname)
            logging.error(ret)
            raise Exception("complete 錯誤")


    def valid(self, ret):
        string = re.findall('Resources:.(.*)\.', ret)[0]
        num = re.findall('(\d+).%s' % self.valid_text, string)[0]
        if int(num) != 0:
            logging.info('%s valid ok' % self.hostname)
            return True
        else:
            logging.error('%s valid error' % self.hostname)
            raise Exception("valid 錯誤")


    def _init(self):
        os.chdir(self.path['host'])
        subprocess.getoutput('terraform init')
        logging.info('%s terraform init' % self.hostname)

    def _plan(self):
        ret = subprocess.getoutput('terraform plan')
        plan_string = re.findall('Plan:\S+(.*)\.', ret)[0]
        num = re.findall('(\d+).to %s' % self.valid_text, plan_string)[0]

        if int(num) != 0:
            logging.info('%s plan ok' % self.hostname)
        else:
            logging.error('%s plan error' % self.hostname)
            raise Exception("plan 錯誤")


    def _main(self):
        ret = subprocess.getoutput(self.command)
        self.complete(ret)
        self.valid(ret)





