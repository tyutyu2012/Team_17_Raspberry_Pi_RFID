import sys, time, serial, json
from firebase import firebase
from datetime import datetime

firebase = firebase.FirebaseApplication('https://#your_project_name.firebaseio.com/')

def get_studentID(code):
    result = firebase.get('/RFID', code)
    print result
    return result

def get_studentName(code):
    result = firebase.get('/Students/' + str(code), "fName")
    print result
    return result

def get_studentStop(code):
    result = firebase.get('/Students/' + str(code), "Stop")
    print result
    return result

def set_onBoardStatus(stop, code):
    result = firebase.get('/Stops/' + str(stop) + '/Students/' + str(code), "onBoard")

    if not result:
        resultPut = firebase.put('/Stops/' + str(stop) + '/Students/' + str(code), "onBoard", True)
        print "on"
        return "on"
    elif result:
        resultPut = firebase.put('/Stops/' + str(stop) + '/Students/' + str(code), "onBoard", False)
        print "off"
        return "off"

def get_studentRoute(code):
    result = firebase.get('/Students/' + str(code), "Route")
    print result
    return result

def get_currentLat(bus):
    result = firebase.get('/Bus/' + str(bus) + '/currentLocation', "Latitude")
    print result
    return result

def get_currentLon(bus):
    result = firebase.get('/Bus/' + str(bus) + '/currentLocation', "Longitude")
    print result
    return result

print "To return to normal Desktop, run these two commands:"
print "\"cd /home/pi/.config/lxsessions/LXDE-pi\""
print "\"rm autostart\""
print "The autostart file contains one line \"@lxterminal\""
print "Starting program..."
time.sleep(10)
print "Program, started..."
while True:
    tag = raw_input("Waiting for RFID Tag... ")
    print "Tag = \"" + str(tag) + "\""

    studentID = get_studentID(tag)
    studentName = get_studentName(studentID)
    studentStop = get_studentStop(studentID)
    boardStatus = set_onBoardStatus(studentStop, studentID)
    studentRoute = get_studentRoute(studentID)
    currentLat = get_currentLat(studentRoute)
    currentLon = get_currentLon(studentRoute)
    print(datetime.now().strftime("%Y-%m-%d %H:%M"))

    data_to_upload = {
        'fName' : studentName,
        'Latitude' : currentLat,
        'Longitude' : currentLon,
        'boardStatus' : boardStatus,
        'Time' : datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    historyLog = firebase.post('/History/', data_to_upload)
    match = firebase.put('/Students/' + str(studentID) + '/History', historyLog["name"], True)
