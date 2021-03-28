from behave import given, when


@given("User opens Amazon Main Page")
def step_impl(context):
    context.app.main_page.open_main_page()


@when("Input {search_query} into the Search Field")
def step_impl(context, search_query):
    context.app.main_page.input_amazon_search(search_query)


@when("Hit the Search Icon")
def step_impl(context):
    context.app.main_page.click_search_icon()