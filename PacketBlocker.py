import os, time
receiverMac = "00:00:00:00:00:00"
receiverIp = "192.168.1.1"
subnet = "24"
senderIp = "192.168.1.2"
os.popen("sudo ifconfig eth0 down")
time.sleep(0.5)
print("eth0 down")
os.popen("sudo macchanger eth0 -m " + receiverMac)
time.sleep(0.5)
print("Mac address set to: "+receiverMac)
os.popen("sudo ifconfig eth0 up")
os.popen("sudo ifconfig eth0 " + receiverIp + "/" + subnet)
time.sleep(0.5)
os.system("ping " + senderIp + " -i 0.05")