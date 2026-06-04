# if you don't have the required libraries, comment line 2 out
# %pip install pandas psutil

from dataclasses import dataclass
import psutil
import os

@dataclass
class OSData:
    identifier: str
    name: str
    disk_path: str
DATA = {
    "nt": {
        "name": "Windows",
        "disk_path": "C:\\",
    },
    "posix": {
        "name": "Unix-based or Unix-like",
        "disk_path": "/"
    }
}

DATA = {k: OSData(identifier=k, **v) for k, v in DATA.items()}

class SystemMonitor:
    def __init__(self):
        self.os_data = DATA[os.name]

    def get_cpu_usage(self) -> float:
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self) -> float:
        mem = psutil.virtual_memory()
        return mem.percent

    def get_disk_usage(self) -> float:
        disk = psutil.disk_usage(self.os_data.disk_path)
        return disk.percent

    def __str__(self) -> str:
        return f"""System Monitor for OS: {self.os_data.name}
CPU Usage: {self.get_cpu_usage()}%
Memory Usage: {self.get_memory_usage()}%
Disk Usage: {self.get_disk_usage()}%"""
    
    def __dict__(self) -> dict:
        return {
            "os": self.os_data.name,
            "cpu_usage": self.get_cpu_usage(),
            "memory_usage": self.get_memory_usage(),
            "disk_usage": self.get_disk_usage()
        }


if __name__ == "__main__":
    system_monitor = SystemMonitor()
    print(system_monitor.get_cpu_usage())
    print(system_monitor.get_memory_usage())
    print(system_monitor.get_disk_usage())
    print(system_monitor)
    print(system_monitor.__dict__())