import seismograph as seismograph
from seismograph import step
from seismograph.ext import selenium

from model.home_page_data import HomePageData
from pages.home_page import HomePage

program = seismograph.Program(config_path='etc.base')
suite = seismograph.Suite(__name__)

@suite.register
class TestQaEngineerButton(selenium.Case):
    def __init__(self, *args, **kwargs):
        super(TestQaEngineerButton, self).__init__(*args, **kwargs)
        self.url = self.config.get('SELENIUM_EX').get('PROJECT_URL')
        self.home_page_data = HomePageData()

    @step(1, "Open page dokkio.com")
    def open_home_page(self, browser):
        browser.go_to(self.url)

    @step(2, "Check page is loaded")
    def check_page_is_loaded(self, browser):
        self.home_page = HomePage(browser)
        self.home_page.check_title(self, self.home_page_data.title)

    @step(3, "Check no QA Engineer info is visible")
    def check_no_qa_engineer_visible(self):
        self.home_page.check_elements(self)
        self.home_page.acive_button_check(
            self, self.home_page_data.full_stack_engineer_button, self.home_page_data.active_button_color
        )
        self.home_page.check_job_header(self, self.home_page_data.full_stack_engineer_header)
        self.home_page.check_job_description(self, self.home_page_data.description_full_stack_engineer)
        self.home_page.check_qa_engineer_button_color(self, self.home_page_data.inactive_button_color)

    @step(4, "Click QA Engineer button")
    def click_qa_engineer_button(self):
        self.home_page.check_name_button_qa_engineer(self, self.home_page_data.qa_engineer_button)
        self.home_page.click_button_qa_engineer()

    @step(5, "Check QA Engineer info is visible")
    def check_qa_engineer_info_is_visible(self):
        self.home_page.check_qa_engineer_button_color(self, self.home_page_data.active_button_color)
        self.home_page.check_full_stack_engineer_button_color(self, self.home_page_data.inactive_button_color)

        self.home_page.check_job_header(self, self.home_page_data.qa_engineer_header)
        self.home_page.check_job_description(self, self.home_page_data.description_qa_engineer)

    @step(6, "Click Full Stack Engineer button")
    def click_full_stack_engineer_button(self):
        self.home_page.check_name_button_full_stack_engineer(self, self.home_page_data.full_stack_engineer_button)
        self.home_page.click_button_full_stack_engineer()

    @step(7, "Check Full Stack Engineer info is visible")
    def check_full_stack_engineer_info_visible(self):
        self.check_no_qa_engineer_visible()

if __name__ == '__main__':
    program()
    seismograph.main()

