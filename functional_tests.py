from selenium import webdriver
import unittest



class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")

        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish the test!")

if __name__=='__main__':
     unittest.main(warnings='ignore')
#很酷的再现办事项应用
#我要去看以下这个网站
#browser.get("http://localhost:8000")

#我注意到网页标题和头部都含有“To-Do”这个词
#assert 'To-Do' in browser.title

#应用邀请我输入一个待办事项

#我在文本框输入“buy peacock feathers"
#我的爱好是用蚊子作鱼饵钓鱼
#browser = webdriver.Firefox()
#browser.quit()
