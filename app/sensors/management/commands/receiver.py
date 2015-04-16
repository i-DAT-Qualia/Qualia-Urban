from django.core.management.base import BaseCommand, CommandError
from sensors.api.collectors import *
import json

import paho.mqtt.client as mqtt

from django.conf import settings

import zmq


def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    if msg.topic == "urban/collector/reading/":
        process_reading(json.loads(msg.payload))


class Command(BaseCommand):
    args = ''
    help = 'Saves data from MQTT'

    def handle(self, *args, **options):

        context = zmq.Context()
        sock = context.socket(zmq.REP)
        sock.bind("tcp://*:5678")

        mqttc = mqtt.Client()
        mqttc.on_message = on_message
        mqttc.connect(settings.MQTT_ADDRESS, settings.MQTT_PORT, 60)
        mqttc.subscribe("urban/#", 0)
        mqttc.loop_forever()

        while True:
            message = socket.recv()
            print("received: " + str(message))
