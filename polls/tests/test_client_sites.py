from selenium import webdriver
from django.test import LiveServerTestCase
from polls.models.question import Question
from polls.models.choice import Choice
from django.contrib.auth.models import User
from django.test.client import Client
from decouple import config


class FrontendTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('-–incognito')
        cls.selenium = webdriver.Chrome(
            chrome_options=chrome_options,
            executable_path=config('CHORME_DRIVER_PATH', default='')
        )
        super(FrontendTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(FrontendTest, cls).tearDownClass()

    def setUp(self) -> None:
        self.client = Client()
        User.objects.create_user(username='User',
                                 email='user@testing.com',
                                 password='UserNotLoser')
        Question.objects.create(question_text="Is this a test?")
        Choice.objects.create(question_id=Question.objects.all()[0].id,
                              choice_text="This is my choice!!")
        self.client.login(username='User', password='UserNotLoser')
        cookie = self.client.cookies['sessionid']
        self.selenium.get(self.live_server_url + '/polls/')
        self.selenium.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})

    def test_header_message(self):
        self.selenium.get(self.live_server_url + '/polls/')
        h2 = self.selenium.find_element_by_tag_name("h2")
        self.assertIn('Hot Topics', h2.text)

    def test_have_question(self):
        self.selenium.get(self.live_server_url + '/polls/')
        questions = self.selenium.find_elements_by_class_name('question')
        self.assertTrue(len(questions) > 0)

    def test_question_link(self):
        self.selenium.get(self.live_server_url + '/polls/')
        self.selenium.find_element_by_id(f'questionId{Question.objects.all()[0].id}').click()
        self.assertURLEqual(self.selenium.current_url,
                            self.live_server_url + f'/polls/{Question.objects.all()[0].id}/')

    def test_voting_for_first_choice(self):
        self.selenium.get(self.live_server_url + f'/polls/{Question.objects.all()[0].id}/')
        self.selenium.find_element_by_id('choice1').click()
        self.selenium.find_element_by_id('voteButton').click()
        self.assertURLEqual(self.live_server_url +
                            f'/polls/{Question.objects.all()[0].id}/results/',
                            self.selenium.current_url)
