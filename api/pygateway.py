#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import time
import serial
import pickle # ecriture et lecture objet

from threading import Timer



class pygateway():

	def __init__(self):
		
		
		self.port='/dev/ttyUSB1'
		self.baudrate = 115200
		
		self.tempo = 10 #secondes entre enregistrement des donnees dans mysensors.bin
		
		self.gat_var={}
		
		self.active_serial()
		Timer(self.tempo,self.timerEvent).start()
		

	
	def active_serial(self):
		self.ser = serial.Serial(
		 port=self.port,
		 baudrate = self.baudrate,
		 parity=serial.PARITY_NONE,
		 stopbits=serial.STOPBITS_ONE,
		 bytesize=serial.EIGHTBITS,
		 timeout=1
		)
		
	def lecture(self):
		while 1:
		 x=self.ser.readline()
		 if x!="": 
			 x=x[:-1]
			 l = x.split(';')
			 self.placement_trame(l)


	def planing_ecriture_donnees(self,donnee):
		
		with open('mysensors.bin', 'wb') as fichier:
			mon_pickler = pickle.Pickler(fichier)
			mon_pickler.dump(donnee)
			
	def timerEvent(self):
		self.planing_ecriture_donnees(self.gat_var)
		Timer(self.tempo,self.timerEvent).start()
		
	def placement_trame(self, donnee):
		
		if not self.gat_var.has_key(donnee[0]): 
			self.gat_var[donnee[0]]={}
		self.gat_var[donnee[0]][donnee[1]]=donnee[5]
		
		print(donnee)
		for cle in self.gat_var[donnee[0]]:
			print(self.gat_var[donnee[0]][cle])
		
		
def main(args):
	
	pygate = pygateway()
	pygate.lecture()
	


if __name__=="__main__":
	
	main(sys.argv)
