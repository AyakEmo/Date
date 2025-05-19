class Date:
    def __init__(self, day, month, year):
        """
        Створює нову дату.

        Аргументи:
            day (int): день (1-31)
            month (int): місяць (1-12)
            year (int): рік (додатнє число)

        Викидає помилку, якщо дата неправильна.
        """

        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise TypeError("День, місяць і рік мають бути цілими числами")


        if year < 1:
            raise ValueError("Рік має бути додатнім числом")


        if month < 1 or month > 12:
            raise ValueError("Місяць має бути від 1 до 12")


        max_days = self._get_days_in_month(month, year)
        if day < 1 or day > max_days:
            raise ValueError(f"Для місяця {month} день має бути від 1 до {max_days}")

        self.day = day
        self.month = month
        self.year = year

    def _get_days_in_month(self, month, year):
        if month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return 29 if self._is_leap_year(year) else 28
        else:
            return 31

    def _is_leap_year(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year

    def __lt__(self, other):
        if self.year != other.year:
            return self.year < other.year
        if self.month != other.month:
            return self.month < other.month
        return self.day < other.day

    def is_leap_year(self):
        return self._is_leap_year(self.year)

    def add_days(self, days):
        new_day = self.day + days
        new_month = self.month
        new_year = self.year

        while new_day > self._get_days_in_month(new_month, new_year):
            new_day -= self._get_days_in_month(new_month, new_year)
            new_month += 1
            if new_month > 12:
                new_month = 1
                new_year += 1

        return Date(new_day, new_month, new_year)

    def days_between(self, other):
        if self == other:
            return 0

        if self > other:
            return -other.days_between(self)

        days = 0
        temp = Date(other.day, other.month, other.year)

        while temp < self:
            temp = temp.add_days(1)
            days += 1

        return days


if __name__ == "__main__":
    print("=== Приклади роботи з класом Date ===")

    today = Date(20, 5, 2023)
    birthday = Date(15, 8, 2023)
    leap_date = Date(29, 2, 2020)

    print(f"\nСьогодні: {today}")
    print(f"День народження: {birthday}")
    print(f"Високосна дата: {leap_date}")

    print(f"\n2020 високосний? {leap_date.is_leap_year()}")
    print(f"2023 високосний? {today.is_leap_year()}")

    print(f"\n{today} < {birthday}? {today < birthday}")
    print(f"{today} == {birthday}? {today == birthday}")

    future_date = today.add_days(30)
    print(f"\nЧерез 30 днів буде: {future_date}")

    days_left = today.days_between(birthday)
    print(f"\nДо дня народження залишилось {days_left} днів")

    print("\nСпробуємо створити неправильні дати:")
    try:
        wrong_date1 = Date(31, 4, 2023)
    except ValueError as e:
        print(f"Помилка: {e}")

    try:
        wrong_date2 = Date(1, 13, 2023)
    except ValueError as e:
        print(f"Помилка: {e}")

    try:
        wrong_date3 = Date(1, 1, "2023")
    except TypeError as e:
        print(f"Помилка: {e}")