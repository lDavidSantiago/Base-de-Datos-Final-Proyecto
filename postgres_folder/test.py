from datetime import datetime

date_string = "2023-03-01"
date_object = datetime.strptime(date_string, "%Y-%m-%d").date()

print(date_object)