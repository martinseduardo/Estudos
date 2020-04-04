from datetime import datetime

class Date:
    def __init__(self):
        self.register_date = datetime.today()

    def __str__(self):
        return self.register_date.strftime("%H:%M %A %d/%m/%Y")

    def registration_time(self):
        current_date = datetime.today()
        return current_date - self.register_date