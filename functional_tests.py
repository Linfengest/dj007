from selenium import webdriver
from django.test import LiveServerTestCase
from seleniun.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import unittest
import time

MAX_WAIT = 10

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    #输入重构
    def inputtext(self,write_text):
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(write_text)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

    #检查重构
    def wait_for_row_in_list_table(self,row_text):
        start_time =time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text,[row.text for row in rows])
                return
            except(AssertionError,WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        #听说一个很酷的在线待办事项应用
        #进去看看首页
        self.browser.get(self.live_server_url)

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

        #输入两个待办事项并检查
        self.inputtext("Buy peacock feathers")
        self.inputtext("Use peacock feather to make a fly")
        self.wait_for_row_in_list_table("1: Buy peacock feathers")
        self.wait_for_row_in_list_table("2: Use peacock feather to make a fly")

        self.fail("Finish the test!")
        #在文本框中输入“Buy peacock feathers"
        #inputbox.send_keys('Buy peacock feathers')

        #按下回车，页面更新，
        #inputbox.send_keys(Keys.ENTER)
        #time.sleep(1)

        #页面还有输入框，继续输入
        #输入“Use peacock feather to make a fly"
        #inputbox = self.browser.find_element_by_id('id_new_item')
        #inputbox.send_keys('Use peacock feather to make a fly')
        #inputbox.send_keys(Keys.ENTER)
        #time.sleep(1)

        #表格显示‘Buy peacock feathers Use peacock feather to make a fly’
        #table = self.browser.find_element_by_id('id_list_table')
        #rows = table.find_elements_by_tag_name('tr')
        #self.assertTrue('Buy peacock feathers',[row.text for row in rows])
        #self.assertTrue('Use peacock feather to make a fly',[row.text for row in rows])






















