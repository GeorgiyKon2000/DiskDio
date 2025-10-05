import unittest
import psutil
from diskdio.disk_usage_chart import get_disk_info


class TestDiskUsage(unittest.TestCase):

    def test_get_disk_info_returns_list(self):
        result = get_disk_info()
        self.assertIsInstance(result, list)

    def test_disk_info_contains_keys(self):
        result = get_disk_info()
        if result:  # если находим хотя бы один диск
            disk = result[0]
            for key in ["device", "mountpoint", "total", "used", "free"]:
                self.assertIn(key, disk)

    def test_total_is_greater_than_used(self):
        result = get_disk_info()
        if result:
            for disk in result:
                self.assertGreaterEqual(disk["total"], disk["used"])

if __name__ == '__main__':
    unittest.main()
