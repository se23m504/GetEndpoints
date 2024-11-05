import logging

from zeroconf import ServiceInfo, Zeroconf

from config import SERVICE_IP, SERVICE_NAME, SERVICE_PORT, SERVICE_TYPE

zeroconf = Zeroconf()

info = ServiceInfo(
    type_=SERVICE_TYPE,
    name=f"{SERVICE_NAME}.{SERVICE_TYPE}",
    addresses=[SERVICE_IP],
    port=int(SERVICE_PORT),
    server=f"{SERVICE_NAME}.local.",
    properties={"path": "/api/endpoints"},
)


def register_service():
    try:
        zeroconf.register_service(info)
        logging.info(f"Service {SERVICE_NAME}.{SERVICE_TYPE} registered")
        logging.info(
            f"Service is available at http://{SERVICE_NAME}.local:{SERVICE_PORT}"
        )
    except Exception:
        logging.error(f"Failed to register service {SERVICE_NAME}.{SERVICE_TYPE}")
        logging.error(
            f"Please add {SERVICE_NAME}.local to /etc/hosts or to your DNS server"
        )
        pass


def unregister_service():
    try:
        zeroconf.unregister_service(info)
        logging.info(f"Service {SERVICE_NAME}.{SERVICE_TYPE} unregistered")
        zeroconf.close()
    except Exception:
        logging.error(f"Failed to unregister service {SERVICE_NAME}.{SERVICE_TYPE}")
        pass
