import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestExamples(unittest.TestCase):
    def expect_text(self, content):
        elem = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'text')))
        self.assertIn(content, elem.text)
        self.next()

    def expect_link(self, content, url):
        elem = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'link')))
        self.assertIn(content, elem.text)
        self.assertIn(url, elem.get_attribute('href'))
        self.next()

    def fill_text(self, label, value):
        elem = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'label')))
        self.assertIn(label, elem.text)
        elem = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'input')))
        elem.send_keys(value)
        self.next()

    def fill_option(self, label, value):
        elem = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'label')))
        self.assertIn(label, elem.text)
        selector = f"//div[contains(@class,'radiobox') and contains(.,'{value}')]"
        elem = self.wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
        elem.click()
        self.next()

    def next(self):
        elem = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'next-button')))
        elem.click()
    
    def test_simple_quiz(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 100)

        self.driver.get("https://examples.abstra.run/8e174c9a-ffe7-44fe-9950-ceafbd7c4bec")
        self.wait.until(EC.title_is('Simple quiz'))
        self.next()

        self.expect_text('Hey, there')
        self.expect_text('So, now')
        self.fill_text('Hang on', 'Abstra bot')
        self.fill_option('Abstra bot', 'ugh')
        self.expect_text('also kinda ugh')
        self.expect_text('Now that we')
        self.fill_text('First up', '1')
        self.fill_text('Cool', '2')
        self.fill_option('Interesting', 'add')
        self.expect_text('1 + 2 = 3')
        self.fill_option('2x + 6y = 22, x + y = 5', '2')
        self.expect_text('Great job')
        self.fill_text('Find the sum', '55')
        self.expect_text('I see you, smarty-pants!')
        self.expect_text('I can feel our day')
        self.expect_text('Give me a spin')
        self.expect_link('Try Abstra Cloud free now', 'abstracloud.com')
        self.expect_text('Thank you')

        self.driver.close()

    def test_self_checkin(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 100)

        self.driver.get("https://examples.abstra.run/b0a39028-1988-42c8-b04b-b230c70c9bb3")
        self.wait.until(EC.title_is('Self check-in'))
        self.next()

        self.fill_text('Welcome to Dr', 'Abstra')
        self.fill_text('What is your last name?', 'Bot')
        self.fill_text('What is your middle initial?', '')
        self.fill_text('Ok. What is your email?', 'abstra@bot.com')

        self.driver.close()


if __name__ == '__main__':
    unittest.main()
