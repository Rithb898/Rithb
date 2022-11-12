import os

cmd = 'sudo apt update'
os.system(cmd)
cmd = 'sudo apt-get install --assume-yes ./chrome-remote-desktop_current_amd64.deb'
os.system(cmd)
cmd = 'sudo apt install --assume-yes task-gnome-desktop desktop-base dbus-x11 xscreensaver'
os.system(cmd)
print("vnc up")
