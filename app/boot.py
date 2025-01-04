# highly recommended to set a lowish garbage collection threshold
# to minimise memory fragmentation as we sometimes want to
# allocate relatively large blocks of ram.
import gc
from configs.sys_config import *
from wifi_ap.wifi_portal import connect_to_wifi_ap, setup_wifi_mode, set_rtc
import mp_git
from web_app.web_app import application_mode
from phew import server

"""Main function. Runs after board boot, before main.py
Connects to Wi-Fi and checks for latest OTA version.
"""
#gc.set_threshold(50000)
gc.collect()
gc.enable()

ip_addres = None
if AUTO_CONNECT_TO_WIFI_AP:
    ip_addres = connect_to_wifi_ap()
if ip_addres is None:
    if AUTO_START_SETUP_WIFI:
        setup_wifi_mode()
        server.run()
else:
    set_rtc()
    mp_git.main()
    if AUTO_START_WEBREPL:
        import webrepl
        webrepl.start()
    if AUTO_START_WEBAPP:
        application_mode()
        server.run()

