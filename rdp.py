import os

cmd = 'sudo apt update'
os.system(cmd)
cmd = 'sudo apt upgrade -y'
os.system(cmd)
cmd = 'sudo apt-get install --assume-yes ./chrome-remote-desktop_current_amd64.deb'
os.system(cmd)
cmd = 'sudo apt install --assume-yes  task-kde-desktop'
os.system(cmd)
cmd = 'sudo apt install xfce4-terminal -y'
os.system(cmd)
cmd = 'sudo apt install firefox-esr -y'
os.system(cmd)
cmd = 'sudo apt-get install geany -y'
os.system(cmd)
cmd = 'sudo apt install iputils-ping -y'
os.sytem(cmd)
print("vnc up")
