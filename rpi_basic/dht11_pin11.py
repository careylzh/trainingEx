#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
import Adafruit_DHT
#for this setup, no need naming convention nor setup pin as input or output,
#the method below automatically sets up 
while True:
    humidity, temperature=Adafruit_DHT.read_retry(11, 4)
    print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
    
#first number ‘11’ means model dht11 is used instead of the other models of dht like dht22, second number means bcm 4, equals to pin 7 in board, equals to what you showed wiring demo 2 slides before