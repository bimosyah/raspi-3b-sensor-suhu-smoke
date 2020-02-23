from twilio.rest import Client
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import requests 


# api  
API_ENDPOINT = "http://192.168.1.8/puskom/api/data/post"

# TWILIO
account_sid = "AC33c4222305503c7e736fb7a42e6b08be"
auth_token  = "0e278cc19e9b9c89ca3139048119e1c5"
client = Client(account_sid, auth_token)
nomer_tujuan = "+6281233045596"
nomer_pengirim ="+12029294009"


# ambil data dari sensor
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
instance = dht11.DHT11(pin=7) #pakai pin cek di gambar raspi pinout

try:
    while True:
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
                    
            #post suhu ke server
            """
            data = {'suhu':result.temperature,
                    'keterangan':""}
            r = requests.post(url = API_ENDPOINT, data = data)
            """
            
            #kirim sms
            """
            if result.temperature >= 29:
                message = client.messages.create(
                            to= nomer_tujuan,
                            from_= nomer_pengirim,
                            body="Suhu melebihi 29 derajat")
                print("SMS terkirim")
            """
        time.sleep(3)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()

