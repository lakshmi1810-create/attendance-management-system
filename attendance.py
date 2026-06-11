class AttendanceManager:
    TOTAL_DAYS = 6

    def __init__(self):
        self.employees = []
        self.total_present = 0
        self.total_saturdays = 0

    @staticmethod
    def get_time(prompt: str) -> int:
        while True:
            try:
                time = int(input(prompt))

                if 0 <= time <= 24:
                    return time

                raise ValueError("Time must be between 0 and 24.")

            except ValueError as error:
                print(f"Error: {error}")

    @staticmethod
    def get_status(entry: int, exit: int) -> str:

        if entry <= 8 and exit == 18:
            return "Present"

        if entry <= 8 and exit > 18:
            return "Overtime"

        if (
            (7 <= entry <= 8 and 13 <= exit <= 17)
            or (9 <= entry <= 13 and exit >= 18)
        ):
            return "Half Day"

        if (
            (entry <= 8 and exit <= 12)
            or (entry >= 13 and exit <= 18)
        ):
            return "Short Day"

        return "Invalid"

    def add_employee(self):

        employee_name = input("Enter Employee Name: ").strip()

        attendance_count = 0

        print(f"\nAttendance for {employee_name}")

        for day in range(1, self.TOTAL_DAYS + 1):

            try:
                print(f"\nDay {day}")

                entry = self.get_time("Entry Time : ")
                exit = self.get_time("Exit Time  : ")

                if entry > exit:
                    raise ValueError(
                        "Entry time cannot be greater than exit time."
                    )

                if day == 6:
                    print("Status : Saturday")
                    self.total_saturdays += 1
                    continue

                status = self.get_status(entry, exit)

                print(f"Status : {status}")

                if status != "Invalid":
                    attendance_count += 1
                    self.total_present += 1

            except ValueError as error:
                print(f"Validation Error: {error}")

            except Exception as error:
                print(f"Unexpected Error: {error}")

        self.employees.append(
            {
                "name": employee_name,
                "present_days": attendance_count,
            }
        )

    def generate_report(self):

        print("\n" + "=" * 50)
        print("ATTENDANCE REPORT")
        print("=" * 50)

        for employee in self.employees:
            print(
                f"{employee['name']} : "
                f"{employee['present_days']} Present Days"
            )

        print("\n" + "=" * 50)
        print(f"Grand Total Present Days : {self.total_present}")
        print(f"Grand Total Saturdays    : {self.total_saturdays}")


def main():

    try:
        attendance_manager = AttendanceManager()

        employee_count = int(
            input("Enter Number of Employees: ")
        )

        for _ in range(employee_count):
            attendance_manager.add_employee()

        attendance_manager.generate_report()

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

    except ValueError:
        print("Please enter a valid number.")

    except Exception as error:
        print(f"Fatal Error: {error}")


if __name__ == "__main__":
    main()