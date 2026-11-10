
import re
import os

def analyze_log_file(file_path):

    log_counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    total_lines = 0
    valid_lines = 0
    invalid_lines = 0

    log_pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (INFO|WARNING|ERROR) (.+)$"

    try:
        with open(file_path, "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                total_lines += 1

                match = re.match(log_pattern, line)

                if match:

                    timestamp = match.group(1)
                    log_level = match.group(2)
                    message = match.group(3)

                    log_counts[log_level] += 1
                    valid_lines += 1

                else:
                    invalid_lines += 1

        report = f"""
APPLICATION LOG ANALYSIS REPORT
================================

Total Log Entries : {total_lines}
Valid Entries     : {valid_lines}
Invalid Entries   : {invalid_lines}

INFO Count        : {log_counts["INFO"]}
WARNING Count     : {log_counts["WARNING"]}
ERROR Count       : {log_counts["ERROR"]}

================================
"""

        return report

    except FileNotFoundError:
        print("Error: Log file not found.")
        return None

    except Exception as e:
        print("An unexpected error occurred:", e)
        return None


def save_report(report, report_path):

    try:
        if report is None:
            return

        os.makedirs(os.path.dirname(report_path), exist_ok=True)

        with open(report_path, "w") as file:
            file.write(report)

        print("Report successfully saved to:", report_path)

    except Exception as e:
        print("Error while saving report:", e)


if __name__ == "__main__":

    log_file_path = "Logs/Application.log"
    report_file_path = "Reports/analysis_report.txt"

    analysis_report = analyze_log_file(log_file_path)

    if analysis_report is not None:

        print(analysis_report)

        save_report(
            analysis_report,
            report_file_path
        )
