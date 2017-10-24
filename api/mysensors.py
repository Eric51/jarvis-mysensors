#!/usr/bin/python
#-*- coding:Utf-8 -*-

import sys
import time
import serial
import pickle # ecriture et lecture objet




def lecture_donnees():
	with open('mysensors.bin', 'rb') as fichier:
		mon_depickler = pickle.Unpickler(fichier)
		info = mon_depickler.load()
	
	return info	
	
def sonde(node, sensor, sondes):
	return (sondes[str(node)][str(sensor)])
		
def main():
	global TOSAY
	TOSAY="main"
		
	try:
		#récupération de la variable avec les mesures des sondes
		sondes = lecture_donnees()
	
		#retour de la valeur de la sonde
		valeur = sonde(sys.argv[1],sys.argv[2], sondes)
		TOSAY = sys.argv[3].replace('{1}',valeur)
		
	except:
		TOSAY = "Cette sonde n'hexiste pas!"
		
	print TOSAY

if __name__ == "__main__":
	main()
	
