import pandas as pd
import matplotlib.pyplot as plt
from utility import find_mean, find_std



def plot_course_distributions(courses_variability2):
    # The line `courses, variability = zip(*course_cols)` is unpacking the `course_cols` variable into
    # two separate lists - `courses` and `variability`.
    sorted_courses = sorted(courses_variability2.items(), key=lambda x: x[1])
    courses, variability = zip(*sorted_courses)

    num_courses = len(courses)
    width = max(8, num_courses * 0.8)   # at least 8 inches wide
    height = 6

    plt.figure(figsize = (width ,height))

    plt.bar(courses, variability, color="skyblue", edgecolor="black")

    # `plt.yscale("log")` is a function in Matplotlib that sets the scale of the y-axis to be
    # logarithmic. This means that the values on the y-axis will be spaced evenly on a logarithmic
    # scale rather than a linear scale.
    plt.yscale("log")

    # For Visibility when there are too many Parameters
    plt.xticks(rotation=45, ha="right")

    # Labeling the Plot
    plt.ylabel("STD of house STDs (lower = more homogeneous)")
    plt.title("Homogeneity of Hogwarts Courses Across Houses")

    # Highlight the most homogeneous course
    min_idx = variability.index(min(variability))
    plt.bar(courses[min_idx], variability[min_idx], color="orange")

    # Fix the padding Visibility 
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":

    df = pd.read_csv("dataset_train.csv")

    # Get the 4 unique houses
    houses = df["Hogwarts House"].unique()


    # Take only after the 6 column {hard coded for our data}
    course_cols = df.columns[6:]


    house_scores = {}  # empty dictionary

    for h in houses:  # loop over Gryffindor, Slytherin, ...

        # filter rows for this house
        house_data = df[df["Hogwarts House"] == h]

        # Store it like this
        house_scores[h] = {}
        
        for course in course_cols:
            # clean missing values and convert to NumPy array
            clean_value = house_data[course].dropna().values
            house_scores[h][course] = clean_value

    courses_variability = {}

    for course in course_cols:
        house_mean = []

        for h in houses:
            values = house_scores[h][course]
            if len(values) > 0:
                house_mean.append(find_std(values))
        
        if len(house_mean) == len(houses):
            variability = find_std(house_mean)
            # variability2 = np.std(house_mean)
            courses_variability[course] = variability

    print(courses_variability)
    plot_course_distributions(courses_variability)
