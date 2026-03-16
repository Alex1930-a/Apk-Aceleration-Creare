# Script PowerShell para escutar o tópico MQTT forwardMessage no Windows
# Broker: 24ad79d7b642426092176dec107992d9.s1.eu.hivemq.cloud:8883
# Usuário: 123456789012345
# Senha: Bryan1234
# Tópico: forwardMessage

Write-Host "Conectando ao broker MQTT..." -ForegroundColor Green
Write-Host "Broker: 24ad79d7b642426092176dec107992d9.s1.eu.hivemq.cloud:8883" -ForegroundColor Cyan
Write-Host "Tópico: forwardMessage" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Yellow

# Usando mosquitto_sub (precisa estar instalado)
# Baixe de: https://mosquitto.org/download/
# Adicione ao PATH após instalação

mosquitto_sub `
  -h 24ad79d7b642426092176dec107992d9.s1.eu.hivemq.cloud `
  -p 8883 `
  -u 123456789012345 `
  -P Bryan1234 `
  -t forwardMessage `
  -v

# Alternativa usando Python (se tiver paho-mqtt instalado):
# python -m pip install paho-mqtt
# python mqtt_subscribe.py
