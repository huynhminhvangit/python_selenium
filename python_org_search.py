import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # Khởi tạo trình duyệt Chrome
        self.driver  = webdriver.Remote(
            command_executor='http://192.168.88.182:4444/wd/hub',
            options=webdriver.ChromeOptions()
        )

    def test_search_in_python_org(self):
        # Truy cập trang web python.org
        driver = self.driver
        driver.get("https://www.python.org")
        # Kiểm tra xem tiêu đề có chứa từ khóa "Python" hay không
        self.assertIn("Python", driver.title)
        # Tìm phần tử input có tên là "q"
        elem = driver.find_element(By.NAME, "q")
        # Gõ "hello" vào ô input
        elem.send_keys("hello")
        # Nhấn phím Enter
        elem.send_keys(Keys.RETURN)
        # Kiểm tra xem có kết quả nào không
        assert "No results found." not in driver.page_source

    def tearDown(self):
        # Đóng trình duyệt sau khi hoàn thành kiểm tra
        self.driver.close()

if __name__ == "__main__":
    # Chạy các testcase khi chạy file python này
    unittest.main()
