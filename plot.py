from ase.optimize.minimahopping import MHPlot

mhplot = MHPlot()
fig = mhplot.get_figure()
fig.axes[2].set_ylim(6.4, 7.8)
fig.savefig('summary2.png')
mhplot.save_figure('summary.png')