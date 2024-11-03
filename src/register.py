from zeroconf import ServiceInfo, Zeroconf

from config import API_HOST, SERVICE_IP, SERVICE_NAME, SERVICE_PORT, SERVICE_TYPE

zeroconf = Zeroconf()

info = ServiceInfo(
    type_=SERVICE_TYPE,
    name=f"{SERVICE_NAME}.{SERVICE_TYPE}",
    addresses=[SERVICE_IP],
    port=int(SERVICE_PORT),
    server=API_HOST,
    properties={
        "path": "/api/endpoints",
    },
)


def register_service():
    zeroconf.register_service(info)
    print(f"Service {SERVICE_NAME}.{SERVICE_TYPE} registered")


def unregister_service():
    zeroconf.unregister_service(info)
    print(f"Service {SERVICE_NAME}.{SERVICE_TYPE} unregistered")
    zeroconf.close()
