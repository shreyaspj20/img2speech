import pickle
import matplotlib.pyplot as plt
import numpy as np
import statistics

with open("E:\my gitprojects\img2speech\img2speech\src\similarity_yes_list.pkl", "rb") as f:
    similarity_yes_list = pickle.load(f)

with open("E:\my gitprojects\img2speech\img2speech\src\similarity_no_list.pkl", "rb") as f:
    similarity_no_list = pickle.load(f)

with open("E:\my gitprojects\img2speech\img2speech\src\wer_yes_list.pkl", "rb") as f:
    wer_yes_list = pickle.load(f)

with open("E:\my gitprojects\img2speech\img2speech\src\wer_no_list.pkl", "rb") as f:
    wer_no_list = pickle.load(f)

with open("E:\my gitprojects\img2speech\img2speech\src\cer_yes_list.pkl", "rb") as f:
    cer_yes_list = pickle.load(f)

with open("E:\my gitprojects\img2speech\img2speech\src\cer_no_list.pkl", "rb") as f:
    cer_no_list = pickle.load(f)

with open("E:\my gitprojects\img2speech\img2speech\src\leven_yes_list.pkl", "rb") as f:
    leven_yes_list = pickle.load(f)

with open("E:\my gitprojects\img2speech\img2speech\src\leven_no_list.pkl", "rb") as f:
    leven_no_list = pickle.load(f)



mean = statistics.mean(leven_yes_list)
print("Mean:", mean)

# Compute the median of the data
median = statistics.median(leven_yes_list)
print("Median:", median)

# Compute the mode of the data
mode = statistics.mode(leven_yes_list)
print("Mode:", mode)

# Compute the variance of the data
variance = statistics.variance(leven_yes_list)
print("Variance:", variance)

# Compute the standard deviation of the data
stdev = statistics.stdev(leven_yes_list)
print("Standard Deviation:", stdev)

# Compute the range of the data
range = max(leven_yes_list) - min(leven_yes_list)
print("Range:", range)

# Compute the quartiles of the data
q1, q2, q3 = statistics.quantiles(leven_yes_list)
print("Q1:", q1)
print("Q2 (Median):", q2)
print("Q3:", q3)

"""
fig, ax = plt.subplots()
ax.set_ylim(0.5, 1)
ax.set_yticks([i/10 for i in range(5, 11)])

ax.plot(similarity_yes_list, label='WITH PREPROCESSING')
ax.plot(similarity_no_list, label='WITHOUT PREPROCESSING')

plt.title('Line Graph of two pipelines')
plt.xlabel('Image number')
plt.ylabel('Similarity index')
plt.legend()
plt.show()

plt.plot(wer_yes_list, label='WITH PREPROCESSING')
plt.plot(wer_no_list, label='WITHOUT PREPROCESSING')

plt.title('Line Graph of two pipelines')
plt.xlabel('Image number')
plt.ylabel('Word error rate')
plt.legend()
plt.show()

plt.plot(cer_yes_list, label='WITH PREPROCESSING')
plt.plot(cer_no_list, label='WITHOUT PREPROCESSING')

plt.title('Line Graph of two pipelines')
plt.xlabel('Image number')
plt.ylabel('Character error rate')
plt.legend()
plt.show()

plt.plot(leven_yes_list, label='WITH PREPROCESSING')
plt.plot(leven_no_list, label='WITHOUT PREPROCESSING')

plt.title('Line Graph of two pipelines')
plt.xlabel('Image number')
plt.ylabel('Levenshtein Distance')
plt.legend()
plt.show()


ind = np.arange(len(similarity_yes_list))
width = 0.25
fig, ax = plt.subplots()
rects1 = ax.bar(ind - width / 2, similarity_yes_list, width, label='With preprocessing')
rects2 = ax.bar(ind + width / 2, similarity_no_list, width, label='Without preprocessing')
ax.set_ylabel('Similarity Index')
ax.set_title('Comparison of two pipelines')
ax.set_xticks(ind)
ax.set_xticklabels([i for i in range(1, 31)])
ax.set_xlabel('Image number')
ax.legend()
plt.show()


ind = np.arange(len(wer_yes_list))
width = 0.25
fig, ax = plt.subplots()
rects1 = ax.bar(ind - width / 2, wer_yes_list, width, label='With preprocessing')
rects2 = ax.bar(ind + width / 2, wer_no_list, width, label='Without preprocessing')
ax.set_ylabel('Word Error Rate')
ax.set_title('Comparison of two pipelines')
ax.set_xticks(ind)
ax.set_xticklabels([i for i in range(1, 31)])
ax.set_xlabel('Image number')
ax.legend()
plt.show()


ind = np.arange(len(cer_yes_list))
width = 0.25
fig, ax = plt.subplots()
rects1 = ax.bar(ind - width / 2, cer_yes_list, width, label='With preprocessing')
rects2 = ax.bar(ind + width / 2, cer_no_list, width, label='Without preprocessing')
ax.set_ylabel('Character Error Rate')
ax.set_title('Comparison of two pipelines')
ax.set_xticks(ind)
ax.set_xticklabels([i for i in range(1, 31)])
ax.set_xlabel('Image number')
ax.legend()
plt.show()


ind = np.arange(len(leven_yes_list))
width = 0.25
fig, ax = plt.subplots()
rects1 = ax.bar(ind - width / 2, leven_yes_list, width, label='With preprocessing')
rects2 = ax.bar(ind + width / 2, leven_no_list, width, label='Without preprocessing')
ax.set_ylabel('Levenshtein distance')
ax.set_title('Comparison of two pipelines')
ax.set_xticks(ind)
ax.set_xticklabels([i for i in range(1, 31)])
ax.set_xlabel('Image number')
ax.legend()
plt.show()


data = [similarity_yes_list, similarity_no_list]
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 6))
ax1.set_ylabel('Similarity Index')
ax1.set_title('Violin Plot')
ax2.set_title('Box Plot')
ax1.violinplot(data)
ax2.boxplot(data)
plt.setp((ax1, ax2), xticks=[1, 2], xticklabels=['With preprocessing', 'Without preprocessing'])
plt.show()

data = [wer_yes_list, wer_no_list]
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 6))
ax1.set_ylabel('Word Error Rate')
ax1.set_title('Violin Plot')
ax2.set_title('Box Plot')
ax1.violinplot(data)
ax2.boxplot(data)
plt.setp((ax1, ax2), xticks=[1, 2], xticklabels=['With preprocessing', 'Without preprocessing'])
plt.show()

data = [cer_yes_list, cer_no_list]
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 6))
ax1.set_ylabel('Character Error Rate')
ax1.set_title('Violin Plot')
ax2.set_title('Box Plot')
ax1.violinplot(data)
ax2.boxplot(data)
plt.setp((ax1, ax2), xticks=[1, 2], xticklabels=['With preprocessing', 'Without preprocessing'])
plt.show()

data = [leven_yes_list, leven_no_list]
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 6))
ax1.set_ylabel('Levenshtein Distance')
ax1.set_title('Violin Plot')
ax2.set_title('Box Plot')
ax1.violinplot(data)
ax2.boxplot(data)
plt.setp((ax1, ax2), xticks=[1, 2], xticklabels=['With preprocessing', 'Without preprocessing'])
plt.show()

"""



