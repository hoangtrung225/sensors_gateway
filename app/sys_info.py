import psutil
import datetime
import socket

class SystemInfo():
    
    def __init__(self):
        self.WLAN_IFACE = self.get_wireless_iface()

    @staticmethod
    def get_wireless_iface():
        ifaces = psutil.net_if_addrs()
        # loop through ifaces and return wireless interface name
        iface_found = None
        for iface in ifaces:
            if iface.startswith("wl"):
                iface_found = iface

        return iface_found

    def network_info(self):
        wlan = psutil.net_if_addrs()[self.WLAN_IFACE]
        network_info = {}
        # network_info = {
        #             'address': wlan[0][1],
        #             'netmask': wlan[0][2],
        #             'broadcast': wlan[0][3],
        #             'mac': wlan[1][1]
        #         }
        for AF in wlan:
            if AF[0] == socket.AF_INET:
                network_info.update({"address": AF[1], "netmask": AF[2], "broadcast": AF[3]})
            elif AF[0] == socket.AF_PACKET:
                network_info.update({"mac": AF[1]})
        return network_info
    
    @staticmethod
    def system_info():
        system_info = {
                    'cpu': psutil.cpu_percent(),
                    'memory': psutil.virtual_memory()[2],
                    'disk': psutil.disk_usage('/')[3],
                    'uptime': datetime.datetime.fromtimestamp(psutil.boot_time())
                }
        return system_info
    
    @staticmethod
    def system_process():
        processes = []
        for process in psutil.process_iter():
            if process.username() != 'root':
                    process_info = {
                        "username": process.username(),
                        "pid": process.pid,
                        "name": process.name(),
                        "status": process.status(),
                        "create_time": process.create_time(),
                        "num_threads": process.num_threads(),
                        "cpu_percent": process.cpu_percent()
                    }
                    processes.append(process_info)
        print(processes)
        return processes
