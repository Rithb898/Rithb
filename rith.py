import os

cmd = 'sudo apt update'
os.system(cmd)
cmd = 'sudo apt install --assume-yes wget tasksel'
os.system(cmd)
cmd = '[[ $(/usr/bin/lsb_release --codename --short) == "stretch" ]] && \'
os.system(cmd)
cmd = 'sudo apt install --assume-yes libgbm1/stretch-backports'
os.system(cmd)
cmd = 'wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb'
os.system(cmd)
cmd = 'sudo apt-get install --assume-yes ./chrome-remote-desktop_current_amd64.deb'
os.system(cmd)
cmd = 'sudo DEBIAN_FRONTEND=noninteractive \'
os.system(cmd)
cmd = 'sudo apt install --assume-yes xfce4 desktop-base dbus-x11 xscreensaver'
os.system(cmd)
cmd = 'sudo bash -c 'echo "exec /etc/X11/Xsession /usr/bin/xfce4-session" > /etc/chrome-remote-desktop-session'''
os.system(cmd)
cmd = 'sudo apt install --assume-yes task-xfce-desktop'
os.system(cmd)
cmd = 'sudo systemctl disable lightdm.service'
os.system(cmd)
cmd = 'wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'
os.system(cmd)
cmd = 'sudo apt install --assume-yes ./google-chrome-stable_current_amd64.deb'
os.system(cmd)
cmd = 'sudo apt update'
os.system(cmd)
print("vnc up")
