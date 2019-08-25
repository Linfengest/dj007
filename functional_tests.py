from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #听说一个很酷的在线待办事项应用
        #进去看看首页
        self.browser.get("http://localhost:8000")

        #注意到首页标题和头部都有 'To-Do'
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        #应用邀请输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                        inputbox.get_attribute('placeholder'),
                        'Enter a to-do item'
                        )

        #在文本框中输入“Buy peacock feathers"
        inputbox.send_keys('Buy peacock feathers')

        #按下回车，页面更新，
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        #表格显示‘1：Buy peacock feathers’
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
                        any(row.text == '1：Buy peacock feathers' for row in rows),
                        "New to-do item did not appear in table"
                        )

        self.fail("Finish the test!")

if __name__=='__main__':
     unittest.main(warnings='ignore')





















