# TODO:
# 1. verify input date, time
## if true, then return true, save event to backend
## if false, send exception, handle in responses

# 2.


class Event:
    def __init__(self, date, time, location) -> None:
        self.date = date
        self.time = time
        self.location = location
        self.check_input(date, time, location)

    def check_input(self, date, time, location):
        """
        date = MM-DD
        time = HH:MM (am/pm)
        location = voice channels
        """
        self.verify_date(date)
        self.verify_time(time)

    def verify_date(self, date):
        try:
            month, day = date.split("-")
            print(f"month: {month}, day: {day}")
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                return True
            else:
                return False
        except Exception as e:
            print(f"Exception occured {e}")
            return False

    def verify_time(self, time):
        try:
            time_only, am_pm = time.split(" ")
            hour, minute = time_only.split(":")
            print(f"hour: {hour}, minute: {minute}, am_pm: {am_pm}")
            if (
                1 <= int(hour) <= 12
                and 0 <= int(minute) <= 59
                and (am_pm.lower() == "am" or am_pm.lower() == "pm")
            ):
                return True
            else:
                return False
        except Exception as e:
            print(f"Exception occured {e}")
            return False
