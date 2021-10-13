class App:
    def __init__(self):
        self.app_name = 'App'
        print(1)


class GetInput:
    def __init__(self):
        super().__init__()
        self.get_input_name = 'GetInput'
        print(2)


class StartApp(GetInput, App):
    def __init__(self):
        super().__init__()
        self.start_app_name = 'StartApp'
        print(3)
        print(self.app_name)
        print(self.get_input_name)
        print(self.start_app_name)


StartApp()
