# Simple scheduler
# Samuel Yvon
# Projet IOTVenstar
import os
import re
import json
import time
import sys

currentPath = os.path.dirname(os.path.realpath(__file__))
targetPath = currentPath + "/Target"


class Schedule(object):
    taskName = ""
    path = ""
    interval = 0
    lastRan = 0
    selfPath = ""

    def __init__(self, taskname, path, interval, lastRan):
        self.taskName = taskname
        self.path = path
        self.interval = interval
        self.lastRan = lastRan

    def needtorun(self):
        now = round(time.time())
        if now >= (self.lastRan + self.interval):
            return True
        else:
            return False

    def timeBeforeRun(self):
        now = round(time.time())
        return (self.lastRan + self.interval) - now

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def run(self):
        if self.needtorun():
            script = targetPath + "/" + self.path
            print('----- Beginning of execution ------')
            print("Running " + self.taskName)
            with open(script) as f:
                code = compile(f.read(), script, 'exec')
                print(exec(code))
                print('------ end of execution ------')
            self.lastRan = round(time.time())
            fo = open(self.selfPath, "w")
            fo.write(self.to_JSON())
            fo.close()


def schedule_decoder(jsonData):
    return Schedule(jsonData["taskName"], jsonData["path"], jsonData["interval"], jsonData["lastRan"])


while True:
    lowestTime = sys.maxsize
    for file in os.listdir(targetPath):
        isSchedule = re.match("[\w]*\.schedule\.json", file)
        if isSchedule:
            with open(targetPath + "/" + file, 'r') as scheduleObject:
                data = scheduleObject.read()
                scheduleObject.close()
                try:
                    schedule = json.loads(data, object_hook=schedule_decoder)
                    schedule.selfPath = targetPath + "/" + file
                    if schedule.needtorun():
                        schedule.run()
                    if schedule.timeBeforeRun() < lowestTime:
                        lowestTime = schedule.timeBeforeRun()


                except Exception as e:
                    print(e)
                    print('Couldn''t parse json')
    timeToSleep = max(lowestTime - 1, 0)
    if timeToSleep > 0:
        print("Sleeping for " + str(timeToSleep) + " seconds")
        time.sleep(timeToSleep)
