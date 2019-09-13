# clone these two scripts onto your raspberry pi

run client.py from console with the first argument being the ngrok url that forwards the Raspberry Pi video feed and the second argument being the ngrok url that forwards the detection output from the Google Colab server 

pi@raspberrypi:~ python3 client.py http://eed3f18c.ngrok.io/ http://60f3fabb.ngrok.io/

