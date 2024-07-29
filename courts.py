import pandas as pd

def dailyAverage(file_path='master.xlsx', day=None, month=None, column_to_average=28):
	df = pd.read_excel(file_path)

	if 'Day' not in df.columns or 'Month' not in df.columns:
		raise ValueError("The dataframe must have 'Day' and 'Month' columns.")

	if day is not None:
		df = df[df['Day'] == day]
	if month is not None:
		df = df[df['Month'] == month]

	if column_to_average >= len(df.columns):
		raise ValueError("The specified column to average does not exist.")

	average_value = df.iloc[:, column_to_average].mean()

	average_value = average_value * 100

	print(f'The daily average % occupied of month {month} and on a {day} is: {average_value:.2f}%')


def monthlyAverage(file_path = 'master.xlsx', month = None, column_index=28):

	df = pd.read_excel(file_path)
	
	month_data = df[df.iloc[:, 1] == month]
	
	month_data.iloc[:, column_index] = pd.to_numeric(month_data.iloc[:, column_index], errors='coerce')
	
	average_value = month_data.iloc[:, column_index].mean()
	
	percentage = average_value * 100
	
	print(f"The average percentage of month {month} is: {percentage:.2f} %")

file_path = 'master.xlsx'

dayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturady', 'Sunday']

data = dailyAverage(day = 'Thursday', month = 5)


