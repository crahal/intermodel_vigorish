import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
import os
from sklearn.preprocessing import StandardScaler
nrmlzd = StandardScaler()


def plot_hrs_imv(fig_path, data_path, style_dict, fig_name):
    mpl.rcParams['font.family'] = style_dict['font']
    csfont = {'fontname': style_dict['font']}
    letter_fontsize = 24
    label_fontsize = 15
    data_dir = os.path.join(data_path, 'HRS')
    out1a = pd.read_csv(os.path.join(data_dir, 'out1a.csv'), index_col=False)
    out1b = pd.read_csv(os.path.join(data_dir, 'out1b.csv'), index_col=False)
    out1c = pd.read_csv(os.path.join(data_dir, 'out1c.csv'), index_col=False)
    out2c = pd.read_csv(os.path.join(data_dir, 'out2c.csv'), index_col=False)

    fig = plt.figure(figsize=(14.4, 13))
    ax1 = plt.subplot2grid((2, 2), (0, 0), rowspan=1, colspan=1)
    ax2 = plt.subplot2grid((2, 2), (0, 1), rowspan=1, colspan=1)
    ax3 = plt.subplot2grid((2, 2), (1, 0), rowspan=1, colspan=1)
    ax4 = plt.subplot2grid((2, 2), (1, 1), rowspan=1, colspan=1)
    colors_long = ['#a6cee3',
                   '#1f78b4',
                   '#b2df8a',
                   '#33a02c',
                   '#fb9a99',
                   '#e31a1c',
                   '#fdbf6f',
                   '#ff7f00',
                   '#cab2d6',
                   '#6a3d9a']
    out1a['V1'] = out1a['V1'].str.title()
    out1a['V1'] = out1a['V1'].replace('Hibp', 'HiBP')
    out1b['V1'] = out1b['V1'].str.title()
    out1b['V1'] = out1b['V1'].replace('Hibp', 'HiBP')
    out1c['V1'] = out1c['V1'].str.title()
    out1c['V1'] = out1c['V1'].replace('Hibp', 'HiBP')
    out2c['V1'] = out2c['V1'].str.title()
    out2c['V1'] = out2c['V1'].replace('Hibp', 'HiBP')
    iterator = 0
    for col in out1a['V1'].unique():
        out1a[out1a['V1'] == col].set_index('V2')['V4'].plot(ax=ax1,
                                                             color=colors_long[iterator],
                                                             linewidth=style_dict['line_width'],
                                                             alpha=0.9,
                                                             label=col)
        out1b[out1b['V1'] == col].set_index('V2')['V4'].plot(ax=ax2,
                                                             color=colors_long[iterator],
                                                             linewidth=style_dict['line_width'],
                                                             alpha=0.9,
                                                             label=col)
        out1c[out1c['V1'] == col].set_index('V2')['V4'].plot(ax=ax3,
                                                             color=colors_long[iterator],
                                                             linewidth=style_dict['line_width'],
                                                             alpha=0.9,
                                                             label=col)
        out2c[out2c['V1'] == col].set_index('V2')['V4'].plot(ax=ax4,
                                                             color=colors_long[iterator],
                                                             linewidth=style_dict['line_width'],
                                                             alpha=0.9,
                                                             label=col)
        iterator = iterator + 1
    ax1.set_title(r'A.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)
    ax2.set_title(r'B.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)
    ax3.set_title(r'C.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)
    ax4.set_title(r'D.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025);
    ax1.set_xlabel('', csfont, fontsize=label_fontsize);
    ax2.set_xlabel('', csfont, fontsize=label_fontsize);
    ax3.set_xlabel('Age', csfont, fontsize=label_fontsize);
    ax4.set_xlabel('Age', csfont, fontsize=label_fontsize);

    ax1.hlines(0, ax1.get_xlim()[0], ax1.get_xlim()[1], linestyle='-', color='k', linewidth=1.25, alpha=0.8)
    ax2.hlines(0, ax2.get_xlim()[0], ax2.get_xlim()[1], linestyle='-', color='k', linewidth=1.25, alpha=0.8)
    ax3.hlines(0, ax3.get_xlim()[0], ax3.get_xlim()[1], linestyle='-', color='k', linewidth=1.25, alpha=0.8)
    ax4.hlines(0, ax4.get_xlim()[0], ax4.get_xlim()[1], linestyle='-', color='k', linewidth=1.25, alpha=0.8)

    ax1.set_ylabel('IMV: Demographics', csfont, fontsize=label_fontsize)
    ax2.set_ylabel('IMV: Education', csfont, fontsize=label_fontsize)
    ax3.set_ylabel('IMV: Cognition', csfont, fontsize=label_fontsize)
    ax4.set_ylabel('IMV: Grip and Gait', csfont, fontsize=label_fontsize)

    ax1.yaxis.set_major_locator(plt.MaxNLocator(6))
    ax2.yaxis.set_major_locator(plt.MaxNLocator(6))
    ax3.yaxis.set_major_locator(plt.MaxNLocator(6))
    ax4.yaxis.set_major_locator(plt.MaxNLocator(6))

    ax1.tick_params(axis='both', which='major', labelsize=13)
    ax2.tick_params(axis='both', which='major', labelsize=13)
    ax3.tick_params(axis='both', which='major', labelsize=13)
    ax4.tick_params(axis='both', which='major', labelsize=13)

    ax1.legend(frameon=True, ncol=5,
               fontsize=label_fontsize-4.5, framealpha=1, facecolor='w',
               edgecolor='k', handletextpad=0.25,
               # bbox_to_anchor=(1.05, 1),
               loc='upper center')

    ax2.legend(frameon=True, ncol=5,
               fontsize=label_fontsize-4.5, framealpha=1, facecolor='w',
               edgecolor='k', handletextpad=0.25,
               # bbox_to_anchor=(1.05, 1),
               loc='upper center')
    ax3.legend(frameon=True, ncol=5,
               fontsize=label_fontsize-4.5, framealpha=1, facecolor='w',
               edgecolor='k', handletextpad=0.25,
               # bbox_to_anchor=(1.05, 1),
               loc='upper center')

    ax4.legend(frameon=True, ncol=5,
               fontsize=label_fontsize-4.5, framealpha=1, facecolor='w',
               edgecolor='k', handletextpad=0.25,
               # bbox_to_anchor=(1.05, 1),
               loc='upper center')

    ax1.annotate(r'Baccarat (0.048)',
                 xy=(70, 0.05), xycoords='data', **csfont,
                 xytext=(76, 0.0675), fontsize=14, textcoords='data',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=0.25", linewidth=0.5,
                                 edgecolor='k', linestyle='-'))

    ax2.annotate(r'Blackjack (0.01)',
                 xy=(70, 0.0099), xycoords='data', **csfont,
                 xytext=(76, 0.025), fontsize=14, textcoords='data',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=0.25", linewidth=0.5,
                                 edgecolor='k'))

    ax2.annotate(r'Baccarat (0.048)',
                 xy=(70, 0.05), xycoords='data', **csfont,
                 xytext=(76, 0.0675), fontsize=14, textcoords='data',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=0.25", linewidth=0.5,
                                 edgecolor='k', linestyle='-'))

    ax3.annotate(r'Blackjack (0.01)',
                 xy=(70, 0.0099), xycoords='data', **csfont,
                 xytext=(76, 0.025), fontsize=14, textcoords='data',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=0.25", linewidth=0.5,
                                 edgecolor='k'))

    ax3.annotate(r'Baccarat (0.048)',
                 xy=(70, 0.05), xycoords='data', **csfont,
                 xytext=(76, 0.0675), fontsize=14, textcoords='data',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=0.25", linewidth=0.5,
                                 edgecolor='k', linestyle='-'))

    ax4.annotate(r'Baccarat (0.048)',
                 xy=(70, 0.05), xycoords='data', **csfont,
                 xytext=(76, 0.0675), fontsize=14, textcoords='data',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=0.25", linewidth=0.5,
                                 edgecolor='k', linestyle='-'))

    # ax3.annotate(r'Blackjack',
    #             xy=(60, 0.0099), xycoords='data', **csfont,
    #             xytext=(62.5, 0.0275), fontsize=12, textcoords='data',
    #             arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=0.25", linewidth=0.5,
    #                             edgecolor='k'))

    # ax3.annotate(r'Baccarat',
    #             xy=(90, 0.048), xycoords='data', **csfont,
    #             xytext=(82.5, 0.0275), fontsize=12, textcoords='data',
    #             arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=0.25", linewidth=0.5,
    #                             edgecolor='k', linestyle='-'))

    # ax4.annotate(r'Blackjack',
    #             xy=(60, 0.0099), xycoords='data', **csfont,
    #             xytext=(62.5, 0.0275), fontsize=12, textcoords='data',
    #             arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=0.25", linewidth=0.5,
    #                             edgecolor='k'))
    # ax4.annotate(r'Baccarat',
    #             xy=(90, 0.048), xycoords='data', **csfont,
    #             xytext=(82.5, 0.0275), fontsize=12, textcoords='data',
    #             arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=0.25", linewidth=0.5,
    #                             edgecolor='k', linestyle='-'))

    ax1.set_ylim(ax2.get_ylim()[0], ax1.get_ylim()[1]+.025)
    ax1.set_xlim(55, 92)
    # ax1.spines['bottom'].set_bounds(ax1.get_xlim()[0], ax1.get_xlim()[1])
    # ax1.spines['left'].set_bounds(0, ax1.get_ylim()[1])

    ax2.set_ylim(ax1.get_ylim()[0], ax1.get_ylim()[1])
    ax2.set_xlim(55, 92)
    # ax2.spines['bottom'].set_bounds(ax2.get_xlim()[0], ax2.get_xlim()[1])
    # ax2.spines['left'].set_bounds(-0.008, ax2.get_ylim()[1])

    ax3.set_ylim(ax1.get_ylim()[0], ax1.get_ylim()[1])
    ax3.set_xlim(55, 92)
    # ax3.spines['bottom'].set_bounds(60, ax3.get_xlim()[1])
    # ax3.spines['left'].set_bounds(-.014, 0.016)

    ax4.set_ylim(ax1.get_ylim()[0], ax1.get_ylim()[1])
    ax4.set_xlim(55, 92)
    # ax4.spines['bottom'].set_bounds(60, ax4.get_xlim()[1])
    # ax4.spines['left'].set_bounds(-.014, 0.016)

    for axy, data in zip([ax1, ax2, ax3, ax4], [out1a, out1b, out1c, out2c]):
        iterator = 0
        for col in data['V1'].unique():
            if axy == ax4:
                gap = 2.5
            else:
                gap = 3
            x = data[data['V1'] == col].reset_index()['V2'][0] - gap
            y = data[data['V1'] == col].reset_index()['V4'][0] -.00175
            iterator = iterator + 1

    ax1.hlines(0.048, ax1.get_xlim()[0], 90,
               linestyle=[(0, (12, 6, 12, 6))],
               color='k', linewidth=0.5, alpha=0.375)
    ax2.hlines(0.048, ax2.get_xlim()[0], 90,
               linestyle=[(0, (12, 6, 12, 6))],
               color='k', linewidth=0.5, alpha=0.375)
    ax3.hlines(0.048, ax3.get_xlim()[0], 90,
               linestyle=[(0, (12, 6, 12, 6))],
               color='k', linewidth=0.5, alpha=0.375)
    ax4.hlines(0.048, ax4.get_xlim()[0], 90,
               linestyle=[(0, (12, 6, 12, 6))],
               color='k', linewidth=0.5, alpha=0.375)
    ax1.hlines(0.0099, ax1.get_xlim()[0], 90,
               linestyle=[(0, (12, 6, 12, 6))],
               color='k', linewidth=0.5, alpha=0.375)
    ax2.hlines(0.0099, ax2.get_xlim()[0], 90,
               linestyle=[(0, (12, 6, 12, 6))],
               color='k', linewidth=0.5, alpha=0.375)
    ax3.hlines(0.0099, ax3.get_xlim()[0], 90,
               linestyle=[(0, (12, 6, 12, 6))],
               color='k', linewidth=0.5, alpha=0.375)
    ax4.hlines(0.0099, ax4.get_xlim()[0], 90,
               linestyle=[(0, (12, 6, 12, 6))],
               color='k', linewidth=0.5, alpha=0.375)
    sns.despine()
    plt.subplots_adjust(wspace=0.225, hspace=0.225)
    plt.savefig(os.path.join(fig_path, fig_name),
                bbox_inches='tight')
