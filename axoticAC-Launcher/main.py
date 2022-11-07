import glob
import os
import threading
from winreg import *
import urllib.request
import re
import requests
import psutil

run = True
installPath = ''
ip = ''
steamid = ''


def setInterval(func, time):
    e = threading.Event()
    while not e.wait(time):
        func()


def scanner():
    print("Beginne Scan...")
    print("ip", ip)
    print("steamID", steamid)
    verified = bool(True)
    os.chdir(installPath)
    for file in glob.glob("*.dll"):
        if file == "d3d10.dll":
            print("File gefunden: ", file)
            verified = False

    if verified:
        print("Verifiziert")
    else:
        print("Cheat erkannt!")

    response = requests.post('http://45.157.235.201:8000/scan', json={'steamid': steamid, 'ip': ip, 'verify': verified})


def getInstallPath():
    return getRegistryEntry("SOFTWARE\Wow6432Node\Rockstar Games\Grand Theft Auto V", 'InstallFolder')


def getSteamID():
    steampath = getRegistryEntry("SOFTWARE\WOW6432Node\Valve\Steam", 'InstallPath')
    IDPath = open(steampath + "\config\loginusers.vdf")
    file = IDPath.read()
    nameregex = re.search(r'[0-9]{10,}', file)
    if nameregex:  # If there is a match
        steamid = nameregex.group()
        return hex(int(steamid))[2:]


def getIP():
    return urllib.request.urlopen('http://45.157.235.201:8000/ip').read().decode('utf8').replace('"', '')


def getRegistryEntry(path: str, keyName: str):
    aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    aKey = OpenKey(aReg, path)
    registryValue = ''
    try:
        i = 0
        while 1:
            name, value, type = EnumValue(aKey, i)
            if name == keyName:
                registryValue = value
            i += 1

    except WindowsError:
        print("END")

    CloseKey(aKey)
    return registryValue


# def checkForUSB():


def getProccess():
    for proc in psutil.process_iter():
        try:
            # this returns the list of opened files by the current process
            try:
                oldPIDs = []
                if "FiveM_ChromeBrowser" in proc.name():
                    oldPIDs.append(proc.pid)
                    print(oldPIDs)
                    # --> check if the pid has changed

                #         return
                    #     p = psutil.Process(proc.pid)
                    #     print(len(p.memory_maps()))
                    # for dll in p.memory_maps():
                    #     print(dll.path)

                    # flist = proc.open_files()
                    # if flist:
                    #     for nt in flist:

                            # if "Session Storage" in nt.path:
                            #     if "context-server" in nt.path:
                            #         print("\t", nt.path, proc.name())
            except:
                la = 1
                print("test")

        # This catches a race condition where a process ends
        # before we can examine its files
        except psutil.NoSuchProcess as err:
            print("****", err)
    while 1:
        if proc.pid not in oldPIDs:
            print("eine pid ist nicht mehr gleich")
            return

# getProccess()
steamid = getSteamID()
ip = getIP()
installPath = getInstallPath()
setInterval(scanner, 10)
