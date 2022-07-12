import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EXAMPLE_DOMAIN = "https://examples.abstra.run"
ABSTRA_SELENIUM_URL = os.getenv(
    "ABSTRA_SELENIUM_URL", 'https://selenium.abstra.cloud/wd/hub')


class TestExamples(unittest.TestCase):

    def setUp(self) -> None:
        if ABSTRA_SELENIUM_URL:
            options = webdriver.ChromeOptions()
            options.add_argument("--no-sandbox")
            self.driver = webdriver.Remote(
                command_executor=ABSTRA_SELENIUM_URL, options=options)
        else:
            self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 50)

    def tearDown(self) -> None:
        self.driver.quit()

    def check_if_exists(self, selector):
        try:
            elem = self.wait.until(
                EC.presence_of_element_located((By.XPATH, selector)))
            return elem
        except:
            return False
        finally:
            self.driver.save_screenshot('screen.png')

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

    def expect_file(self, content, downloadUrl, next=True):
        selector = f'//a[contains(@href, "{downloadUrl}") and contains(.,"{content}")]'
        elem = self.check_if_exists(selector)
        if elem is False:
            self.fail(f'File {content} not found')
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

    def fill_text(self, label, value, next=True, placeholder="Your answer here", type="text-input", index="0"):
        selector = f'//div[contains(@class,"label") and contains(.,"{label}")]'
        response = self.check_if_exists(selector)
        if response is False:
            self.fail(f'Label {label} not found')
        selector = f'//div[contains(@id, "{type+index}")]//input[contains(@class,"input") and contains(@placeholder,"{placeholder}")]'
        elem = self.check_if_exists(selector)
        if elem is False:
            self.fail(f'Text input not found')
        elem.send_keys(value)
        if next:
            self.next()

    def fill_textarea(self, label, value, next=True, placeholder="Your answer here", type="textarea-input", index="0"):
        selector = f'//div[contains(@class,"label") and contains(.,"{label}")]'
        self.check_if_exists(selector)
        selector = f'//div[contains(@id, "{type+index}")]//textarea[contains(@class,"input") and contains(@placeholder,"{placeholder}")]'
        elem = self.check_if_exists(selector)
        if elem is False:
            self.fail(f'TextArea input not found')
        elem.send_keys(value)
        if next:
            self.next()

    def fill_phone(self, label, value, next=True, placeholder="(000)000-0000", type="phone-input", index="0"):
        selector = f'//div[contains(@class,"label") and contains(.,"{label}")]'
        response = self.check_if_exists(selector)
        if response is False:
            self.fail(f'Label {label} not found')
        selector = f'//div[contains(@id, "{type+index}")]//input[contains(@class,"input") and contains(@placeholder,"{placeholder}")]'
        elem = self.check_if_exists(selector)
        if elem is False:
            self.fail(f'Phone input not found')
        elem.send_keys(value)
        if next:
            self.next()

    def fill_date(self, label, value, next=True, type="date-input", index="0"):
        selector = f'//div[contains(@class,"label") and contains(.,"{label}")]'
        response = self.check_if_exists(selector)
        if response is False:
            self.fail(f'Label {label} not found')
        selector = f'//div[contains(@id, "{type+index}")]//input[contains(@class,"input") and contains(@type,"date")]'
        elem = self.check_if_exists(selector)
        if elem is False:
            self.fail(f'Date input not found')
        elem.send_keys(value)
        if next:
            self.next()

    def fill_option(self, label, value, next=True, buttonText="Next", type="multiple-choice-input", index="0"):
        selector = f'//div[contains(@class,"label") and contains(.,"{label}")]'
        response = self.check_if_exists(selector)
        if response is False:
            self.fail(f'Label {label} not found')
        if buttonText:
            selector = f'//div[contains(@id, "{type+index}")]//div[contains(@class,"radiobox") and contains(.,"{value}")]'
            elem = self.check_if_exists(selector)
            if elem is False:
                self.fail(f'Option {value} not found')
            elem.click()
            if next:
                self.next()
        else:
            selector = f'//div[contains(@class,"multiple-choice-button") and contains(.,"{value}")]'
            elem = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, selector)))
            elem.click()

    def fill_multiple_options(self, label, values, next=True, type="multiple-choice-input", index="0"):
        selector = f'//div[contains(@class,"label") and contains(.,"{label}")]'
        response = self.check_if_exists(selector)
        if response is False:
            self.fail(f'Label {label} not found')
        for value in values:
            selector = f'//div[contains(@id, "{type+index}")]//div[contains(@class,"checkbox") and contains(.,"{value}")]'
            elem = self.check_if_exists(selector)
            if elem is False:
                self.fail(f'Option {value} not found')
            elem.click()
        if next:
            self.next()

    def fill_dropdown(self, label, value, next=True, type="dropdown-input", index="0"):
        selector = f'//div[contains(@class,"label") and contains(.,"{label}")]'
        response = self.check_if_exists(selector)
        if response is False:
            self.fail(f'Label {label} not found')
        selector = f'//div[contains(@id, "{type+index}")]//div[contains(@class, "v-select")]'
        elem = self.check_if_exists(selector)
        elem.click()
        if elem is False:
            self.fail(f'Dropdown Button {value} not found')
        selector = f'//li[contains(@class,"vs__dropdown-option") and contains(.,"{value}")]'
        elem = self.check_if_exists(selector)
        if elem is False:
            self.fail(f'Dropdown Option {value} not found')
        elem.click()
        if next:
            self.next()

    def fill_card(self, label, value, next=True, type="cards-input", index="0"):
        selector = f'//div[contains(@class,"label") and contains(.,"{label}")]'
        response = self.check_if_exists(selector)
        if response is False:
            self.fail(f'Label {label} not found')
        selector = f'//div[contains(@id, "{type+index}")]//h3[contains(@class,"card-title") and contains(.,"{value}")]'
        elem = self.check_if_exists(selector)
        if elem is False:
            self.fail(f'Card {value} not found')
        elem.click()
        if next:
            self.next()

    def fill_file(self, label, value,  next=True, type='file-input', index="0"):
        selector = f'//div[contains(@class,"label") and contains(.,"{label}")]'
        response = self.check_if_exists(selector)
        if response is False:
            self.fail(f'Label {label} not found')
        selector = f'//div[contains(@id, "{type+index}")]//input[contains(@class,"input") and contains(@type,"file")]'
        elem = self.check_if_exists(selector)
        if elem is False:
            self.fail(f'File input not found')
        elem.send_keys(value)
        if next:
            self.next()

    def next(self):
        elem = self.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'next-button')))
        elem.click()

    def test_purchase_requester(self):  # ✅
        self.driver.get(
            f"{EXAMPLE_DOMAIN}/f036497f-4069-4010-b7a8-2ebed126d872")
        self.wait.until(EC.title_is('Purchase Requester'))
        self.next()

        self.expect_text('Hi! Welcome to our Purchase Requester.')
        self.fill_text('What is the title of this expense?',
                       'Figura de ação do naruto')
        self.fill_text('How much was this expense?',
                       '100', type='number-input')
        self.fill_option('Is this a monthly recurring expense?', 'no')
        self.fill_option(
            'To which department does this expense belong?', 'Engineering')
        self.fill_text('Briefly describe what this expense is for.',
                       'Melhorar a moral da equipe')
        self.fill_option('What type of expense is this?', 'misc')
        self.fill_date('When is this expense due?', '05/30/2022')
        self.expect_text(
            "We've registered this expense succesfully. Thanks! See ya next time.", False)

    def test_simple_quiz(self):  # ✅
        self.driver.get(
            f"{EXAMPLE_DOMAIN}/8e174c9a-ffe7-44fe-9950-ceafbd7c4bec")
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
        self.fill_text('Find the sum', '55', type='number-input')
        self.expect_text('I see you, smarty-pants!')
        self.expect_text('I can feel our day')
        self.expect_text('Give me a spin')
        self.expect_link('Try Abstra Cloud free now', 'abstracloud.com')
        self.expect_text('Thank you', False)

    def test_buying_intention_form(self):  # ✅
        self.driver.get(
            f"{EXAMPLE_DOMAIN}/2ef3700b-9d75-49bb-9c60-7924a0cb8c19")
        self.wait.until(EC.title_is('Upgrade Abstra Cloud'))
        self.next()

        self.expect_text(
            'Thank you for showing interest in our standard plan. We need some informations to get in touch.')
        self.fill_text('Name', 'Abstra Bot')
        self.fill_text('Email', 'email@abstra.app',
                       placeholder="Your email here", type='email-input')
        self.fill_text('Company name', 'Abstra')
        self.expect_text(
            "We've got your information, we'll get in contact soon! 😉", False)

    def test_subscribe_to_feature(self):  # ✅
        self.driver.get(
            f"{EXAMPLE_DOMAIN}/b871dce9-8a1d-4511-aa64-cc857e7a3950")
        self.wait.until(EC.title_is('Subscribe to Feature'))
        self.next()

        self.expect_text(
            'Hi there. Thanks for your interest in our upcoming features!')
        self.expect_text(
            "We're almost ready to launch. Let's sign you up to get the news first-hand.")
        self.fill_text('Firstly, what is your first name?', 'Abstra')
        self.fill_text('What is your last name?', 'Bot')
        self.fill_text("Great! What's your email?", 'email@abstra.app')
        self.expect_text(
            "All set, Abstra! You'll be notified as soon as we launch 😎🚀", False)

    def test_dev_marketplace(self):  # ✅
        self.driver.get(
            f"{EXAMPLE_DOMAIN}/33ddb3d0-af07-4f35-84fb-65e30125fd06")
        self.wait.until(EC.title_is('Dev Marketplace'))
        self.next()

        self.expect_text('Hey there. Welcome to our marketplace.')
        self.fill_option('What are you looking for today?',
                         "I'm a dev, looking for a job opening")
        self.fill_option("Very cool. What do you need?",
                         "I'd like to check out the job board.")
        self.fill_option(
            'Do you want to view the whole board or add a filter?', 'Add a filter')
        self.fill_option('What would you like to filter by?',
                         'Seniority needed')
        self.fill_dropdown('What is your seniority?', 'Senior')
        self.fill_card(
            'Select your desired job to get in touch with the company:', 'Database Tech')
        self.expect_text(
            "Love to see it. We're sending an email to connect you and the company right now. Be sure to check your inbox in the next few minutes.")
        self.expect_link('If you have any questions, you can get in touch with us here.',
    #                      'https://meetings.hubspot.com/sophia-faria/abstra-cloud-onboarding')

    def test_vacation_approval(self):  # ❌
        self.driver.get(
            f"{EXAMPLE_DOMAIN}/842f9872-59fd-4735-8b9a-4e6f5065a96e")
        self.wait.until(EC.title_is('Vacation Approval'))
        self.next()

        self.expect_text(
            'Hi there! You have a new vacation request.')
        self.expect_text(
            'Abby from the Marketing team has requested 15 days of vacation, from 08/18/22 to 09/02/22.')
        self.expect_text(
            'They’ve taken 12 days off in the last 12 months and have 18 remaining days to request, according to company policy.')
        self.fill_option(
            'Do you approve this request for 15 days starting 08/18/22?', 'Yes')
        self.expect_text("We've registered your approval successfully!")
        self.expect_link("Click here to add Abby's vacation to your calendar",
                         'https://calendar.google.com/calendar/render?action=TEMPLATE&dates=20220818%2F20220902&details=Enjoy%21&text=Abby%27s+Vacation')

    def test_insert_saving_incomes(self):  # ❌
        self.driver.get(
            f"{EXAMPLE_DOMAIN}/9636b0b4-7cdc-4ae7-9762-8f939555d2f9")
        self.wait.until(EC.title_is('Insert income savings'))
        self.next()

        self.expect_text('Hey there.')
        self.fill_file('Upload your .xlsx file',
                       '/Users/felipereyel/Abstra/Downloads/tests-example.xls')
        self.expect_text(
            "All your savings income info has been inputed. Simple as that", False)

    def test_self_checkin(self):  # ❌
        self.driver.get(
            f"{EXAMPLE_DOMAIN}/b0a39028-1988-42c8-b04b-b230c70c9bb3")
        self.wait.until(EC.title_is('Self check-in'))
        self.next()

        self.fill_text('Welcome to Dr', 'Abstra')
        self.fill_text('What is your last name?', 'Bot')
        self.fill_text('What is your middle initial?', '')
        self.fill_text('Ok. What is your email?', 'abstra@bot.com')
        self.fill_date('What is your date of birth, Abstra', '05/30/2022')
        self.fill_dropdown('In which country do you currently live?', 'Brazil')
        self.fill_dropdown(
            'In which city do you currently live?', 'Rio de Janeiro')
        self.fill_text(
            'Ok! Please add your street address in Brazil.', 'Rua Teste Numero Teste')
        self.fill_text("And what's the number?", 10, type='number-input')
        self.fill_text('Apartment or unit:', 'teste 21231')
        self.fill_text('Zip code:', '123123121231', type='number-input')
        self.fill_phone('What is your primary phone number?', '11999999999')
        self.fill_option(
            'What type of identification can you provide?', "driver's license")
        self.fill_text('What is the identification number?', '123121231')
        self.fill_date(
            'What is the identification expiration date?', '05/30/2022')
        self.expect_text(
            "We're done with personal info! Let's move on to your medical history.")
        self.fill_text(
            'What is your last known weight, in kilograms?', '70', type='number-input')
        self.fill_text('What is your height, in centimeters?',
                       '180', type='number-input')
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

    def test_invoice_factoring_calculator(self):  # ❌
        self.driver.get(
            f"{EXAMPLE_DOMAIN}/56aee472-37a9-49e7-8f4b-9460c84dbc92")
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
            'What is the total value of this invoice?', '500', False, index="1", type='number-input')
        self.fill_date('When is this invoice due?', '30/05/2022', index="2")
        self.fill_dropdown(
            'Choose a supplier from this list to calculate risk multiplier.', 'Mediocre Thing Doer')
        self.expect_text(
            "OK! Mediocre Thing Doer has a risk multiplier of 2 because they sometimes delay payment on invoices but have never defaulted. The new updated interest rate is 2.0%.")
        self.expect_text(
            'The take rate for this invoice is calculated at 2.0% over -1 months, given the invoice due date, assignor credit score and relevant supplier historical data.', False)
        self.expect_text(
            'The amount payable for this invoice is $510.0.', False)

    def test_certificate_maker(self):  # ❌
        self.driver.get(
            f"{EXAMPLE_DOMAIN}/82f4a14b-1494-4818-8455-cb6c76af08eb")
        self.wait.until(EC.title_is('Certificate Maker'))
        self.next()

        self.expect_text(
            "Quick tip before we begin: make sure you have the correct file in your workspace's file system.")
        self.expect_text(
            'Welcome to our Certificate Maker!')
        self.fill_option(
            'Do you want to generate a single certificate or multiple, from a spreadsheet?', 'single', buttonText=None)
        self.fill_text('What is the course name?', 'Python')
        self.fill_text(
            'How many hours does this course account for?', '10', type='number-input')
        self.fill_date('What date should be on the certificate?', '2020-01-01')
        self.fill_text("What is the student's full name?", 'Abstra Bot')
        self.expect_text('All done! Your certificate is ready! 🧑‍🎓', False)
        self.expect_file('Download here', 'generated_certificate.docx')

    def test_tax_calculator(self):  # ❌
        self.driver.get(
            f"{EXAMPLE_DOMAIN}/cbdc145f-608d-4a13-a796-641f728aa6ee")
        self.wait.until(EC.title_is('Tax calculator'))
        self.next()

        self.expect_text('Hello! Fill in the data below:', False)
        self.fill_text('Invoice value without taxes (BRL)',
                       '100', False, index="1")
        self.fill_text('Cofins (%)', '5', False, index="2")
        self.fill_text('Csll (%)', '5', False, index="3")
        self.fill_text('Irpj (%)', '25', False, index="4")
        self.fill_text('Pis (%)', '10', index="5")
        self.expect_text(
            'Invoice value with taxes: R$ 181.82', False)
        self.expect_text('Cofins: R$ 9.09', False)
        self.expect_text('Csll: R$ 9.09', False)
        self.expect_text('Irpj: R$ 45.45', False)
        self.expect_text('Pis: R$ 18.18')

    def test_customer_registration(self):  # ❌
        self.driver.get(
            f"{EXAMPLE_DOMAIN}/81e15ebb-40bf-444e-8c83-35aafbc033b9")
        self.wait.until(EC.title_is('Customer registration'))
        self.next()

        self.fill_option(
            'Hello! Before continuing, what would you like to do?', 'Register a new customer',)
        self.fill_text('Name', 'Abstra', False, index="0")
        self.fill_text('Email', 'email@abstra.app', False,
                       'Your email here', 'email-input', "1")
        self.fill_dropdown('Legal entity', 'Physical', False, index="2")
        self.fill_dropdown('Payment Frequency', 'Monthly', False, index="3")
        self.fill_dropdown('Payment Method', 'Credit card', False, index="4")
        self.fill_text('Country', 'Brazil', False, index="5")
        self.fill_date('Registration date', '2020-01-01', index="6")
        self.expect_text(
            'Perfecto. Your new customer has been registered 😎', False)


if __name__ == '__main__':
    unittest.main()
