from datetime import datetime as dt
import os
print(os.getenv('GITHUB_OLD_DATE'))
print(os.getenv('GITHUB_NEW_DATE'))

date_diff = dt.strptime(os.environ['GITHUB_NEW_DATE'], "%Y-%m-%d") - dt.strptime(os.environ['GITHUB_OLD_DATE'], "%Y-%m-%d")
print(date_diff)
if data_diff.days > 92: raise ValueError("date diff to high")
