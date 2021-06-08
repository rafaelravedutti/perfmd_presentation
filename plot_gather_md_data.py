import matplotlib.pyplot as plt
import sys

vector_width = 8 # 8 doubles per zmm vector

filename = sys.argv[1]
output_file = filename.replace(".txt", ".pdf")
fig = plt.figure()
ax = plt.axes()
plot_data = {}

with open(filename, 'r') as fp:
    for line in fp.readlines():
        stride, N, size, total_time, time_per_it, cy_per_it, cy_per_gather, cy_per_elem  = line.split(',')
        stride = int(stride)
        size = float(size)
        cy_per_it = float(cy_per_it)

        #if stride < 5 and stride != 3:
        if stride < 100:
            if stride not in plot_data:
                plot_data[stride] = {}

            plot_data[stride][size] = cy_per_it if size not in plot_data[stride] \
                                      else min(cy_per_it, plot_data[stride][size])

for stride in plot_data:
    sizes = list(plot_data[stride].keys())
    sizes.sort()
    cycles = [plot_data[stride][size] for size in sizes]
    ax.plot(sizes, cycles, marker='.', label=str(stride))

ax.vlines([32, 1000], 0, 1, transform=ax.get_xaxis_transform(), linestyles='dashed', color=['#444444', '#777777'])
#ax.vlines([32, 1000, 28000], 0, 1, transform=ax.get_xaxis_transform(), linestyles='dashed', color=['#444444', '#777777', '#aaaaaa'])
ax.set(xlabel='Array size (kB)', ylabel='Cycles per gather')
ax.set_xscale('log')
#ax.set_xticks([32, 1000, 28000])
#ax.set_xlim(0, 200000)
#ax.set_ylim(25, 60)
plt.legend(title="Stride")
fig.savefig(output_file, bbox_inches = 'tight', pad_inches = 0)
