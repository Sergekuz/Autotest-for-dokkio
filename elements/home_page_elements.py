from seismograph.ext import selenium


class HomePageElements(selenium.PageItem):
    qa_engineer_button = selenium.PageElement(
        selenium.query("#Jobs-2 > a")
    )

    full_stack_engineer_button = selenium.PageElement(
        selenium.query("#Jobs-1 > a")
    )

    active_button = selenium.PageElement(
        selenium.query(".iw-so-tab-active a")
    )

    job_header = selenium.PageElement(
        selenium.query(".iw-so-tab-active .job-header h3")
    )

    job_description = selenium.PageElement(
        selenium.query(".iw-so-tab-active .job-header")
    )