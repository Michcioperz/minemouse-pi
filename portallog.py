#!/usr/bin/env python2
import random, subprocess

init = {
    "Hi.":"",
    "Target acquired.":"",
    "Firing.":"",
    "Hello friend.":"",
    "Gotcha.":"",
    "There you are.":"",
    "I see you.":"",
}

scan = {
    "Searching.":"",
    "Is anyone there?":"",
    "Who's there?":"",
}

die = {
    "Goodbye.":"",
    "Sleep mode activated.":"",
    "Hibernating.":"",
    "Goodnight.":"",
    "Resting.":"",
    "Nap time.":"",
    "Target lost.":"",
    "Critical error.":"",
    "Shutting down.":"",
    "I don't blame you.":"",
    "I don't hate you.":"",
    "Whyyyy.":"",
    "No hard feelings.":"",
    "Vital testing apparatus destroyed.":"",
}

move = {
    "Coming through.":"",
    "Could you come over here?":"",
    "Deploying.":""
}

# TODO: assign corresponding Portal sound files

def sayInit():
    cotsg = random.choice(init)
    if len(init[cotsg]) > 0:
        subprocess.Popen(['omxplayer',cotsg])
    return cotsg

def sayScan():
    cotsg = random.choice(scan)
    if len(scan[cotsg]) > 0:
        subprocess.Popen(['omxplayer',cotsg])
    return cotsg

def sayDie():
    cotsg = random.choice(die)
    if len(die[cotsg]) > 0:
        subprocess.Popen(['omxplayer',cotsg])
    return cotsg

def sayMove():
    cotsg = random.choice(move)
    if len(move[cotsg]) > 0:
        subprocess.Popen(['omxplayer',cotsg])
    return cotsg
