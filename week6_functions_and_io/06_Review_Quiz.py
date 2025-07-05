# Quiz) Your company requires a weekly report to be written once a week.
# The report must always follow this format:

# - Week X Weekly Report -
# Department:
# Name:
# Summary:

# Task: Generate report files from Week 1 to Week 50.

# Condition: The file names should be like '1_week.txt', '2_week.txt', ..., '50_week.txt'.

for i in range(1, 51):
    with open(f"{i}_week.txt", "w", encoding="utf8") as report_file:
        report_file.write(f"- Week {i} Weekly Report -\n")
        report_file.write("Department:\n")
        report_file.write("Name:\n")
        report_file.write("Summary:\n")

# Running this script will generate 50 files with the weekly report template.
