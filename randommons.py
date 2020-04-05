from lists import friilist
import random
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
mon1 = None
mon2 = mon1
mon3 = mon1
mon4 = mon1
mon5 = mon1
mon6 = mon1
team = mon1
pasteplace = mon1
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
                    ph = input("Are you done? ")
                    if ph.lower() == "true" or ph.lower() == "t" or ph.lower() == "y" or ph.lower() == "yes":
                        done = True
                elif thisorthat.lower() == "txt" or thisorthat.lower() == "t" or thisorthat.lower() == "text":
                    savefile()
                    ph = input("Are you done? ")
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
def runchrome():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--log-level=3')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    try:
        driver = webdriver.Chrome(options = options)
    except:
        print("Chrome driver not found, please put it into your system PATH variable or into the same directory as the executable")
        print("Aborting....")
        time.sleep(1)
        sys.exit()

def newline():
    global pasteplace
    pasteplace.send_keys(Keys.ENTER)
    pasteplace.send_keys("\n")

def savetoPokepastes():
    global driver,pasteplace,finished
    driver.implicitly_wait(0)
    driver.get("https://pokepast.es")
    pasteplace = driver.find_element_by_name("paste")
    pasteplace.send_keys(Keys.TAB)
    pasteplace.clear()
    pasteplace.send_keys(mon1)
    newline()
    pasteplace.send_keys(mon2)
    newline()
    pasteplace.send_keys(mon3)
    newline()
    pasteplace.send_keys(mon4)
    newline()
    pasteplace.send_keys(mon5)
    newline()
    pasteplace.send_keys(mon6)
    try:
        if flag == True:
            pasteplace.send_keys("silent")
    except: 
        pass
    savebutton = driver.find_element_by_xpath("//input[ @type='Submit' and @value='Submit Paste!']")
    savebutton.click()
    print("Your team has been saved at: " + driver.current_url)
    if finished == 1:
        driver.quit()

def savefile():
    
    bointer = True
    while bointer == True:
        filename = input("Input filename: ")
        try:
            if ".txt" in filename:
                print("Saving to " + filename + "...")
                time.sleep(2)
                f = open(str(filename), "x")
                f.write(team)
                bointer = False
            else:
                print("Saving to " + filename + ".txt" + "...")
                time.sleep(2)
                f = open(str(filename)+".txt", "x")
                f.write(team)
                f.close()
                bointer = False
        except FileExistsError:
            print("File already exists! Give another name: ")


def createTeam(s):
    global mon1,mon2,mon3,mon4,mon5,mon6,team,flag,uwu
    n = 1
    mon1 = None
    mon2 = mon1
    mon3 = mon1
    mon4 = mon1
    mon5 = mon1
    mon6 = mon1
    while mon1 == None or mon2 == None or mon3 == None or mon4 == None or mon5 == None or mon6 == None:
        wg = "Wonder Guard"
        mold = "Mold Breaker"
        a = random.choice(friilist)
        if wg in a and mon5 == None:
            mon5 = a
        elif mold in a and mon6 == None:
            mon6 = a
        elif n == 1:
            mon1 = a
            n = 2 
        elif n == 2:
            mon2 = a
            n = 3
        elif n == 3:
            mon3 = a
            n = 4
        elif n == 4:
            mon4 = a
            n = 5
        else:
            pass
    team =(mon1 + "\n" + mon2 + "\n" + mon3 + "\n" + mon4 + "\n" + mon5 + "\n" + mon6 + "\n")    
    if "-s" in sys.argv or s == "silent":
        pass
        flag = True
    else:
        print(team)
def main():
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

runchrome()
main()
