import pandas as pd

def dailyAverage(file_path= None, day=None, month=None, columnToAverage=28):
	df = pd.read_excel(file_path)

	if 'Day' not in df.columns or 'Month' not in df.columns:
		raise ValueError("The dataframe must have 'Day' and 'Month' columns.")

	if day is not None:
		df = df[df['Day'] == day]
	if month is not None:
		df = df[df['Month'] == month]

	if columnToAverage >= len(df.columns):
		raise ValueError("The specified column to average does not exist.")

	averageValue = df.iloc[:, columnToAverage].mean()

	averageValue = averageValue * 100

	print(f'The daily average % occupied of month {month} and on a {day} is: {averageValue:.2f}%')

def averagePerTime(file_path=None, day=None, month=None, start = None, end = None):
	df = pd.read_excel(file_path)

	if 'Day' not in df.columns or 'Month' not in df.columns:
		raise ValueError("The dataframe must have 'Day' and 'Month' columns.")

	if day is not None:
		df = df[df['Day'] == day]
	if month is not None:
		df = df[df['Month'] == month]

	rowAVG = df.iloc[:, start:end].mean()

	averageTotal = rowAVG.mean()

	averageTotal = averageTotal * 100

	print(f'The percentage of courts used in {month} on a {day} {start} {end} : {averageTotal:.3f} %')


def monthlyAverage(file_path = None, month = None, column_index=28):

	df = pd.read_excel(file_path)
	
	month_data = df[df.iloc[:, 1] == month]
	
	month_data.iloc[:, column_index] = pd.to_numeric(month_data.iloc[:, column_index], errors='coerce')
	
	average_value = month_data.iloc[:, column_index].mean()
	
	percentage = average_value * 100
	
	print(f"The average percentage of month {month} is: {percentage:.2f} %")

file_path = 'masterPickleball.xlsx'

monthList = [5, 6, 7]
dayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
timeRange = [[4,8],[9,12],[13,16],[17,22],[23, 26], [27,29]]

for day in dayList:
    for start, end in timeRange:
        averagePerTime(file_path=file_path, day=day, month=7, start=start, end=end)

'''
for month in monthList:
	for day in dayList:
		dailyAverage(file_path = file_path, day = day, month = month)
'''
