students = [
    ("STU-01", [55, 42, 38], 82, True),
    ("STU-02", [62, 54, 48], 72, True),
    ("STU-03", [45, 45, 46], 90, False),
]
pass_mark = 40
attendance_required = 75
print("Pass mark: 40 | Attendance required: 75% | Prerequisites: complete\n")
eligible_count = 0
for student_id, marks, attendance, prerequisite_complete in students:
    reasons = []
    for subject_index in range(len(marks)):
        if marks[subject_index] < pass_mark:
            reasons.append(f"Subject {subject_index + 1} mark is {marks[subject_index]} (minimum {pass_mark})")
    if attendance < attendance_required:
        reasons.append(f"Attendance is {attendance}% (minimum {attendance_required}%)")
    if not prerequisite_complete:
        reasons.append("Prerequisite completion is missing")
    if len(reasons) == 0:
        print(f"{student_id}  ELIGIBLE")
        eligible_count += 1
    else:
        print(f"{student_id}  NOT ELIGIBLE  - " + "; ".join(reasons))
print(f"\nAudit complete: {eligible_count} eligible, {len(students) - eligible_count} records need attention")
