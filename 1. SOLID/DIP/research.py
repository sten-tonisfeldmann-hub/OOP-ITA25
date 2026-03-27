class Research:
    def __init__(self, browser):
        for child in browser.find_all_children_of("John"):
            print(f"John has a child called {child}")