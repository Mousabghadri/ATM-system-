import os

class Screen:
    def show_message(self, message):
        print(message)

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")
