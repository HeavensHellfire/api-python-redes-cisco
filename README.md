# Scripts del Network Controller

Conjunto de scripts en Python que consumen la API REST del Network Controller de Packet Tracer para consultar y listar la información de la topología.

## Requisitos

- Python 3
- Librerías: `requests` y `tabulate`
- Conectividad IP con el Network Controller

```bash
pip install requests tabulate
```

## Detalle de cada script

### 01_get-ticket.py
Hace una solicitud de service ticket para poder utilizar la API del Network Controller. En caso exitoso, devuelve el código del service ticket.

### 02_get-network-device.py
Retorna la lista de los distintos dispositivos (routers y switches) que integran la topología. Además, indica sus modelos y su dirección IPv4 correspondiente.

### 03_get-host.py
Lista todos los hosts que forman parte de la topología (PCs y servers). Junto a ellos, muestra sus direcciones IPv4 e IPv6, además de la interfaz a la que están conectados.

### 04_tabulate.py
De forma tabulada, devuelve una lista de hosts y dispositivos de la topología:

- **Hosts:** tipo e IPv4 asignada.
- **Dispositivos:** número de serie y versión de software.

### 05_get-siteHealth.py
Comando personal. Lista todos los equipos registrados por el Network Controller. Además del hostname, muestra:

- IP e interfaz correspondiente.
- VLAN a la que pertenece cada equipo.

## Uso

Ejecutar primero `01_get-ticket.py` para verificar que la autenticación funciona, y luego cualquiera de los demás scripts:

```bash
python 01_get-ticket.py
python 02_get-network-device.py
```