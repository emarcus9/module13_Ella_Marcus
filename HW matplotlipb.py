# By: Ella Marcus
# 12/29/2025
# Import libraries
import random
import matplotlib.pyplot as plt

def read_first():
    """
    Read in file and add items to multiple lists.

    Read in weather_data_flatbush.csv.
    Create four lists for each section of items on the doc.
    Use for loop to go through each line and append month, high temp, low temp, and precipitation to lists.
    Use try and except to catch errors when opening the file.
    :return:
        month (list): stores months from doc
        avg_high (list): stores average high temps from doc
        avg_low (list): stores average low temps from doc
        precipitation (list): stores precipitation levels from doc
    """
    # Store all data in lists
    month = []
    avg_high = []
    avg_low = []
    precipitation = []
    try:
        with open("weather_data_flatbush.csv", "r") as f:
            # Skip header
            f.readline()
            for line in f:
                # Strip whitespace and newline characters, split by commas
                new = line.strip().split(",")
                # Append to lists based on indexes, convert to ints and floats
                month.append(new[0])
                avg_high.append(int(new[1]))
                avg_low.append(int(new[2]))
                precipitation.append(float(new[3]))
            return month, avg_high, avg_low, precipitation
    except FileNotFoundError as e:
        print(f"File not found: e")


def first_graph(month, avg_high, avg_low):
    """
    Plots average temperatures by month on line graph.

    Creates tuple of colors to pick graph colors from.
    Create line graph of two lines using random colors.
    Label the graph and what it represents.
    Calculate the highest temp and the lowest temp, and corresponding months.
    Calculate average of the two values.
    Print results.
    :param:
        month(list): stores months from doc:
        avg_high (list): stores average high temps from doc
        avg_low (list): stores average low temps from doc
    """
    # Store all possible colors in a tuple
    colors1 = ("#ffd6ff", "#e7c6ff", "#c8b6ff", "#b8c0ff", "#bbd0ff")

    # Title
    plt.title("Average Weather in Flatbush")
    # Plot two lines, color choices taken from color tuple at random
    plt.plot(month, avg_high, color = random.choice(colors1), label = "Average High", marker = "o")
    plt.plot(month, avg_low, color = random.choice(colors1), label = "Average Low", marker = "o")
    # Labels for axis
    plt.xlabel('Month')
    plt.ylabel('Temperature')
    # Custom tick labels for the months
    plt.xticks(ticks = range(len(month)), label = month)
    # Grid
    plt.grid(True)
    plt.legend()
    plt.show()

    # Calculate largest and lowest averages
    largest_avg = max(avg_high)
    lowest_avg = min(avg_low)
    # Find index of largest and lowest avg and use that index to find the month
    highest_month = month[avg_high.index(largest_avg)]
    lowest_month = month[avg_low.index(lowest_avg)]
    total = largest_avg + lowest_avg
    average = total / 2
    print(f"The month with the highest value shown in the first graph: {highest_month}")
    print(f"The month with the lowest value shown in the first graph: {lowest_month}")
    print(f"The average of the highest value and lowest value: {average}")
    print()
    """
    Reflection:
    The graph showed me the average weather in flatbush by plotting two lines- one for the average high weather and
    one for the average low weather. I noticed that both lines had similar slopes in the same months- meaning they
    basically running parallel to each other the whole time. If one line had a lower slope, the other one did as well.
    They were imitating each other just at different levels- the high temperature was higher than the low temperature.
    This surprised me because I had originally thought that their lines would look different, and would have different
    slopes and different times. I did not at all think that the lines would be so similar. I also was surprised to see
    that August was the hottest month because I always assumed that July is the hottest month of the year.
    """


