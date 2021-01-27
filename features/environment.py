from selenium import webdriver


def browser_init(context):
    """
    :param context: Behave context
    """
    context.chrome_instance = webdriver.Chrome()
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.chrome_instance.maximize_window()
    context.chrome_instance.implicitly_wait(4)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.chrome_instance.delete_all_cookies()
    context.chrome_instance.quit()
