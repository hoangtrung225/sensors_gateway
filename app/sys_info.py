import psutil
import datetime

class SystemInfo():
    WLAN_IFACE = "wlan0"

    @staticmethod
    def network_info():
        wlan = psutil.net_if_addrs()[SystemInfo.WLAN_IFACE]
        network_info = {
                    'address': wlan[0][1],
                    'netmask': wlan[0][2],
                    'broadcast': wlan[0][3],
                    'mac': wlan[1][1]
                }
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
            if process.username() == 'pi':
                    process_info = {
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
