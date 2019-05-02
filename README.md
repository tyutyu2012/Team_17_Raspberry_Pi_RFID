# Team_17_Raspberry_Pi_RFID

Instruction for Raspberry Pi and RFID 
1. Download the python code from the below 
2. Put the code into the Raspberry Pi 
4. On the code, replace #your_project_name with your project name url
5. On the terminal run 'python3 rfid.py' 
6. Scan the RFID for testing

//
1. "To return to normal Desktop, run these two commands:"
2. cd /home/pi/.config/lxsession/LXDE-pi\""
3. rm autostart\""
4. ***NOTE*** autostart file MUST be deleted, only emptying the content WILL cause problems"
5. The autostart file contains one line \"@lxterminal\""
6. Then, \"cd /home/pi/\""
7. \"nano .bashrc\""
8. "Then delete the lines \"echo Running at boot\" and \"sudo python /home/pi/rfid.py\""
9. "Then reboot"
10. "If you want to redo it, add the above deleted file with the one line"
11. "Then add the deleted two lines at the bottom of .bashrc"
12. "Starting program..."
