
from seismograph.ext import selenium

from elements.home_page_elements import HomePageElements


class HomePage(selenium.Page):

    elements = selenium.PageElement(HomePageElements) #type: HomePageElements

    def check_elements(self, case):
        self.check_button_full_stack_engineer_element(case)
        self.check_button_qa_engineer_element(case)
        self.check_job_header_element(case)
        self.check_job_description_element(case)

    def check_title(self, case, title):

        page_title = self.browser.title
        message = "The title doesn't match the expected result.\n The title of the page: {0}\n " \
                  "Expected result: {1}".format(page_title, title)
        case.assertion.true(page_title == title, message)

    def check_button_full_stack_engineer_element(self, case):
        case.assertion.true(self.elements.full_stack_engineer_button.exist)

    def check_button_qa_engineer_element(self, case):
        case.assertion.true(self.elements.qa_engineer_button.exist)

    def click_button_full_stack_engineer(self):
        self.elements.full_stack_engineer_button.click()

    def click_button_qa_engineer(self):
        self.elements.qa_engineer_button.click()

    def check_name_button_full_stack_engineer(self, case, button_name):
        case.assertion.true(self.elements.full_stack_engineer_button.text==button_name)

    def check_name_button_qa_engineer(self, case, button_name):
        case.assertion.true(self.elements.qa_engineer_button.text==button_name)

    def acive_button_check(self, case, button_name, color):
        case.assertion.true(self.elements.active_button.text==button_name)
        self.check_button_color(case, self.elements.active_button, color)

    def check_qa_engineer_button_color(self, case, color):
        self.check_button_color(case, self.elements.qa_engineer_button, color)

    def check_full_stack_engineer_button_color(self, case, color):
        self.check_button_color(case, self.elements.full_stack_engineer_button, color)

    def check_button_color(self, case, button_object, color):
        css_property = button_object.value_of_css_property("background")
        case.assertion.true(css_property == color)

    def check_job_header_element(self, case):
        case.assertion.true(self.elements.job_header.exist)

    def check_job_description_element(self, case):
        case.assertion.true(self.elements.job_description.exist)

    def check_job_header(self, case, header):
        job_header = self.elements.job_header.text
        message = "The header doesn't match the expected result.\n The header of the page: {0}\n " \
                  "Expected result: {1}".format(job_header, header)

        case.assertion.true(job_header == header, message)

    def check_job_description(self, case, description):
        job_description = self.elements.job_description.text.encode("utf-8").split("\n")[1]
        message = "Job description doesn't match the expected result.\n Job description of the page: {0}\n " \
                  "Expected result: {1}".format(job_description, description)

        case.assertion.true(job_description == description, message)