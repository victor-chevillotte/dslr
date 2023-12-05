import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

classes = [
	"Arithmancy",
	"Astronomy",
	"Herbology",
	"Defense Against the Dark Arts",
	"Divination",
	"Muggle Studies",
	"Ancient Runes",
	"History of Magic",
	"Transfiguration",
	"Potions",
	"Care of Magical Creatures",
	"Charms",
	"Flying"
]


def read_csv(path):
	try:
		df = pd.read_csv(path, index_col="Index")
	except FileNotFoundError:
		print("File not found. Please set dataset_train.csv in data folder")
		exit(1)
	return df


def main():
	df = read_csv("data/dataset_train.csv")
	df = df[classes]
	sns.pairplot(df)
	plt.show()
	
	print("From this visualization, what features are you going to use for your logistic regression?")


if __name__ == "__main__":
	main()
