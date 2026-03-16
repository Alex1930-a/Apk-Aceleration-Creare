# Como Escutar o Tópico MQTT `forwardMessage`

## Informações do Broker

- **Broker**: `24ad79d7b642426092176dec107992d9.s1.eu.hivemq.cloud`
- **Porta**: `8883` (SSL/TLS)
- **Usuário**: `123456789012345`
- **Senha**: `Bryan1234`
- **Tópico**: `forwardMessage`
- **Protocolo**: MQTT 3.1.1 com TLS/SSL

## Opção 1: Usando mosquitto_sub (Linux/macOS)

### Instalação

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install mosquitto-clients
```

**macOS:**
```bash
brew install mosquitto
```

**Windows:**
Baixe de: https://mosquitto.org/download/

### Comando

```bash
mosquitto_sub \
  -h 24ad79d7b642426092176dec107992d9.s1.eu.hivemq.cloud \
  -p 8883 \
  -u 123456789012345 \
  -P Bryan1234 \
  -t forwardMessage \
  -v \
  --cafile /etc/ssl/certs/ca-certificates.crt
```

**Windows (PowerShell):**
```powershell
mosquitto_sub `
  -h 24ad79d7b642426092176dec107992d9.s1.eu.hivemq.cloud `
  -p 8883 `
  -u 123456789012345 `
  -P Bryan1234 `
  -t forwardMessage `
  -v
```

## Opção 2: Usando Python (paho-mqtt)

### Instalação

```bash
pip install paho-mqtt
```

### Executar script

```bash
python mqtt_subscribe.py
```

Ou use o script Python fornecido (`mqtt_subscribe.py`).

## Opção 3: Usando mqtt-cli (Java)

### Instalação

```bash
# macOS/Linux
brew install mqtt-cli

# Ou baixe de: https://github.com/hivemq/mqtt-cli/releases
```

### Comando

```bash
mqtt sub \
  -h 24ad79d7b642426092176dec107992d9.s1.eu.hivemq.cloud \
  -p 8883 \
  -u 123456789012345 \
  -pw Bryan1234 \
  -t forwardMessage \
  -s
```

## Opção 4: Usando MQTT Explorer (GUI)

1. Baixe: https://mqtt-explorer.com/
2. Configure:
   - Host: `24ad79d7b642426092176dec107992d9.s1.eu.hivemq.cloud`
   - Port: `8883`
   - Username: `123456789012345`
   - Password: `Bryan1234`
   - SSL/TLS: Habilitado
3. Conecte e navegue até o tópico `forwardMessage`

## Formato das Mensagens

As mensagens são JSON com dados de acelerômetro:

```json
{
  "accel_data": [
    {
      "ts": "2026-03-04T13:30:00Z",
      "x": 0.123,
      "y": -0.456,
      "z": 0.789,
      "lat": -23.5505,
      "lon": -46.6333
    }
  ],
  "timestamp": "2026-03-04T13:30:00Z",
  "point_count": 1500,
  "device_name": "M3 Mini",
  "device_address": "AA:BB:CC:DD:EE:FF",
  "full_scale": "±2g",
  "sampling_rate": "10 Hz"
}
```

## Troubleshooting

### Erro de certificado SSL

Se houver erro de certificado, tente:

```bash
mosquitto_sub \
  -h 24ad79d7b642426092176dec107992d9.s1.eu.hivemq.cloud \
  -p 8883 \
  -u 123456789012345 \
  -P Bryan1234 \
  -t forwardMessage \
  -v \
  --insecure  # Ignora verificação de certificado (não recomendado em produção)
```

### Verificar conexão

Teste a conexão primeiro:

```bash
mosquitto_pub \
  -h 24ad79d7b642426092176dec107992d9.s1.eu.hivemq.cloud \
  -p 8883 \
  -u 123456789012345 \
  -P Bryan1234 \
  -t forwardMessage \
  -m "teste" \
  --cafile /etc/ssl/certs/ca-certificates.crt
```
