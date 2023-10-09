"""
Problema 2 (2 días)

Existen diferentes bases de datos de acceso público donde se registra la geolocalización de de
direcciones IP, sin embargo, no todas concuerdan en los datos que devuelven.

Se requiere determinar de forma automática la ciudad origen de una dirección IP después de
consultar diferentes plataformas, en caso de que exista discrepancia en la información, indicar como
“probable” la ciudad origen que más veces coincidió en la consulta.
Ejemplo de resultado:
Cuando las consultas coinciden:
Ciudad origen: Tokyo
Cuando las consultas discrepan:
Probable Ciudad Origen: Madrid
Se pueden hacer uso de las siguientes plataformas para consulta (al menos usar 2):
• https://geolocation-db.com/json/{DIRECCION_IP}&position=true
• https://ipinfo.io/{DIRECCION_IP}/json
• http://api.hostip.info/get_json.php?ip={DIRECCION_IP}&position=true
• https://json.geoiplookup.io/{DIRECCION_IP}
• https://freegeoip.app/json/{DIRECCION_IP}
• http://ip-api.com/json/{DIRECCION_IP}
"""

import asyncio
import aiohttp
import random
import ipaddress


# Lista de URLs de las APIs de geolocalización
BASE_URLS = [
    "https://geolocation-db.com/json/{DIRECCION_IP}&position=true",
    "https://ipinfo.io/{DIRECCION_IP}/json",
    "http://api.hostip.info/get_json.php?ip={DIRECCION_IP}&position=true",
    "https://json.geoiplookup.io/{DIRECCION_IP}",
    "https://freegeoip.app/json/{DIRECCION_IP}",
    "http://ip-api.com/json/{DIRECCION_IP}"
]

# Función para validar que la ipv4 es valida
def validate_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

# Función para generar una IP aleatoria
def generate_random_ip() -> str:
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

# Función asíncrona para hacer la solicitud HTTP
async def get_url(session: aiohttp.ClientSession, url: str) -> tuple[dict | None, str | None]:
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            # Usamos contet_type = None por que geolocation-db utiliza mimetype: text/html en lugar de json...
            json_response = await response.json(content_type=None)
            return json_response, None
    except Exception as err:
        #print(f"Error en la solicitud para {url}: {err}")
        return None, str(err)

# Función asíncrona para obtener la geolocalización
async def get_ip_location(ip) -> dict:
    possible_cities = {}

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in BASE_URLS:
            url_replace_str = "{" + "DIRECCION_IP" + "}"
            url = url.replace(url_replace_str, ip)
            task = get_url(session, url)
            tasks.append(task)

        responses = await asyncio.gather(*tasks)

        # Procesamos las respuestas
        for response, error in responses:
            if error:
                continue
            city = response.get('city') if response else None
            # Revizamos que la respuesta no contenga que no se conoce la ciudad
            if city and all(term not in city.lower() for term in {"unknown", "not found", "private address"}):
                if city.lower() in possible_cities:
                    possible_cities[city.lower()] += 1
                else:
                    possible_cities[city.lower()] = 1

    return possible_cities

if __name__ == '__main__':
    choice = input("¿Quieres ingresar una IP manualmente? (s/n): ")
    if choice.lower() == 's':
        ip = input("Introduce la dirección IPv4 para buscar: ")
        if not validate_ipv4(ip):
            print(f"{ip} no es una IPv4 valida, por favor ingresa un ip correcta: eg: 187.145.145.41")
            quit()
        ips = [ip]
    else:
        n = int(input("¿Cuántas IPs aleatorias quieres generar?: "))
        ips = [generate_random_ip() for _ in range(n)]

    for ip in ips:
        print("\n")
        possible_cities = asyncio.run(get_ip_location(ip))
        print(f"IP {ip} - Ciudades posibles: {possible_cities}")

        # Interpretación de los resultados
        # Si no hay ciudades
        if not possible_cities:
            print(f"IP {ip} - No se encontró la ciudad")
        # Si todos coinciden con la misma ciudad
        elif len(possible_cities) == 1:
            possible_city, _ = possible_cities.popitem()
            print(f"IP {ip} - Ciudad de origen: {possible_city.title()}")
        # Si hay varias ciudades posibles
        else:
            max_count = max(possible_cities.values())
            most_probable_cities = [city for city, count in possible_cities.items() if count == max_count]

            # Si hay varias ciudades con las misma probabilidad mostramos esas opciones
            if len(most_probable_cities) > 1:
                print(f"IP {ip} - Ciudades más probables: {', '.join(city.title() for city in most_probable_cities)}")
            # Mostramos la ciudad más probable
            else:
                print(f"IP {ip} - Probable Ciudad de Origen: {most_probable_cities[0].title()}")
