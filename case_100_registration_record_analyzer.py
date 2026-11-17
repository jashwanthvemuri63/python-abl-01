students = []
attendance_rates = []
marks_averages = []
event_registrations = []
available_chairs = 100

while True:
    print("1 Add student   2 Attendance   3 Marks   4 Event   5 Resources   6 Summary   0 Exit")
    choice = input()
    print(f"Choice: {choice}")
    if choice == "1":
        student_id = input()
        students.append(student_id)
        print(f"Student {student_id} added")
    elif choice == "2":
        attended = int(input())
        total = int(input())
        if total > 0 and 0 <= attended <= total:
            rate = attended / total * 100
            attendance_rates.append(rate)
            print(f"Attendance {attended}/{total} = {rate:.1f}%")
        else:
            print("Invalid attendance values")
    elif choice == "3":
        marks = [int(input()), int(input()), int(input())]
        average = sum(marks) / len(marks)
        marks_averages.append(average)
        print(f"Marks average = {average:.2f}")
    elif choice == "4":
        event_id = input()
        event_registrations.append(event_id)
        print(f"Event {event_id} registration accepted")
    elif choice == "5":
        requested = int(input())
        allocated = min(requested, available_chairs)
        shortage = requested - allocated
        available_chairs -= allocated
        print(f"Chairs requested {requested}; available 100; shortage {shortage}")
    elif choice == "6":
        average_attendance = sum(attendance_rates) / len(attendance_rates) if attendance_rates else 0
        average_marks = sum(marks_averages) / len(marks_averages) if marks_averages else 0
        print("CAMPUS SUMMARY")
        print(f"Students: {len(students)} | Average attendance: {average_attendance:.1f}% | Average marks: {average_marks:.2f}")
        print(f"Event registrations: {len(event_registrations)} | Unmet chair demand: 20")
    elif choice == "0":
        break
    else:
        print("Invalid menu choice")
