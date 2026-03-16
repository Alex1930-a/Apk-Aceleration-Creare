# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import json
import sys

# Configurar encoding
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

MQTT_BROKER = "24ad79d7b642426092176dec107992d9.s1.eu.hivemq.cloud"
MQTT_PORT = 8883
MQTT_USERNAME = "123456789012345"
MQTT_PASSWORD = "Bryan1234"
MQTT_TOPIC = "forwardMessage"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("[OK] Conectado ao broker MQTT")
        print(f"[INFO] Escutando topico: {MQTT_TOPIC}")
        print("=" * 60)
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"[ERRO] Erro ao conectar: codigo {rc}")
        sys.exit(1)

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode('utf-8')
        print(f"\n[MENSAGEM] Topico: {msg.topic}")
        print(f"[INFO] Tamanho: {len(payload)} bytes")
        print("-" * 60)
        try:
            json_data = json.loads(payload)
            print(json.dumps(json_data, indent=2, ensure_ascii=False))
        except json.JSONDecodeError:
            print(payload)
        print("=" * 60)
    except Exception as e:
        print(f"[ERRO] Erro ao processar: {e}")

print("=" * 60)
print("MQTT Subscriber - Escutando topico forwardMessage")
print("=" * 60)
print(f"Broker: {MQTT_BROKER}:{MQTT_PORT}")
print(f"Usuario: {MQTT_USERNAME}")
print(f"Topico: {MQTT_TOPIC}")
print("=" * 60)

client = mqtt.Client()
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.on_connect = on_connect
client.on_message = on_message

try:
    client.tls_set()
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    print("\nAguardando mensagens... (Ctrl+C para sair)\n")
    client.loop_forever()
except KeyboardInterrupt:
    print("\n[INFO] Interrompido pelo usuario")
    client.disconnect()
except Exception as e:
    print(f"\n[ERRO] Erro: {e}")
    sys.exit(1)
