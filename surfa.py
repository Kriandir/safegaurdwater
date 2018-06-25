import numpy as np
import matplotlib.pyplot as plt
from matplotlib import container

hr = [4,0.0023]
min10 = [34,0.011]
min1 = [378,0.018]
sec10 = [554,0.025]
timelist = [hr,min10,min1,sec10]
def Calcsurface(images):
    return (-1*np.log(0.05))/(78*(images-1))
def Calcsens(rms):
    return 8*rms*np.exp((5**2)/(2*3.96**2))




surfacelist = []
for i in timelist:

    if i == hr:
        surfacelist.append([Calcsurface(i[0]),60*60,"1 hour","less"])
        surfacelist[-1].append(Calcsens(i[1]))
    if i == min10:
        surfacelist.append([Calcsurface(i[0]),60*10,"10 minutes","less"])
        surfacelist[-1].append(Calcsens(i[1]))
    if i == min1:
        surfacelist.append([Calcsurface(i[0]),60,"1 minute","less"])
        surfacelist[-1].append(Calcsens(i[1]))
    if i == sec10:
        surfacelist.append([Calcsurface(i[0]),10,"10 seconds","less"])
        surfacelist[-1].append(Calcsens(i[1]))
surfacelist = np.array(surfacelist)


previoussurface = [[4.1e-7,30,r'Stewart et al. (2016)','less',36.1],[1.4e-5,60*4,r'Stewart et al. (2016)','ex',7.9],\
[1.9e-11,5,r'Obenberger et al. (2015)','less',1440],[7.5e-5,60*3,r'Bell et al. (2014)','less',5.5],\
[1e-4,60*59,r'Carbone et al. (2014)','less',.5],[2.2e-2,60*40,r'Cendes et al. (2014)','less',.5],\
[1.2e-1,60*60*24,r'Jaeger et al. (2012)','ex',.0021],[1.3e-2,60*60*24,r'Bannister et al. (2011)','ex',.014],\
[9.5e-8,300,r'Lazio et al. (2010)','less',2500],[3.4e-2,60*60*24,r'Hyman et al. (2009)','ex',.03]]
# for i in range(1):
#     previoussurface.append([4.1e-7,30,'stew','less',36.1])
#     previoussurface.append([1.4e-5,60*4,'stew','ex',7.9])
#     previoussurface.append([1.9e-11,5,'oben','less',1440])
#     previoussurface.append([7.5e-5,60*3,'bell','less',5.5])
#     previoussurface.append([1e-4,60*59,'carb','less',.5])
#     previoussurface.append([2,2e-2,60*40,'cend','less',.5])
#     previoussurface.append([1,2e-1,60*60*24,'jaeg','ex',.0021])
#     previoussurface.append([1,3e-2,60*60*24,'bann','ex',.014])
#     previoussurface.append([9.5e-8,300,'lazio','less',2500])
#     previoussurface.append([3.4e-2,60*60*24,'hymen','ex',.03])
print np.array(previoussurface)
previoussurface = np.array(previoussurface)
### DAYZ ####
# colors = plt.cm.hsv(np.linspace(0.,1.,10))
# symbols = ["o","v","^","<",">","+","s","p","*","D"]
#
# fig,ax = plt.subplots(figsize=(10,10))
# # ax.errorbar(previoussurface[0][4],previoussurface[0][0],lolims=lolims,linestyle=ls)
# xaxis = np.logspace(-5,4,8)
# fontax = 20
# ax.set_xticks(xaxis)
# ax.set_xlim(1e-5,1e1)
# ax.set_xscale('log')
# ax.set_yscale('log')
# ax.get_xaxis().get_major_formatter().labelOnlyBase = False
# # ax.set_yticks(xaxis)
# # ax.set_xscale('log')
# # ax.set_yscale('log')
# plt.minorticks_off()
# ax.tick_params(axis='x', pad=5)
# ax.set_xlabel(r"Timescale (Days)",fontsize = fontax)
# ax.set_ylabel(r"Surface Density (deg$^{-2}$)",fontsize = fontax)
# ax.axvline(1,linestyle='--', alpha = 0.3)
# ax.text(1,1e-11,r"1 Day",rotation=90, fontsize = fontax/1.2,verticalalignment='center')
# ax.axvline(1./24,linestyle='--', alpha = 0.3)
# ax.text(1./24,1e-11,r"1 Hour",rotation=90, fontsize = fontax/1.2,verticalalignment='center')
# ax.axvline(1./(24*60),linestyle='--', alpha = 0.3)
# ax.text(1./(24*60),1e-11,r"1 Minute",rotation=90, fontsize = fontax/1.2,verticalalignment='center')
# ax.axvline(1./(24*60*60),linestyle='--',alpha =0.3)
# ax.text(1./(24*60*60),1e-11,r"1 Second",rotation=90, fontsize = fontax/1.2,verticalalignment='center')
# box = ax.get_position()
# ax.set_position([box.x0, box.y0 + box.height * 0.1,
#                  box.width, box.height * 0.9])
#
# print xaxis
# ctr =0
# for i in previoussurface:
#     if i[3] == "less":
#
#         ax.errorbar(float(i[1])/(60.*60*24), float(i[0]), yerr=0.5*float(i[0]),
#                             uplims=True,
#                             marker=symbols[ctr],
#                             color = colors[ctr],
#                             markeredgecolor="black",ecolor='black',
#                             linewidth=3.0, linestyle="None", alpha=1,label=i[2],ms = 10)
#         if i[2] ==r'Stewart et al. (2016)':
#             continue
#         else:
#             ctr +=1
#
#     else:
#
#         ax.scatter(float(i[1])/(60.*60*24), float(i[0]),color = colors[ctr],marker=symbols[ctr],edgecolors='black',alpha =1,s=70,label=i[2])
#         ctr +=1
#
# for i in surfacelist:
#     ax.errorbar(float(i[1])/(60.*60*24), float(i[0]), yerr=0.5*float(i[0]),
#                         uplims=True,
#                         marker="o",
#                         color = "yellow",
#                         markeredgecolor="black",
#                         linewidth=2.0, linestyle="None",ecolor='black', alpha=1,ms=10,label="Own Work")
#
#
# handles, labels = ax.get_legend_handles_labels()
# handles = [h[0] if isinstance(h, container.ErrorbarContainer) else h for h in handles]
#
# ax.legend(handles,labels,loc='upper center', bbox_to_anchor=(0.5, -0.1),
#           fancybox=True, shadow=True, ncol=5,numpoints=1,scatterpoints=1)
# # plt.legend(numpoints=1,scatterpoints=1, loc=8)
# plt.show()
### SENSITIVITY ####
colors = plt.cm.hsv(np.linspace(0.,1.,10))
symbols = ["o","v","^","<",">","+","s","p","*","D"]

