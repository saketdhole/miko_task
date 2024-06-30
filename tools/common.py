import inspect
import logging
import os
from datetime import date
import csv


class Common:
    def get_logs(self):
        logger_name = inspect.stack()[1][3]
        log = logging.getLogger(logger_name)
        logfile = logging.FileHandler(
            filename=f'{os.path.join(os.getcwd(), f"Test_output/Logs/logfile-{date.today()}.log")}')
        log_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(filename)s:%(lineno)s %(message)s")
        logfile.setFormatter(log_formatter)
        log.addHandler(logfile)
        log.setLevel(logging.INFO)
        return log

    def get_csv_data(self, csv_file):
        csv_path = os.path.join(os.getcwd(), "resources", "data", csv_file)
        with open(csv_path, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                return row
        return None
