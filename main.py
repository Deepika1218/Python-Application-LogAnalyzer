
import re
import os

# Log file paths
file_path = "Logs/Application.log"
report_path = "Reports/analysis_report.txt"

# Regex pattern
pattern = r"^(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+(INFO|WARNING|ERROR)\s+(.*)$"


# Function to analyze log file
def analyze_log_file(file_path):

    error_count = 0
    warning_count = 0
    info_count = 0
    total_lines = 0
    invalid_lines = 0

    report = []

    if not os.path.exists(file_path):
        raise FileNotFoundError("Log file not found!")

    with open(file_path, "r") as file:

        report.append("========== APPLICATION LOG ANALYZER ==========")

        for line in file:

            total_lines += 1
            line = line.strip()

            match = re.search(pattern, line)

            if match:

                timestamp = match.group(1)
                log_level = match.group(2)
                message = match.group(3)

                report.append("")
                report.append("Timestamp: " + timestamp)
                report.append("Log Level: " + log_level)
                report.append("Message: " + message)

                if log_level == "ERROR":
                    error_count += 1

                elif log_level == "WARNING":
                    warning_count += 1

                elif log_level == "INFO":
                    info_count += 1

            else:
                invalid_lines += 1

    # Generate summary
    report.append("")
    report.append("========== LOG ANALYSIS REPORT ==========")

    report.append("Total Log Entries: " + str(total_lines))
    report.append("Valid Log Entries: " + str(total_lines - invalid_lines))
    report.append("Invalid Log Entries: " + str(invalid_lines))

    report.append("")
    report.append("----- LOG LEVEL SUMMARY -----")

    report.append("ERROR Count: " + str(error_count))
    report.append("WARNING Count: " + str(warning_count))
    report.append("INFO Count: " + str(info_count))

    report.append("")
    report.append("========== ANALYSIS COMPLETED ==========")

    return report


# Function to save report
def save_report(report, report_path):

    os.makedirs(os.path.dirname(report_path), exist_ok=True)

    with open(report_path, "w") as file:

        for line in report:
            file.write(line + "\n")

    print("\nReport successfully saved to:", report_path)


# Main program
try:

    result = analyze_log_file(file_path)

    # Display report in terminal
    for line in result:
        print(line)

    # Save report to file
    save_report(result, report_path)


except FileNotFoundError as e:

    print("Error:", e)

except Exception as e:

    print("Unexpected error:", e)
