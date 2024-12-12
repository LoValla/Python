f = open(
    "my_file_name.txt", "w"
)  # r = read, w = write, a = append lines at the end, x = create new
f.write("Write this line of text. And this second sentence. And the third one. \nThis line has only one sentence.")
f.close()

f = open(
    "my_file_name.txt", "r"
)  # r = read, w = write, a = append lines at the end, x = create new
for line in f:  # can loop over the lines
    line = line.replace("e", "E")
    print("This line: {}".format(line))
    sentences = line.strip().split(
        "."
    )  # use strip to remove initial and final blank spaces/newlines, split to separate words
    print("This line has {} sentences.".format(len(sentences)))
f.close()

# create csv file
f = open("data.csv", "w")
f.write(
    """index,date,height,heightMax,period,energy,direction,temperature
1,01/01/2017 00:00,-99.9,-99.9,-99.9,-99.9,-99.9,-99.9
2,01/01/2017 00:30,0.875,1.39,4.421,4.506,-99.9,-99.9
3,01/01/2017 01:00,0.763,1.15,4.52,5.513,49,25.65
4,01/01/2017 01:30,0.77,1.41,4.582,5.647,75,25.5
5,01/01/2017 02:00,0.747,1.16,4.515,5.083,91,25.45
6,01/01/2017 02:30,0.718,1.61,4.614,6.181,68,25.45
7,01/01/2017 03:00,0.707,1.34,4.568,4.705,73,25.5
8,01/01/2017 03:30,0.729,1.21,4.786,4.484,63,25.5
9,01/01/2017 04:00,0.733,1.2,4.897,5.042,68,25.5"""
)
f.close()

# read csv file
f = open("data.csv", "r")

# Get the first line to extract the features names.
features = (
    f.readline().strip().split(",")
)  # readline reads the first line (in this case, read attributes' names)
print(features)

# Loop over lines and store the information
data = []
for l in f:  # since I used readline() above, l starts from the data row number 1 (not 0)
    values = l.strip().split(",")
    print(values)
    data_single_line = {var: val for var, val in zip(features, values)}
    data.append(data_single_line)

# heights = [w["height"] for w in data]  # (data is a list of dictionaries, hence w is a dictionary)
# average = sum(heights) / len(heights)  # problem: the data is in string format


def str_to_time(date_str):
    import datetime

    return datetime.datetime.strptime(date_str, "%d/%m/%Y %H:%M")


# Container with properly converted data
DATA = []
# Loop over waves and make the proper conversion depending on the feature name
for w in data:
    wgood = w.copy()
    for k in w:
        if (
            k == "index"
        ):  # Cast string into an integer (note that the == for the dictionaries compares the key, not the value)
            wgood[k] = int(w[k])
        elif k == "date":  # cast string into a datetime object
            wgood[k] = str_to_time(w[k])
        else:  # cast string into a float
            wgood[k] = float(w[k])
    DATA.append(wgood)

heights = [
    w["height"] for w in DATA[1:]
]  # (data is a list of dictionaries, hence w is a dictionary)

average = sum(heights) / len(heights)
print("Averaged waveheight is {:.1f} m".format(average))
print(f"Averaged waveheight is {average:.1f} m")  #:.1f means rounded to 1 decimal digit

height = [w["height"] for w in DATA if w["height"] > -99]
energy = [w["energy"] for w in DATA if w["energy"] > -99]

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")

my_plot = plt.plot(
    height, energy, linewidth=0, marker="o", label="Data"
)  # only dots (line width = 0)
# set x and y axes labels
plt.xlabel("Wave Height")
plt.ylabel("Wave Energy")

# Adding a legend based on label keyword
plt.legend()
plt.savefig("aaa.png") #use this before showing the plot
plt.show()  # use this at the end