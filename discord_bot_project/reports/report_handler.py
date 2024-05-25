# reports/report_handler.py

class ReportHandler:
    def __init__(self):
        self.reports = []

    def add_report(self, report):
        self.reports.append(report)

    def get_reports(self):
        return self.reports

    def clear_reports(self):
        self.reports.clear()