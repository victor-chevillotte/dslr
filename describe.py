import sys
import pandas as pd
import math 

def get_numeric_columns(df):
	numeric_columns = []
	for col in df.columns:
		try:
			float(df[col][0])
			numeric_columns.append(col)
		except ValueError:
			continue
	return numeric_columns

def create_describe_df(df):
	infos = ["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]
	columns = get_numeric_columns(df)
	describe_df = pd.DataFrame(columns = columns, index = infos)
	return describe_df

def read_csv(path):
	try:
		df = pd.read_csv(path, index_col = "Index")
	except FileNotFoundError:
		print("File not found")
		sys.exit(1)
	return df


def ft_std(values, mean):
	sum = 0
	for value in values:
		sum += (value - mean) ** 2
	return (sum / len(values)) ** 0.5

def analyze_data(df, describe_df):	
	for column_name in describe_df :
		sum = 0
		count = 0
		min = None
		max = None
		sorted_values = []
		for value in df[column_name]:
			if math.isnan(value):
				continue
			else :
				sorted_values.append(value)
				count += 1
				sum += value
				if min is None or value < min:
					min = value
				if max is None or value > max:
					max = value
		sorted_values.sort()
		describe_df[column_name]["Count"] = count
		describe_df[column_name]["Mean"] = sum / count
		describe_df[column_name]["Std"] = ft_std(sorted_values, describe_df[column_name]["Mean"])
		describe_df[column_name]["Min"] = min
		describe_df[column_name]["25%"] = sorted_values[int(count * 0.25)]
		describe_df[column_name]["50%"] = sorted_values[int(count * 0.5)]
		describe_df[column_name]["75%"] = sorted_values[int(count * 0.75)]
		describe_df[column_name]["Max"] = max
	return describe_df

		
def display (df, describe_df):
	# display lines as columns and columns as lines and display no numerical value if colomn of df is not in describe_df
	not_numeric_columns = []
	for column_name in df.columns:
		if column_name not in describe_df.columns:
			not_numeric_columns.append(column_name)
	describe_df = describe_df.T
	print(describe_df)
	print("\n")
	print("Not numeric columns : ", not_numeric_columns)

    
def main():
	if len(sys.argv) > 1:
		df = read_csv(sys.argv[1])
	else:
		print("Usage: python describe.py <path_to_dataset>")
		sys.exit(1)
	describe_df = create_describe_df(df)
	describe_df = analyze_data(df, describe_df)
	display(df, describe_df)
    
if __name__ == "__main__":
    main()