def printing_name_and_args(args):
    for arg in args:
        print("Имя функции:", arg.__name__, end='. ')
        if not any(arg.__code__.co_varnames):
            print("Аргументы отстуствуют")
        else:
            print("Аргумент(ы) функции:", arg.__code__.co_varnames)


def open_browser(browser_name):
    pass

def go_to_companyname_homepage(page_url):
    pass

def find_registration_button_on_login_page():
    pass

functions = [open_browser, go_to_companyname_homepage, find_registration_button_on_login_page]

printing_name_and_args(functions)