fig,ax = plt.subplots(figsize=(10,10))
# ax.errorbar(previoussurface[0][4],previoussurface[0][0],lolims=lolims,linestyle=ls)
xaxis = np.logspace(-5,4,8)
fontax = 20
ax.set_xticks(xaxis)
ax.set_xlim(1e-3,1e4)
ax.set_xscale('log')
ax.set_yscale('log')
ax.get_xaxis().get_major_formatter().labelOnlyBase = False
# ax.set_yticks(xaxis)
# ax.set_xscale('log')
# ax.set_yscale('log')
plt.minorticks_off()
ax.tick_params(axis='x', pad=5)
ax.set_xlabel(r"Sensitivity (Jy)",fontsize = fontax)
ax.set_ylabel(r"Surface Density (deg$^{-2}$)",fontsize = fontax)

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

print xaxis
ctr =0
for i in previoussurface:
    if i[3] == "less":

        ax.errorbar(float(i[4]), float(i[0]), yerr=0.5*float(i[0]),
                            uplims=True,
                            marker=symbols[ctr],
                            color = colors[ctr],
                            markeredgecolor="black",ecolor='black',
                            linewidth=3.0, linestyle="None", alpha=1,ms = 10)
        if i[2] ==r'Stewart et al. (2016)':
            continue
        else:
            ctr +=1

    else:

        ax.scatter(float(i[4]), float(i[0]),color = colors[ctr],marker=symbols[ctr],edgecolors='black',alpha =1,s=70)
        ctr +=1

for i in surfacelist:
    ax.errorbar(float(i[4]), float(i[0]), yerr=0.5*float(i[0]),
                        uplims=True,
                        marker="o",
                        color = "yellow",
                        markeredgecolor="black",
                        linewidth=2.0, linestyle="None",ecolor='black', alpha=1,ms=10,label="Own Work")

handles, labels = ax.get_legend_handles_labels()
handles = [h[0] if isinstance(h, container.ErrorbarContainer) else h for h in handles]

ax.legend(handles,labels,loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=5,numpoints=1,scatterpoints=1)
# plt.legend(numpoints=1,scatterpoints=1, loc=8)
plt.show()
