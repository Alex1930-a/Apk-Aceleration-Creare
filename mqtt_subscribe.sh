#!/bin/bash
# Script para escutar o tópico MQTT forwardMessage
# Broker: 24ad79d7b642426092176dec107992d9.s1.eu.hivemq.cloud:8883
# Usuário: 123456789012345
# Senha: Bryan1234
# Tópico: forwardMessage

echo "Conectando ao broker MQTT..."
echo "Broker: 24ad79d7b642426092176dec107992d9.s1.eu.hivemq.cloud:8883"
echo "Tópico: forwardMessage"
echo "=========================================="

# Usando mosquitto_sub (se instalado)
mosquitto_sub \
  -h 24ad79d7b642426092176dec107992d9.s1.eu.hivemq.cloud \
  -p 8883 \
  -u 123456789012345 \
  -P Bryan1234 \
  -t forwardMessage \
  -v \
  --cafile /etc/ssl/certs/ca-certificates.crt

# Se não tiver mosquitto_sub instalado, instale com:
# Ubuntu/Debian: sudo apt-get install mosquitto-clients
# macOS: brew install mosquitto
# Windows: Baixe de https://mosquitto.org/download/
