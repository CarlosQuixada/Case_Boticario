import locale

import matplotlib.pyplot as plt
import seaborn as sns

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

class Graph:
    def create_graph_line_group(self, df, title, col_x, col_y, col_group, x_label, y_label, lim_min, lim_max):
        ax = sns.catplot(x=col_x, y=col_y, hue=col_group, height=4, aspect=2,
                         capsize=.2, kind="point", data=df)

        ax.set(xlabel=x_label, ylabel=y_label)
        plt.title(title, fontsize=10)
        ax.despine(left=True)
        plt.xticks(rotation=45)
        plt.ylim(lim_min, lim_max)

        plt.savefig(f"imgs/{title}.png", dpi=300, bbox_inches='tight')
        plt.show()

    def create_graph_line(self, df, title, col_x, col_y, x_label, y_label, lim_min, lim_max):
        ax = sns.catplot(x=col_x, y=col_y, height=4, aspect=2, capsize=.2, kind="point", data=df, legend=False)

        for ind, safra in enumerate(list(sorted(set(df[col_x].values)))):
            value = df[df[col_x] == safra][col_y].values[0]
            ax.ax.text(ind, value, f'{value:.2f}', backgroundcolor='white', color='black', ha='center', va='center', fontsize=12)

        ax.set(xlabel=x_label, ylabel=y_label)
        plt.title(title)
        ax.despine(left=True)
        plt.xticks(rotation=45)
        plt.ylim(lim_min, lim_max)

        plt.savefig(f"imgs/{title}.png", dpi=300, bbox_inches='tight')
        plt.show()

    def create_graph_bar(self, df, col_x, col_y, x_label, y_label, title):
        plt.figure(figsize=(15, 6))
        aux = sns.barplot(x=col_x, y=col_y, data=df)
        aux.set(xlabel=x_label, ylabel=y_label)
        plt.title(title)

        for index, row in df.iterrows():
            aux.text(row.name, row[col_y], row[col_y], color='black', ha="center", fontsize=12)
        plt.savefig(f"imgs/{title}.png", dpi=300, bbox_inches='tight')

        plt.show()

    def create_graph_multi_bar(self, df, col_x, col_hue, col_value, x_label, y_label, title, legend, ordened=False,
                               cols_ordened=[]):
        df_plot = df.pivot(index=col_x, columns=col_hue, values=col_value)

        if ordened and cols_ordened:
            df_plot = df_plot.loc[cols_ordened]

        ax = df_plot.plot(kind='barh', figsize=(12, 10), width=0.8)

        ax.set_ylabel(x_label)
        ax.set_xlabel(y_label)
        ax.set_title(title)
        ax.legend(title=legend)
        ax.set_yticklabels(df_plot.index, rotation=0, ha='right')

        for container in ax.containers:
            ax.bar_label(container, padding=3, fontsize=12)

        plt.tight_layout()
        plt.savefig(f"imgs/{title}.png", dpi=300, bbox_inches='tight')
        plt.show()
