import psutil
import os

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

class GetProcessor:
    def __init__(self):
        self.processor_percent = psutil.cpu_percent(interval=1)
    def __str__(self):
        return f"{self.processor_percent:.2f}"
    
class GetMemory:
    def __init__(self):
        memory = psutil.virtual_memory()
        self.memory_percent = memory.percent
    def __str__(self):
        return f"{self.memory_percent:.2f}"

class GetDisk:
    def __init__(self):
        kernel = os.name
        disk_path = DATA.get(kernel, "posix")["disk_path"]
        disk = psutil.disk_usage(disk_path)

        disk_used = disk.used / (1024 ** 3)
        disk_total = disk.total / (1024 ** 3)

        self.disk_percent = disk_used / disk_total * 100
    def __str__(self):
        return f"{self.disk_percent:.2f}"
    
if __name__ == "__main__":
    processor = GetProcessor()
    memory = GetMemory()
    disk = GetDisk()

    print(f"CPU: {processor}%\nRAM: {memory}%\nDisk used: {disk}%")