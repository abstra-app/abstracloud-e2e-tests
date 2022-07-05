import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestExamples(unittest.TestCase):
    def check_if_exists(self, selector):
        try:
            elem = self.wait.until(
                EC.presence_of_element_located((By.XPATH, selector)))
            return elem
        except:
            return False

    def expect_text(self, content, next=True):
        selector = f'//div[contains(@class,"text") and contains(.,"{content}")]'
        response = self.check_if_exists(selector)
        if response is False:
            self.fail(f'Text {content} not found')

        if next:
            self.next()

    def expect_link(self, content, url, next=True):
        selector = f'//a[contains(@href,"{url}") and contains(.,"{content}")]'
        elem = self.check_if_exists(selector)
        if elem is False:
            self.fail(f'Link {content} not found')
        if next:
            self.next()

    def expect_panda_table(self, columns, next=True):
        for index, column in enumerate(columns):
            selector = f'//table/thead/tr/th[{index+2}]'
            elem = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, selector)))
            self.assertIn(column, elem.text)
        if next:
            self.next()

    def fill_text(self, label, value, next=True, placeholder="Your answer here"):
        selector = f'//div[contains(@class,"label") and contains(.,"{label}")]'
        self.check_if_exists(selector)
        selector = f'//input[contains(@class,"input") and contains(@placeholder,"{placeholder}")]'
        elem = self.check_if_exists(selector)
        elem.send_keys(value)
        if next:
            self.next()

    def fill_textarea(self, label, value, next=True, placeholder="Your answer here"):
        selector = f'//div[contains(@class,"label") and contains(.,"{label}")]'
        self.check_if_exists(selector)
        selector = f'//textarea[contains(@class,"input") and contains(@placeholder,"{placeholder}")]'
        elem = self.check_if_exists(selector)
        elem.send_keys(value)
        if next:
            self.next()

    def fill_phone(self, label, value, next=True, placeholder="(000)000-0000"):
        selector = f'//div[contains(@class,"label") and contains(.,"{label}")]'
        elem = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, selector)))
        self.assertIn(label, elem.text)
        selector = f'//input[contains(@class,"input") and contains(@placeholder,"{placeholder}")]'
        elem = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, selector)))
        elem.send_keys(value)
        if next:
            self.next()

    def fill_date(self, label, value, next=True):
        selector = f'//div[contains(@class,"label") and contains(.,"{label}")]'
        elem = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, selector)))
        self.assertIn(label, elem.text)
        selector = f'//input[contains(@class,"input") and contains(@type,"date")]'
        elem = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, selector)))
        elem.send_keys(value)
        if next:
            self.next()

    def fill_option(self, label, value, next=True):
        elem = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'label')))
        self.assertIn(label, elem.text)
        selector = f'//div[contains(@class,"radiobox") and contains(.,"{value}")]'
        elem = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, selector)))
        elem.click()
        if next:
            self.next()

    def fill_multiple_options(self, label, values, next=True):
        elem = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'label')))
        self.assertIn(label, elem.text)
        for value in values:
            selector = f'//div[contains(@class,"checkbox") and contains(.,"{value}")]'
            elem = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, selector)))
            elem.click()
        if next:
            self.next()

    def fill_dropdown(self, label, value, next=True):
        selector = f'//div[contains(@class,"label") and contains(.,"{label}")]'
        elem = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, selector))
        )
        self.assertIn(label, elem.text)
        selector = f'//li[contains(@class,"vs__dropdown-option") and contains(.,"{value}")]'
        elem = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, selector)))
        elem.click()
        if next:
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
        self.expect_text('Thank you', False)
        self.driver.close()

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
        self.fill_date('What is your date of birth, Abstra', '30/05/2022')
        self.fill_dropdown('In which country do you currently live?', 'Brazil')
        self.fill_dropdown(
            'In which city do you currently live?', 'Rio de Janeiro')
        self.fill_text(
            'Ok! Please add your street address in Brazil.', 'Rua Teste Numero Teste')
        self.fill_text("And what's the number?", 10)
        self.fill_text('Apartment or unit:', 'teste 21231')
        self.fill_text('Zip code:', '123123121231')
        self.fill_phone('What is your primary phone number?', '11999999999')
        self.fill_option(
            'What type of identification can you provide?', "driver's license")
        self.fill_text('What is the identification number?', '123121231')
        self.fill_date(
            'What is the identification expiration date?', '30/05/2022')
        self.expect_text(
            "We're done with personal info! Let's move on to your medical history.")
        self.fill_text('What is your last known weight, in kilograms?', '70')
        self.fill_text('What is your height, in centimeters?', '180')
        self.fill_option("Are you under a physician's care now?", 'yes')
        self.fill_textarea(
            'Please state the main reason you are under medical care at the moment.', 'aaaaaaaaaaaa')
        self.fill_option(
            'Have you ever been hospitalized or had a major injury?', 'yes')
        self.fill_textarea('Please provide details.', 'aaaaaaaaaaaa')
        self.fill_option('Are you taking any medication?', 'yes')
        self.fill_textarea(
            'Please provide reasons, names and dosages of all medication.', 'aaaaaaaaaaaa bbbbbbbb 2mg')
        self.fill_option('Are you on a special diet?', 'yes')
        self.fill_textarea(
            'Please provide details regarding your diet.', 'aaaaaaaaaaaa')
        self.fill_option('Do you smoke?', 'yes')
        self.fill_option('Do you consume alcohol regularly?', 'yes')
        self.fill_option('Are you pregnant or trying to get pregnant?', 'yes')
        self.fill_multiple_options('Please select from the list below any allergies you have.', [
                                   "aspirin", "penicillin", "codein", "local anesthetics", "other"])
        self.fill_text('What other allergies do you have?', 'bbbbbbbb 3mg')
        self.fill_textarea(
            'If you have any specific concerns that brought you to medical care today, please explain them in detail here.', 'bbbbbb cccccccc 4mg')
        self.expect_text(
            "Alright! We're nearly finished. Just one last thing...")
        self.fill_text("Please confirm that you've answered this form with the truth to the best of your knowledge by typing your full name EXACTLY as follows: Abstra Bot", 'Abstra Bot')
        self.expect_text(
            "Thanks, Abstra Bot! You're checked in and ready to go.", False)
        self.driver.close()

    def test_purchase_requester(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 100)

        self.driver.get(
            "https://examples.abstra.run/f036497f-4069-4010-b7a8-2ebed126d872")
        self.wait.until(EC.title_is('Purchase Requester'))
        self.next()

        self.expect_text('Hi! Welcome to our Purchase Requester.')
        self.fill_text('What is the title of this expense?',
                       'Figura de ação do naruto')
        self.fill_text('How much was this expense?', '100')
        self.fill_option('Is this a monthly recurring expense?', 'no')
        self.fill_option(
            'To which department does this expense belong?', 'Engineering')
        self.fill_text('Briefly describe what this expense is for.',
                       'Melhorar a moral da equipe')
        self.fill_option('What type of expense is this?', 'misc')
        self.fill_date('When is this expense due?', '30/05/2022')
        self.expect_text(
            "We've registered this expense succesfully. Thanks! See ya next time.", False)
        self.driver.close()

    def test_invoice_factoring_calculator(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.get(
            "https://examples.abstra.run/56aee472-37a9-49e7-8f4b-9460c84dbc92")
        self.wait.until(EC.title_is('Invoice Factoring Calculator'))
        self.next()

        self.expect_text('Hi! Welcome to our Invoice Factoring Calculator.')
        self.fill_option(
            'Please choose from the list of example assignors:', "McQueen's Auto Shop")
        self.expect_text(
            'Here are the receivables financing terms for this assignor.', False)
        self.expect_panda_table(
            ['Assignor Name', 'Monthly Interest Rate'])
        self.expect_text(
            "Now, let's calculate terms for a new invoice.", False)
        self.fill_text(
            'What is the total value of this invoice?', '500', False)
        self.fill_date('When is this invoice due?', '30/05/2022')
        self.fill_dropdown(
            'Choose a supplier from this list to calculate risk multiplier.', 'Mediocre Thing Doer')
        self.expect_text(
            "OK! Mediocre Thing Doer has a risk multiplier of 2 because they sometimes delay payment on invoices but have never defaulted. The new updated interest rate is 2.0%.")
        self.expect_text(
            'The take rate for this invoice is calculated at 2.0% over -1 months, given the invoice due date, assignor credit score and relevant supplier historical data.', False)
        self.expect_text(
            'The amount payable for this invoice is $510.0.', False)

        self.driver.close()


if __name__ == '__main__':
    unittest.main()
