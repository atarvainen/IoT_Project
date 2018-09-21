#Tuodaan GPIO ja time kirjastot
import RPi.GPIO as GPIO
import time
import signal

#Asetaan nimikaytanteet PIlle
GPIO.setmode(GPIO.BCM)
#Asetetaan GPIO varoitusten tulostus pois paalta
GPIO.setwarnings(False)

#Tehdaan ikuinen silmukka, silmukan saa keskeytettya Ctrl 
#ja C-nappainen yhtaaikaisella painamisella 
while 1: 
	try:
		#Asetetaan pinni 18 ulostuloksia
		GPIO.setup(18,GPIO.OUT)
		print("Led ON")
		#Laitetaan pinniin 18 jannite 
		GPIO.output(18,GPIO.HIGH)
		#Pysaytetaan ohjelma 1 sekunniksi

		#Asetetaan pinni 25  ulostuloksia
		GPIO.setup(17,GPIO.OUT)
		print("Led ON")
                #Laitetaan pinniin 25 jannite
		GPIO.output(17,GPIO.HIGH)
                #Pysaytetaan ohjelma 1 sekunniksi


#suunta vasen-oikea
#sleep to 5
		time.sleep(5)
		print("Led OFF")
		#Laitetaan jannite POIS pinnista 18
		GPIO.output(18,GPIO.LOW)

		#Laitetaan jannite POIS pinnista 25
		GPIO.output(17,GPIO.LOW)
		
		#Pysaytetaan ohjelma 1 sekunniksi

#sleep to 0
		time.sleep(0)

                #Asetetaan pinni 23 ulostuloksia
		GPIO.setup(23,GPIO.OUT)
		print("Led ON")
		#Laitetaan pinniin 23 jannite 
		GPIO.output(23,GPIO.HIGH)
		#Pysaytetaan ohjelma 1 sekunniksi

		#Asetetaan pinni 27 ulostuloksia
		GPIO.setup(27,GPIO.OUT)
		print("Led ON")
                #Laitetaan pinniin 27 jannite
		GPIO.output(27,GPIO.HIGH)
                #Pysaytetaan ohjelma 1 sekunniksi
		time.sleep(2)



#suunto ylos-alas
#sleep to 5
		#Laitetaan jannite POIS pinnista 23
		GPIO.output(23,GPIO.LOW)
		#Pysaytetaan ohjelma 1 sekunniksi


		#Laitetaan jannite POIS pinnista 27
		GPIO.output(27,GPIO.LOW)
                #Pysaytetaan ohjelma 1 sekunniksi

#punaiset
 #Asetetaan pinni 24 ulostuloksia
		GPIO.setup(24,GPIO.OUT)
		print("Led ON")
               	#Laitetaan pinniin 24 jannite
		GPIO.output(24,GPIO.HIGH)
                #Pysaytetaan ohjelma 1 sekunniksi

                #Asetetaan pinni 22  ulostuloksia
		GPIO.setup(22,GPIO.OUT)
		print("Led ON")
                #Laitetaan pinniin 22 jannite
		GPIO.output(22,GPIO.HIGH)
                #Pysaytetaan ohjelma 1 sekunniksi


#suunta vasen-oikea
#sleep to 5
		time.sleep(5)
		print("Led OFF")
                #Laitetaan jannite POIS pinnista 24
		GPIO.output(24,GPIO.LOW)

                #Laitetaan jannite POIS pinnista 22
		GPIO.output(22,GPIO.LOW)



#sleep to 0
		time.sleep(0)


                #Asetetaan pinni 23 ulostuloksia
		GPIO.setup(23,GPIO.OUT)
		print("Led ON")
                #Laitetaan pinniin 23 jannite
		GPIO.output(23,GPIO.HIGH)
                #Pysaytetaan ohjelma 1 sekunniksi

                #Asetetaan pinni 27 ulostuloksia
		GPIO.setup(27,GPIO.OUT)
		print("Led ON")
                #Laitetaan pinniin 27 jannite
		GPIO.output(27,GPIO.HIGH)
                #Pysaytetaan ohjelma 1 sekunniksi
		time.sleep(2)



#suunto ylos-alas
#sleep to 5
                #Laitetaan jannite POIS pinnista 23
		GPIO.output(23,GPIO.LOW)
                #Pysaytetaan ohjelma 1 sekunniksi


                #Laitetaan jannite POIS pinnista 27
		GPIO.output(27,GPIO.LOW)
                #Pysaytetaan ohjelma 1 sekunniksi

		

	#Otetaan Ctrl+C nappaiten painnus kiinni ja keskeytetaan suoritus
	except KeyboardInterrupt:
		#GPIO pinnien pudistaminen
		GPIO.cleanup()
		break
