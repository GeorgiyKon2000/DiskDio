import psutil 
import matplotlib.pyplot as plt

def get_disk_info():
    disks = []
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            disks.append({
                "device": part.device,
                "mountpoint": part.mountpoint,
                "total": usage.total,
                "used": usage.used,
                "free": usage.free
            })
        except PermissionError:
            # Некоторые системные разделы могут быть недоступны
            continue
    return disks

def plot_disk_usage(disks):
    """Рисует круговую диаграмму для каждого диска"""
    for disk in disks:
        labels = ['Занято', 'Свободно']
        sizes = [disk['used'], disk['free']]
        plt.figure(figsize=(4, 4))
        plt.pie(
            sizes, labels=labels, autopct='%1.1f%%', startangle=90,
            colors=['#ff6666', '#66b3ff']
        )
        plt.title(f"Диск {disk['device']} ({disk['mountpoint']})")
        plt.axis('equal')
        plt.show()


def main():
    print("📊 Disk usage information:")
    disks = get_disk_info()
    for disk in disks:
        print(f"{disk['device']} — {disk['total'] / (1024**3):.2f} GB total, "
              f"{disk['used'] / (1024**3):.2f} GB used, "
              f"{disk['free'] / (1024**3):.2f} GB free.")
    plot_disk_usage(disks)

if __name__ == "__main__":
    main()