def read_second():
    """
    Read in file and add items to multiple lists.

    Read in flatbush_extremes.csv.
    Create four lists for each section of items on the doc.
    Use for loop to go through each line and append month, high temp, low temp, and avg snow to lists.
    Use try and except to catch errors when opening the file.
    :return:
        month (list): stores months from doc
        record_high (list): stores record high temps from doc
        record_low (list): stores record low temps from doc
        avg_snow (list): stores average snow levels from doc
    :return:
    """
    # Store all data in lists
    month = []
    record_high = []
    record_low = []
    avg_snow = []
    try:
        with open("flatbush_extremes.csv", "r") as f:
            # Skip header
            f.readline()
            for line in f:
                # Strip whitespace and newline characters, split by commas
                new = line.strip().split(",")
                # Append to lists based on indexes, convert to ints and floats
                month.append(new[0])
                record_high.append(int(new[1]))
                record_low.append(int(new[2]))
                avg_snow.append(float(new[3]))
            return month, record_high, record_low, avg_snow
    except FileNotFoundError as e:
        print(f"File not found: e")


def second_graph(month, record_high, record_low):
    """
    Plots record temperatures by month on line graph.

    Creates tuple of colors to pick graph colors from.
    Create line graph of two lines using random colors.
    Label the graph and what it represents.
    Calculate the highest record temp and the lowest record temp, and corresponding months.
    Calculate average of the two values.
    Print results.
    :param:
        month(list): stores months from doc:
        record_high (list): stores record high temps from doc
        record_low (list): stores record low temps from doc
    """
    # Store all possible colors in a tuple
    colors2 = ("#ffccd5", "#800f2f", "#ff4d6d", "#ff8fa3", "#bf5266", "#590e1c")

    # Title
    plt.title("Record Highs and Lows")
    # Plot two lines, color choices taken from color tuple at random
    plt.plot(month, record_high, color=random.choice(colors2), label="Record High", marker = "o")
    plt.plot(month, record_low, color=random.choice(colors2), label="Record Low", marker = "o")
    # Labels for axis
    plt.xlabel('Month')
    plt.ylabel('Temperature')
    # Custom tick labels for the months
    plt.xticks(ticks=range(len(month)), label=month)
    # Grid
    plt.grid(True)
    plt.legend()
    plt.show()

    # Calculate largest and lowest temperatures
    largest_high = max(record_high)
    lowest_low = min(record_low)
    # Find index of largest and lowest temperature and use that index to find the month
    highest_month = month[record_high.index(largest_high)]
    lowest_month = month[record_low.index(lowest_low)]
    total = largest_high + lowest_low
    average = total / 2
    print(f"The month with the highest value shown in the second graph: {highest_month}")
    print(f"The month with the lowest value shown in the second graph: {lowest_month}")
    print(f"The average of the highest value and lowest value: {average}")
    print()
    """
    Reflection:
    The graph showed me the record high temperatures per month and the record low temperatures per month in Flatbush.
    Two lined were plotted, one for the record high temperatures and one for the record low temperatures. I noticed
    that this graph has a different trend than the first. While in the first graph both lines have the same shape, in
    this graph they have slightly different shapes. For example, there is only a small difference in the record high
    temperatures of April and May while there is a very big difference in the record low temperatures of those same
    months. The slope of the two lines are very different in these two places. This surprised me because I had assumed
    that this graph would act in a similar way to the first one and both lines would have similar slopes. It also
    surprised me to see just how high and low the record temperatures were. I never knew that it ever got that hot
    and cold in Flatbush!
    """


