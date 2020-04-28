from lists import friilist
import random
import sys
import time
import requests

pasteplace = None
finished = 0
def save():
    done = False
    save = input("save? (Y/N) ")
    while done == False:
        if save.lower() == "n" or save.lower() == "no":
            done = True
        elif save.lower() == "y" or save.lower() == "yes":
            thisorthat = input("Would you like to save your team as a pokepaste or txt? ")
            while done == False: 
                if thisorthat.lower() == "pokepaste" or thisorthat.lower() == "pokepastes" or thisorthat.lower() == "pokepast.es" or thisorthat.lower() == "p":
                    print("\nWorking, sorry for the wait ")
                    savetoPokepastes()
                    ph = input("Are you done? (y/n) ")
                    if ph.lower() == "true" or ph.lower() == "t" or ph.lower() == "y" or ph.lower() == "yes":
                        done = True
                elif thisorthat.lower() == "txt" or thisorthat.lower() == "t" or thisorthat.lower() == "text":
                    savefile()
                    ph = input("Are you done? (y/n) ")
                    if ph.lower() == "true" or ph.lower() == "t" or ph.lower() == "y" or ph.lower() == "yes":
                        done = True
                else:
                    thisorthat = input("Would you like to save your team as a pokepaste or txt? ")
        else:
            save = input("save? (Y/N) ")
def parser(stri):
    try:
        if int(stri) > 0:
            return True
        else:
            print("""MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWWWNNNNNNNNNNNNWWWMMMMMMMMMMMMM
MMMMMMMMMMMMMMWWNXXKK00000000000000KKKXNWWMMMMMMMM
MMMMMMMMMMMWNXK00000O000OOOO0000000000000KXNWMMMMM
MMMMMMMMMWXK00000000000O0000000000000O0000O0KNWMMM
MMMMMMMWXK00O000OOxxxkO00O00000OOO000O00Odc:ccokXM
MMMMMWNK000O0OOdc::cc:cxO00000OO0000000Oo,:dkxl;ck
MMMMNX000000Od:;cdkOOo,ck000O0OO0000000Oo,cO000kc,
MMWNK00000Oxc;lkO000kl,lO000000000000000kc,lO000Ol
MMNK00000Od;:dO000Ox:;oO000O0OO0000000000k:,d0000O
MNK00000Od;:xO0000k:';ldkOO00000000000000Oo,lO00O0
WX000000k:;x00000Ol,co:;;;:lxO00O000000OOxl,:k0O00
NK00000Oo,cO00000x;;olc:,'...;ok0000Okdc;,;,;x0O00
X0OO0Oxl;ck0O000Ol,lxolllllllcok0000Ol,'',;,,lO000
K0Okdc;:dO000OOkl,ck000000000000OO00Okkkxxdo:,lkO0
00OxllxO0000Oxo:;okO0000OOOOOOO000000OOO0000ko;:ok
0000O0000Okdc;:okO00Oxoc::;;;;cldxdlc::coxO00Okl;:
00O0000Odc::lxO000Ox:'..,;:cllc:;::cll:'.,dO000Oko
00000O0kolxOO0OOO0Od;,:okOO000OOOOOO00OdclxO00O000
X000000OO00O0000OO0OOOO0000000000000O000000000000X
WNXK000O000000000000000000000000000000000000000KNW
MMMWNXKK000000000000000OOO00000000OOOO00000KXNWWMM
MMMMMMWWNNXXXKKK000000000000000000KKKKXXNNWWMMMMMM
MMMMMMMMMMMMMWWWWWNNNNNNNNNNNNNNWWWWMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM""")
            return False
    except ValueError:
        return False

def savetoPokepastes(team):
    #global flag
    paste = (team[0] + team[1] + team[2] +  team[3] + team[4] + team[5]).replace("\n", "\r\n")
    #if flag:
    #    paste += "silent"
    response = requests.post("https://pokepast.es/create", data={"paste" : paste})
    if response.status_code != 200:
        print("Error: post request returned bad status code %d with text %s" % (response.status_code, response.text))
        return ""
    return response.url

def savefile():
    global team 
    bointer = True
    while bointer == True:
        filename = input("Input filename: ")
        try:
            if ".txt" in filename:
                print("Saving to " + filename + "...")
                time.sleep(2)
                f = open(str(filename), "x")
                f.write(team[0] + team[1] + team[2] +  team[3] + team[4] + team[5] + "\n")  #str(magic))
                bointer = False
            else:
                print("Saving to " + filename + ".txt" + "...")
                time.sleep(2)
                f = open(str(filename)+".txt", "x")
                f.write(team[0] + team[1] + team[2] +  team[3] + team[4] + team[5] + "\n") #+ str(magic))
                f.close()
                bointer = False
        except FileExistsError:
            print("File already exists! Give another name: ")


def createTeam(s):
    global team,flag,count
    team = [None] * 6
    abil = [None] * 6
    recr = False
    while team[0] == None or team[1] == None or team[2] == None or team[3] == None or team[4] == None or team[5] == None or recr == True:
        recr = False
        while team[4] == None or team[5] == None:
            a = random.choice(friilist)
            if "Wonder Guard" in a and team[4] == None:
                team[4] = a 
                abil[4] = [x for x in team[4].split("\n") if "Ability:" in x][0]
                while abil[4][-1] == ' ':
                    abil[4] = abil[4][:-1]
            elif "Mold Breaker" in a and team[5] == None:
                team[5] = a
                abil[5] = [x for x in team[5].split("\n") if "Ability:" in x][0]
                while abil[5][-1] == ' ':
                    abil[5] = abil[5][:-1]
        for n in range(4):
            a = random.choice(friilist)
            team[n] = a
            abil[n] = [x for x in team[n].split("\n") if "Ability:" in x][0]  
            while abil[n][-1] == ' ':
                abil[n] = abil[n][:-1]
        for b in range(6):
            stillsomething = abil[b]
            if stillsomething == "Ability: Turboblaze":
                stillsomething = "Ability: Mold Breaker"
            elif stillsomething == "Ability: Teravolt":
                stillsomething = "Ability: Mold Breaker"
            something = abil.count(stillsomething)
            if something >= 3:
                recr = True
    #count += 1
    #print("team created = " + str(count))

    if "-s" in sys.argv or s == "silent":
        pass
        flag = True
    else:
        return team
def dostuff():
    global finished
    amount = ""
    while not(parser(amount)):
        amount = input("How many teams would you like to make?: ")
    else:
        for i in range(int((amount))):
            if int(amount) ==  1:
                createTeam("notsilent")
                save()
            else:
                createTeam("silent")
                print("Created a new team!")
                save()
        finished = 1
    sys.exit()

#runchrome()
#dostuff()
