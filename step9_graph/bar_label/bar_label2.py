import matplotlib.pyplot as plt
import numpy as np

species = ('1st_monday', '1st_tuesday', '1st_wednesday','1st_thursday', '1st_friday','1st_saturday', '1st_sunday','2nd_monday', '2nd_tuesday', '2nd_wednesday','2nd_thursday', '2nd_friday','2nd_saturday', '2nd_sunday')
sex_counts = {
    'Male': np.array([25, 34, 61, 73, 54, 78, 99, 24, 55, 90, 26, 77, 55, 88]),
    'Female': np.array([73, 54, 78, 99, 24, 55, 90, 54, 78, 99, 25, 34, 55, 88]),
}
width = 0.4  # the width of the bars: can also be len(x) sequence


fig, ax = plt.subplots()
bottom = np.zeros(14)

for sex, sex_count in sex_counts.items():
    p = ax.bar(species, sex_count, width, label=sex, bottom=bottom)
    bottom += sex_count

    ax.bar_label(p, label_type='center')

ax.set_title('Number of penguins by sex')
ax.legend()

plt.show()