#**********************************WARNING**********************************
#before execute this code: replace the second line in setup.txt ********************************** do not finish the 4th line with a line break
#this code was made with the only intention to mine a 4 letter sequence address, its virtually impossible to find much larger sequences in adressess try it for 3 or 2 letter/number sequences
import pywaves as pw
from time import time, sleep

setup = open("setup.txt")
name = setup.readline()
passphrase = setup.readline()
steps = int(setup.readline())
target = setup.readline()
print(name)
print(passphrase)
print(steps)
print(target)
setup.close()

writeResult = open("results.txt","a")
writeResult.write(name + "\n")
writeResult.close()

	
	
def seedGenerator(steps=1, number=0, variator=passphrase):
	fullNumber = str(number).zfill(15*steps)
	seed = ""
	for i in range(15):
		position = (i)*steps
		seed += "{0}{1} ".format(fullNumber[position:position + steps],str(variator[i]))
	return seed

def addressChecker(seed, target):
	try:
		address = pw.Address(seed = seed)
		address.address.lower().find(target.lower(), 1) != -1:
		return (address)
	except:
		print("offine while trying to get address from seed {0}".format(seed))
		sleep(10)
		return addressChecker(seed, target)
#testing
#it still needs better input methods
	
i = 0
startTime = time()
lastTime = startTime
while(i<10**(15*steps)):
	result = addressChecker(seedGenerator(steps, i),target)
	if result:
		print("address minned")
		writeResult = open("results.txt","a")
		writeResult.write("{0}\n\n".format(result))
		writeResult.close()
	i+=1
	currentTime = time()
	if (currentTime - lastTime)>1000 :
		print("tryd {0} times, and passed {1} minutes".format(i,(currentTime-startTime)/60))
		lastTime = currentTime
