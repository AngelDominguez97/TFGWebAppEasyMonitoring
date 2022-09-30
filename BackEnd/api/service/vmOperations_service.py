from ctypes import memmove
from shutil import disk_usage
from urllib import response
from xmlrpc.client import ResponseError
from paramiko import SSHClient
import paramiko
from api.utils.settings import EnvVariables
from api.utils.operations_util import Utils
import psutil

envVariables = EnvVariables()

VM_USERNAME = envVariables.vm_username
VM_PASSWORD = envVariables.vm_password
client = SSHClient()

def rebootMachineByIP(ip: str):
    command = 'reboot'
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=VM_USERNAME, password=VM_PASSWORD)
    response = client.exec_command('echo %s|sudo -S %s' % (VM_PASSWORD, command))
    return response


def getCPUInfo():
    cpuPercent = psutil.cpu_percent(interval=1)
    cpuCount = psutil.cpu_count()
    response = str(cpuCount) + "CPU, Average load " + str(cpuPercent) + "% < 80%: OK"
    return response

def getMemmoryInfo():
    memmoryUsage = psutil.virtual_memory()
    freeMemmory = Utils.getGbByBytes(memmoryUsage.free)
    availableMemmory = Utils.getGbByBytes(memmoryUsage.available)
    totalMemmory = Utils.getGbByBytes(memmoryUsage.total)
    cachedMemmory = Utils.getGbByBytes(memmoryUsage.cached)
    response = str(memmoryUsage.percent) + "% < 85%: OK, " + str(freeMemmory) + " Gb free, " + str(availableMemmory) + "Gb available, " + str(totalMemmory) + " Gb total, " + str(cachedMemmory) + " Gb cached"
    return response 

def getDiskInfo():
    diskUsage = psutil.disk_usage('/')
    totalDisk = Utils.getGbByBytes(diskUsage.total)
    freeDisk = Utils.getGbByBytes(diskUsage.free)
    usedDisk = Utils.getGbByBytes(diskUsage.used)
    response = str(diskUsage.percent) + "% < 90%: OK, " + str(freeDisk) + " Gb free, " + str(usedDisk) + "Gb used, " + str(totalDisk) + " Gb total"
    return response

def getNetworkInfo():
    netInfo = psutil.net_io_counters()
    response = str(netInfo.bytes_sent) + " bytes sent, " + str(netInfo.bytes_recv) + " bytes recived, " + str(netInfo.packets_sent) + " packets sent, " + str(netInfo.packets_recv) + " packets recived"
    return response

#para hacer un ping seria response = os.system("ping -c 1 " + hostname), siendo 0 false y sino true
