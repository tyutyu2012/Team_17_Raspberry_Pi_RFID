# Team_17_Raspberry_Pi_RFID

Instruction for Raspberry Pi and RFID 
1. Download the python code from the below 
2. Put the code into the Raspberry Pi 
4. On the code, replace #your_project_name with your project name url
5. On the terminal run 'python3 rfid.py' 
6. Scan the RFID for testing

1. "To return to normal Desktop, run these two commands:"
print "\"cd /home/pi/.config/lxsession/LXDE-pi\""
print "\"rm autostart\""
print "***NOTE*** autostart file MUST be deleted, only emptying the content WILL cause problems"
print "The autostart file contains one line \"@lxterminal\""
print "Then, \"cd /home/pi/\""
print "\"nano .bashrc\""
print "Then delete the lines \"echo Running at boot\" and \"sudo python /home/pi/rfid.py\""
print "Then reboot"
print "If you want to redo it, add the above deleted file with the one line"
print "Then add the deleted two lines at the bottom of .bashrc"
print "Starting program..."
