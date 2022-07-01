import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestExamples(unittest.TestCase):
    def expect_text(self, content):
        elem = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'text')))
        self.assertIn(content, elem.text)
        self.next()

    def expect_closing_text(self, content):
        elem = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'text')))
        self.assertIn(content, elem.text)
        self.driver.close()

    def expect_link(self, content, url):
        elem = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'link')))
        self.assertIn(content, elem.text)
        self.assertIn(url, elem.get_attribute('href'))
        self.next()

    def fill_text(self, label, value):
        elem = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'label')))
        self.assertIn(label, elem.text)
        elem = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'input')))
        elem.send_keys(value)
        self.next()

    def fill_option(self, label, value):
        elem = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'label')))
        self.assertIn(label, elem.text)
        selector = f'//div[contains(@class,"radiobox") and contains(.,"{value}")]'
        elem = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, selector)))
        elem.click()
        self.next()

    def fill_multiple_options(self, label, values):
        elem = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'label')))
        self.assertIn(label, elem.text)
        for value in values:
            selector = f'//div[contains(@class,"checkbox") and contains(.,"{value}")]'
            elem = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, selector)))
            elem.click()
        self.next()

    def fill_dropdown(self, label, value):
        elem = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'label'))
        )
        self.assertIn(label, elem.text)
        selector = f'//li[contains(@class,"vs__dropdown-option") and contains(.,"{value}")]'
        elem = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, selector)))
        elem.click()
        self.next()

    def next(self):
        elem = self.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'next-button')))
        elem.click()

    def test_simple_quiz(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 100)

        self.driver.get(
            "https://examples.abstra.run/8e174c9a-ffe7-44fe-9950-ceafbd7c4bec")
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
        self.expect_closing_text('Thank you')

    def test_self_checkin(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 100)

        self.driver.get(
            "https://examples.abstra.run/b0a39028-1988-42c8-b04b-b230c70c9bb3")
        self.wait.until(EC.title_is('Self check-in'))
        self.next()

        self.fill_text('Welcome to Dr', 'Abstra')
        self.fill_text('What is your last name?', 'Bot')
        self.fill_text('What is your middle initial?', '')
        self.fill_text('Ok. What is your email?', 'abstra@bot.com')
        self.fill_text('What is your date of birth, Abstra', '30/05/2022')
        self.fill_dropdown('In which country do you currently live?', 'Brazil')
        self.fill_dropdown(
            'In which city do you currently live?', 'Rio de Janeiro')
        self.fill_text(
            'Ok! Please add your street address in Brazil.', 'Rua Teste Numero Teste')
        self.fill_text("And what's the number?", 10)
        self.fill_text('Apartment or unit:', 'teste 21231')
        self.fill_text('Zip code:', '123123121231')
        self.fill_text('What is your primary phone number?', '11999999999')
        self.fill_option(
            'What type of identification can you provide?', "driver's license")
        self.fill_text('What is the identification number?', '123121231')
        self.fill_text(
            'What is the identification expiration date?', '30/05/2022')
        self.expect_text(
            "We're done with personal info! Let's move on to your medical history.")
        self.fill_text('What is your last known weight, in kilograms?', '70')
        self.fill_text('What is your height, in centimeters?', '180')
        self.fill_option("Are you under a physician's care now?", 'yes')
        self.fill_text(
            'Please state the main reason you are under medical care at the moment.', 'aaaaaaaaaaaa')
        self.fill_option(
            'Have you ever been hospitalized or had a major injury?', 'yes')
        self.fill_text('Please provide details.', 'aaaaaaaaaaaa')
        self.fill_option('Are you taking any medication?', 'yes')
        self.fill_text(
            'Please provide reasons, names and dosages of all medication.', 'aaaaaaaaaaaa bbbbbbbb 2mg')
        self.fill_option('Are you on a special diet?', 'yes')
        self.fill_text(
            'Please provide details regarding your diet.', 'aaaaaaaaaaaa')
        self.fill_option('Do you smoke?', 'yes')
        self.fill_option('Do you consume alcohol regularly?', 'yes')
        self.fill_option('Are you pregnant or trying to get pregnant?', 'yes')
        self.fill_multiple_options('Please select from the list below any allergies you have.', [
                                   "aspirin", "penicillin", "codein", "local anesthetics", "other"])
        self.fill_text('What other allergies do you have?', 'bbbbbbbb 3mg')
        self.fill_text(
            'If you have any specific concerns that brought you to medical care today, please explain them in detail here.', 'bbbbbb cccccccc 4mg')
        self.expect_text(
            "Alright! We're nearly finished. Just one last thing...")
        self.fill_text("Please confirm that you've answered this form with the truth to the best of your knowledge by typing your full name EXACTLY as follows: Abstra Bot", 'Abstra Bot')
        self.expect_closing_text(
            "Thanks, Abstra Bot! You're checked in and ready to go.")


if __name__ == '__main__':
    unittest.main()
