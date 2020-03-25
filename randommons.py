from lists import friilist
import random
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#22 offset
mon1 = None
mon2 = mon1
mon3 = mon1
mon4 = mon1
mon5 = mon1
mon6 = mon1
team = mon1
def savetoPokepastes():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--log-level=3')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    try:
        driver = webdriver.Chrome(options = options)
    except:
        print("Chromium driver not found, please place the executable in the same directory as this or in your path")
        print("Aborting...")
        sys.exit()
    driver.implicitly_wait(1)
    driver.get("https://pokepast.es")
    pasteplace = driver.find_element_by_name("paste")
    pasteplace.send_keys(Keys.TAB)
    pasteplace.clear()
    pasteplace.send_keys(team)
    savebutton = driver.find_element_by_xpath("//input[ @type='Submit' and @value='Submit Paste!']")
    savebutton.click()
    print("your team is saved at " + driver.current_url)
    driver.quit()

def savefile():
    while True:
        filename = input("filename? ")
        try:
            if ".txt" in filename:
                print("saving to " + filename)
                time.sleep(2)
                f = open(str(filename), "x")
                f.write(team)
                sys.exit()
            else:
                print("saving to " + filename + ".txt")
                time.sleep(2)
                f = open(str(filename)+".txt", "x")
                f.write(team)
                f.close()
                sys.exit()
        except FileExistsError:
            print("file already exists,give another name")
        finally:
            sys.exit()


def createTeam():
    global mon1,mon2,mon3,mon4,mon5,mon6,team
    n = 1
    while mon1 == None or mon2 == None or mon3 == None or mon4 == None or mon5 == None or mon6 == None:
        wg = "Wonder Guard"
        mold = "Mold Breaker"
        a = random.choice(friilist)
        if wg in a and mon5 == None:
            mon5 = a
            h = mon5.split('\n')
            h = h[0:2] + ["EVs: 84 HP / 84 Atk / 84 Def / 84 SpA / 84 SpD / 84 Spe "]+ h[2:8]
            b = '\n'
            b = b.join(h)
            mon5 = b
        elif mold in a and mon6 == None:
            mon6 = a
            h = mon6.split('\n')
            h = h[0:2] + ["EVs: 84 HP / 84 Atk / 84 Def / 84 SpA / 84 SpD / 84 Spe "]+ h[2:8]
            b = '\n'
            b = b.join(h)
            mon6 = b 
        elif n == 1:
            mon1 = a
            n = 2
            h = mon1.split('\n')
            h = h[0:2] + ["EVs: 84 HP / 84 Atk / 84 Def / 84 SpA / 84 SpD / 84 Spe "]+ h[2:8]
            b = '\n'
            b = b.join(h)
            mon1 = b
        elif n == 2:
            mon2 = a
            n = 3
            h = mon2.split('\n')
            h = h[0:2] + ["EVs: 84 HP / 84 Atk / 84 Def / 84 SpA / 84 SpD / 84 Spe "]+ h[2:8]
            b = '\n'
            b = b.join(h)
            mon2 =  b
        elif n == 3:
            mon3 = a
            n = 4
            h = mon3.split('\n')
            h = h[0:2] + ["EVs: 84 HP / 84 Atk / 84 Def / 84 SpA / 84 SpD / 84 Spe "]+ h[2:8]
            b = '\n'
            b = b.join(h)
            mon3 = b
        elif n == 4:
            mon4 = a
            n = 5
            h = mon4.split('\n')
            h = h[0:2] + ["EVs: 84 HP / 84 Atk / 84 Def / 84 SpA / 84 SpD / 84 Spe "]+ h[2:8]
            b = '\n'
            b = b.join(h)
            mon4 = b
        else:
            pass
    team =(mon1 + "\n" + mon2 + "\n" + mon3 + "\n" + mon4 + "\n" + mon5 + "\n" + mon6 + "\n")    
    print(team)
createTeam()
save = input("save? (Y/N) ")
if save == "n" or save == "N":
    sys.exit()
elif save == "Y" or save == "y":
   thisorthat = input("pokepaste or txt? ")
   if thisorthat.lower() == "pokepaste" or thisorthat.lower() == "pokepastes" or thisorthat.lower() == "pokepast.es" or thisorthat.lower() == "p":
    print("\nworking sorry for the wait")
    savetoPokepastes()
   elif thisorthat.lower() == "txt" or thisorthat.lower() == "t" or thisorthat.lower() == "text":
    savefile()
else:
    print("should've chosen Y or N")
    time.sleep(1)
    sys.exit()

