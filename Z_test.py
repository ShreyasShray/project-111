import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("medium_data.csv")
reading_time = df["reading_time"].tolist()

population_mean = statistics.mean(reading_time)

def random_set_of_mean(counter):
    data_set = []
    for i in range(counter):
        random_index = random.randint(0, len(reading_time) - 1)
        value = reading_time[random_index]
        data_set.append(value)
    mean_of_the_data_set = statistics.mean(data_set)
    return mean_of_the_data_set

sampling_mean_list = []

for i in range(100):
    sampling_mean = random_set_of_mean(30)
    sampling_mean_list.append(sampling_mean)

samplingMean = statistics.mean(sampling_mean_list)
sampling_standard_deviation = statistics.stdev(sampling_mean_list)

z_score = (samplingMean - samplingMean)/sampling_standard_deviation

print("Mean of the sampling distribution is:- {}".format(samplingMean))
print("Standard Deviation of the sampling distribution is:- {}".format(sampling_standard_deviation))
print("Mean of sample 1:- {}".format(samplingMean))
print("The z score is:- {}".format(z_score))
print("there is no intervation")

first_standard_deviation_start, first_standard_deviation_end = samplingMean - sampling_standard_deviation, samplingMean + sampling_standard_deviation
second_standard_deviation_start, second_standard_deviation_end = samplingMean - (2*sampling_standard_deviation), samplingMean + (2*sampling_standard_deviation)
third_standard_deviation_start, third_standard_deviation_end = samplingMean - (3*sampling_standard_deviation), samplingMean + (3*sampling_standard_deviation)

fig = ff.create_distplot([sampling_mean_list], ["Mean"], show_hist = False)
fig.add_trace(go.Scatter(x = [samplingMean, samplingMean], y = [0, 0.9], mode = "lines", name="Sampling Mean"))
fig.add_trace(go.Scatter(x = [first_standard_deviation_start, first_standard_deviation_start], y = [0, 0.8], mode = "lines", name = "Standard Deviation 1"))
fig.add_trace(go.Scatter(x = [first_standard_deviation_end, first_standard_deviation_end], y = [0, 0.8], mode = "lines", name = "Standard Deviation 1"))
fig.add_trace(go.Scatter(x = [second_standard_deviation_start, second_standard_deviation_start], y = [0, 0.8], mode = "lines", name = "Standard Deviation 2"))
fig.add_trace(go.Scatter(x = [second_standard_deviation_end, second_standard_deviation_end], y = [0, 0.8], mode = "lines", name = "Standard Deviation 2"))
fig.add_trace(go.Scatter(x = [third_standard_deviation_start, third_standard_deviation_start], y = [0, 0.8], mode = "lines", name = "Standard Deviation 3"))
fig.add_trace(go.Scatter(x = [third_standard_deviation_end, third_standard_deviation_end], y = [0, 0.8], mode = "lines", name = "Standard Deviation 3"))
fig.add_trace(go.Scatter(x = [samplingMean, samplingMean], y = [0, 0.8], mode = "lines", name = "sample1"))
fig.show()