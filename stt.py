import requests
from requests.exceptions import Timeout
import sys
import socket
import argparse
import os

portList = [80, 443]

def Sis():
	if sys.platform == "linux2":
		os.system("cls")
	else:
		os.system("clear")

def Logo():
	print('''
███████╗████████╗████████╗
██╔════╝╚══██╔══╝╚══██╔══╝
███████╗   ██║      ██║   
╚════██║   ██║      ██║   
███████║   ██║      ██║   
╚══════╝   ╚═╝      ╚═╝   v1.0
by: DhelthaX  
		''')

def Argumentos():
	global args
	print ("\n[+] SubDomain Takeover Tester\n")
	print ("[+] Digite stt.py -h para checar o manual\n")
	parser = argparse.ArgumentParser()
	parser.add_argument("-l", dest="subList", action="store", help="Use -l para definir a lista de subdominios a ser verificada")
	args = parser.parse_args()

def subScan():
	with open(subList, 'r') as fo:
		for line in fo:
			line = line.rstrip("\n")
			openPorts = portScan(line, portList)
			sub = "http://"+line
			try:
				r = requests.get(sub, timeout = 2)
			except requests.exceptions.ConnectionError:
				pass	
			if r.status_code == 404:
				print("Possible Subdomain Takeover in: {} - {}".format(line, r.status_code))
			else:
				print("The response of the subdomain {} is {}".format(line, r.status_code))
				pass

def portScan(host, porta):
	for ports in porta:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(2)
		c = s.connect_ex((str(host),int(ports)))
		if c == 0:
			
			print ("\nPort ",ports," Open:")
		else:
				print ("\nPort ",ports," Closed:")
	else:
		quit()

def main():
	Sis()
	Logo()
	Argumentos()
	subScan()

if __name__ == '__main__':
	main()