import pandas as pd
import matplotlib.pyplot as plt

courses = [
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
    "Flying",
]

houses = ["Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff"]


def read_csv(path):
    try:
        df = pd.read_csv(path, index_col="Index")
    except FileNotFoundError:
        print("File not found. Please set dataset_train.csv in data folder")
        exit(1)
    return df


def display_histogram(path):
	df = read_csv(path)
	fig, axs = plt.subplots(3, 5, figsize=(15, 15))
	index = 0
	for course in courses:
		# Turn grid into array of length [number of features]
		axs = axs.flatten()[:len(courses)]
		for house in houses:
			axs[index].hist(df[df["Hogwarts House"] == house][course], alpha=0.5, label=house)
		axs[index].set_title(course)
		index += 1
            
    # Set house legend in bottom right corner
	handles, labels = axs[0].get_legend_handles_labels()
	plt.legend(handles, labels, loc='center')
	fig.suptitle("Distribution of scores for each course between all four houses")
	fig.tight_layout()
	fig.subplots_adjust(top=0.93, hspace=0.2, wspace=0.15)#margin between subplots
    
	plt.show()



def main():
	display_histogram("data/dataset_train.csv")
	print("Which Hogwarts course has a homogeneous score distribution between all four houses?") 
	print("Care of magical creatures has a homogeneous score distribution between all four houses") 
	


if __name__ == "__main__":
    main()
