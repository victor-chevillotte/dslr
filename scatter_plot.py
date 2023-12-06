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


def display_scatter_plot(path):
    df = read_csv(path)
    fig, axs = plt.subplots(len(courses), len(courses), figsize=(15, 8))
    # What are the two features that are similar ?
    for i, course_x in enumerate(courses):
        for j, course_y in enumerate(courses):
            axs[i][j].scatter(df[course_x], df[course_y], alpha=0.5, label=course_x)
            axs[i][j].tick_params(
                left=False,
                right=False,
                labelleft=False,
                labelbottom=False,
                bottom=False,
            )

            # Set column titles
            if i == 0:
                # Alternate placement for readability
                if not j % 2 == 0:
                    axs[i][j].set_title(course_y, fontsize=8)

            # Set line titles
            if j == 0:
                # Alternate placement for readability
                if i % 2 == 0:
                    axs[i][j].set_ylabel(course_x, rotation=90, fontsize=8)

    plt.show()


def main():
    display_scatter_plot("data/dataset_train.csv")
    print("What are the two features that are similar ?")
    print(
        "Defense Against the Dark Arts and Astronomy are the two features that are similar"
    )


if __name__ == "__main__":
    main()