def third_graph(month, avg_snow):
    """
    Plots average temperatures by month on bar graph.

    Creates tuple of colors to pick graph colors from.
    Create bar graph of snow fall for each month using random colors.
    Label the graph and what it represents.
    Calculate the highest snowfall and the lowest snowfall, and corresponding months.
    Calculate average of the two values.
    Print results.
    :param:
        month(list): stores months from doc:
        avg_snow (list): stores average snow levels from doc
    """
    # Store all possible colors in a tuple
    colors3 = ("#00ffc8", "#00d3e0", "#00a8f7", "#aaff01", "#004cff")
    # Use list comprehension to create new list with random colors in it picked from tuple
    bar_colors = [random.choice(colors3) for i in month]
    # Bar Chart
    plt.title("Average Snowfall")
    plt.bar(month, avg_snow, color=bar_colors, label="Average Snowfall")
    # Axis labels
    plt.xlabel('Month')
    plt.ylabel('Snowfall(inches)')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Calculate largest and lowest snowfall
    largest_snow = max(avg_snow)
    lowest_snow = min(avg_snow)
    # Find index of largest and lowest avg and use that index to find the month
    highest_month = month[avg_snow.index(largest_snow)]
    lowest_month = month[avg_snow.index(lowest_snow)]
    total = largest_snow + lowest_snow
    average = total / 2
    print(f"The month with the highest value shown in the third graph: {highest_month}")
    print(f"The month with the lowest value shown in the third graph: {lowest_month}")
    print(f"The average of the highest value and lowest value: {average}")
    print()
    """
    Reflection:
    This graph showed me the average snowfall that fell in inches in each month in Flatbush for the whole year.
    It shows this through a bar chart by plotting each month on its own bar. 
    There is a trend in the graph that shows that snow most commonly falls at the beginning of the year and at 
    the end of the year. This makes sense because these are the times when it is the most cold. I found it
    surprising that the graph also showed that it has even snowed in March and April. I never knew that it ever
    snows that late in the year. I also found it surprising that not only did it snow then, but in March it snowed
    around 3 inches! This is quite a lot for so late in the year. I guess Flatbush is a very cold place!
    """


def fourth_graph(month, record_high, record_low):
    """
    Plots difference of record temperatures by month on line graph.

    Creates tuple of colors to pick graph colors from.
    Create line graph to plot one line of the differences of temperatures using random colors.
    Label the graph and what it represents.
    Calculate the highest record temp difference and the lowest record temp difference, and corresponding months.
    Calculate average of the two values.
    Print results.
    :param:
        month(list): stores months from doc:
        record_high (list): stores record high temps from doc
        record_low (list): stores record low temps from doc
    """
    # Use list comprehension to create new list with the differences of the highest and lowest of each month
    ranges = [record_high[i] - record_low[i] for i, e in enumerate(record_high)]
    # Store colors in a tuple
    colors3 = ("#aaff01", "#ff8f01", "#ff00aa", "#aa00ff")

    # Title
    plt.title("Largest Temperature Range")
    # Plot two lines, color choices taken from color tuple at random
    plt.plot(month, ranges, color=random.choice(colors3), label="Temperature Range", marker = "o")
    # Labels for axis
    plt.xlabel('Month')
    plt.ylabel('Range')
    # Custom tick labels for the months
    plt.xticks(ticks=range(len(month)), label=month)
    # Grid
    plt.grid(True)
    plt.legend()
    plt.show()

    # Calculate largest and lowest range
    largest_range = max(ranges)
    lowest_range = min(ranges)
    # Find index of largest and lowest and use that index to find the month
    highest_month = month[ranges.index(largest_range)]
    lowest_month = month[ranges.index(lowest_range)]
    total = sum(ranges)
    average = total / len(ranges)
    print(f"The month with the highest value shown in the fourth graph: {highest_month}")
    print(f"The month with the lowest value shown in the fourth graph: {lowest_month}")
    print(f"The average of all of the ranges: {average}")
    print()
    """
    Reflection:
    This graph calculated the month that has the biggest difference between the record high and record low
    temperature. It plots one line of all the differences. This line does not at all have a line with a consistent
    slope but instead the line is sort of sporadic- going up in certain places and then down at other times.
    I was not expecting this at all because I was expecting more of a consistent line like the other graphs.
    What also surprised me is the vast difference between two month that are right next to each other- for example,
    the difference of April temperatures and the difference of May temperatures are very different, even though
    May comes right after April. The plot shows that the spring and fall months have the biggest difference and this
    makes sense because these months are the in between months between the summer and winter. The summer is always
    hot while the winter is always cold so it makes sense that the months in between have the biggest difference in
    their temperatures.
    """


def main():
    """
    Call each function to have them run and print to screen.
    Unpack every tuple from each function and pass them into those that require it.
    """
    # Unpack each function and pass in parameters
    # Call every function
    month, avg_high, avg_low, precipitation = read_first()
    first_graph(month, avg_high, avg_low)
    month, record_high, record_low, avg_snow = read_second()
    second_graph(month, record_high, record_low)
    third_graph(month, avg_snow)
    fourth_graph(month, record_high, record_low)


if __name__ == '__main__':
    main()



