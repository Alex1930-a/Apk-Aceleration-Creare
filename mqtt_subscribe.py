#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para escutar o tópico MQTT forwardMessage
Broker: 24ad79d7b642426092176dec107992d9.s1.eu.hivemq.cloud:8883
Usuário: 123456789012345
Senha: Bryan1234
Tópico: forwardMessage

Instalação: pip install paho-mqtt
"""

import paho.mqtt.client as mqtt
import json
import gzip
import sys
import os

# Configurar encoding UTF-8 para Windows
if sys.platform == 'win32':
    os.system('chcp 65001 >nul 2>&1')
    sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None

# Configurações MQTT
MQTT_BROKER = "24ad79d7b642426092176dec107992d9.s1.eu.hivemq.cloud"
MQTT_PORT = 8883
MQTT_USERNAME = "123456789012345"
MQTT_PASSWORD = "Bryan1234"
MQTT_TOPIC = "forwardMessage"

def on_connect(client, userdata, flags, rc):
    """Callback quando conecta ao broker"""
    if rc == 0:
        print("[OK] Conectado ao broker MQTT")
        print(f"[INFO] Escutando topico: {MQTT_TOPIC}")
        print("=" * 60)
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"[ERRO] Erro ao conectar: codigo {rc}")
        sys.exit(1)

def expand_compact(data):
    """Expande formato compacto v2 para exibição legível"""
    if data.get("v") != 2 or "data" not in data:
        return data
    
    fields = data.get("fields", ["dt", "x", "y", "z"])
    ts_base = data.get("ts_base", "")
    lat = data.get("lat")
    lon = data.get("lon")
    rows = data["data"]
    
    print(f"  Formato: v2 compacto ({len(rows)} pontos)")
    print(f"  Dispositivo: {data.get('device_name', '?')} [{data.get('device_address', '?')}]")
    print(f"  Full Scale: {data.get('full_scale', '?')} | Sampling: {data.get('sampling_rate', '?')}")
    print(f"  Timestamp base: {ts_base}")
    if lat is not None and lon is not None:
        print(f"  GPS: lat={lat}, lon={lon}")
    print(f"  Primeiros 5 pontos (de {len(rows)}):")
    for row in rows[:5]:
        vals = dict(zip(fields, row))
        print(f"    dt={vals.get('dt',0):>6}ms  x={vals.get('x',0):>8.4f}  y={vals.get('y',0):>8.4f}  z={vals.get('z',0):>8.4f}")
    if len(rows) > 5:
        print(f"    ... mais {len(rows) - 5} pontos")
    return None

def on_message(client, userdata, msg):
    """Callback quando recebe mensagem (suporta GZIP e JSON)"""
    try:
        raw = msg.payload
        raw_size = len(raw)
        
        # Detectar GZIP (magic bytes 1f 8b)
        is_gzip = len(raw) >= 2 and raw[0] == 0x1f and raw[1] == 0x8b
        
        if is_gzip:
            decompressed = gzip.decompress(raw)
            payload = decompressed.decode('utf-8')
            json_size = len(decompressed)
            print(f"\n[MENSAGEM] Topico: {msg.topic}")
            print(f"[GZIP] {raw_size} bytes -> {json_size} bytes ({100 - (raw_size * 100 // json_size)}% compressao)")
        else:
            payload = raw.decode('utf-8')
            print(f"\n[MENSAGEM] Topico: {msg.topic}")
            print(f"[INFO] Tamanho: {raw_size} bytes (sem compressao)")
        
        print("-" * 60)
        
        try:
            json_data = json.loads(payload)
            result = expand_compact(json_data)
            if result is not None:
                print(json.dumps(json_data, indent=2, ensure_ascii=False))
        except json.JSONDecodeError:
            print(payload)
        
        print("=" * 60)
    except Exception as e:
        print(f"[ERRO] Erro ao processar mensagem: {e}")
        print(f"Payload (raw): {msg.payload}")

def on_disconnect(client, userdata, rc):
    """Callback quando desconecta"""
    print("\n[INFO] Desconectado do broker MQTT")

def main():
    print("=" * 60)
    print("MQTT Subscriber - Escutando tópico forwardMessage")
    print("=" * 60)
    print(f"Broker: {MQTT_BROKER}:{MQTT_PORT}")
    print(f"Usuário: {MQTT_USERNAME}")
    print(f"Tópico: {MQTT_TOPIC}")
    print("=" * 60)
    
    # Criar cliente MQTT (usando API padrão)
    client = mqtt.Client()
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    
    # Configurar callbacks
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    
    # Conectar com TLS
    try:
        client.tls_set()  # Usa certificados padrão do sistema
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        
        # Loop infinito para escutar mensagens
        print("\nAguardando mensagens... (Ctrl+C para sair)\n")
        client.loop_forever()
    except KeyboardInterrupt:
        print("\n\n[INFO] Interrompido pelo usuario")
        client.disconnect()
    except Exception as e:
        print(f"\n[ERRO] Erro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
