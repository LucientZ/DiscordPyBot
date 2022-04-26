from datahandling import *
import os

#Test 1: add a token
write_token("awesome")
try:
    myfile = open('token.dat','r')
    token = myfile.read()
    if(token != "awesome"):
        raise Exception("File contents not string 'awesome'")
    myfile.close()
    print("[Test 1] passed")
except Exception as e:
    print("[Test 1] failed\n","[ERROR]:",e)


#Test 2: add a new token to replace the old token
write_token("new_token")
try:
    myfile = open('token.dat','r')
    token = myfile.read()
    if(token != "new_token"):
        raise Exception("File contents not string 'new_token'")
    myfile.close()
    print("[Test 2] passed")
except Exception as e:
    print("[Test 2] failed\n","[ERROR]:",e)

#Test 3: try to get_token from token.dat
write_token("new_token")
TOKEN = get_token()
if(TOKEN == "new_token"):
    print("[Test 3] passed")
else:
    print("[Test 3] failed")
    print("TOKEN =", TOKEN)

#Test 4: call get_token() when token.dat does not exist and create file
os.remove("token.dat") 
print("--------------------------------------------------------------------------------\nPlease type 'Y' on this next section and enter 'new_token' when prompted for a token")
TOKEN = get_token()

if(TOKEN == "new_token"):
    print("[Test 4] passed")
else:
    print("[Test 4] failed")
    print("TOKEN =", TOKEN)

#Test 5: call get_token() when token.dat does not exist and do not create file
os.remove("token.dat") 
print("--------------------------------------------------------------------------------\nPlease type 'n' on this next section and enter 'new_token' when prompted for a token")
TOKEN = get_token()

if(TOKEN == "new_token"):
    print("[Test 5] passed")
else:
    print("[Test 5] failed")
    print("TOKEN =", TOKEN)


#Test 6: call get_token() when token.dat is empty. Write to token.dat
write_token("")
print("--------------------------------------------------------------------------------\nPlease type 'Y' on this next section and enter 'new_token' when prompted for a token")
TOKEN = get_token()

if(TOKEN == "new_token"):
    print("[Test 6] passed")
else:
    print("[Test 6] failed")
    print("TOKEN =", TOKEN)
os.remove("token.dat") 

#Test 7: call get_token() when token.dat is empty. Do not write to token.dat
write_token("")
print("--------------------------------------------------------------------------------\nPlease type 'n' on this next section and enter 'new_token' when prompted for a token")
TOKEN = get_token()

if(TOKEN == "new_token"):
    myfile = open('token.dat','r')
    token = myfile.read()
    if(token != ""):
        print("[Test 7] failed")
        print("TOKEN =", TOKEN)
    else:
        print("[Test 7] passed")
    myfile.close()
else:
    print("[Test 7] failed")
    print("TOKEN =", TOKEN)

os.remove('token.dat')