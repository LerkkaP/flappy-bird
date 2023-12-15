import matplotlib
import matplotlib.backends.backend_agg as agg
import pylab
import pygame
from db.database_actions import get_highest_score, get_number_of_items, get_list_of_scores

class Stats():

    def _initialize_graph(self):
        '''Initialize graph'''
        matplotlib.use("Agg")
        fig = pylab.figure(figsize=[4, 4], dpi=100)
        ax = fig.gca()
        return fig, ax
    
    def _set_graph_properties(self, ax):
        ax.plot(get_list_of_scores())
        ax.set_title("Pisteiden kehittyminen")
        ax.set_xlabel('Pelikerta', fontsize=10)
        ax.set_ylabel('Pisteet', fontsize=10)
        ax.set_ylim(0, get_highest_score())
        ax.set_xlim(1, get_number_of_items())
        ax.xaxis.set_major_locator(pylab.MultipleLocator(1))
        ax.yaxis.set_major_locator(pylab.MultipleLocator(1))

    def _set_ticks(self, ax, ticks=8):
        x_values = range(1, get_number_of_items() + 1, max(1, get_number_of_items() // ticks))
        ax.set_xticks(x_values)

    def _render_graph(self, fig):
        '''Render graph'''
        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        surf = pygame.image.fromstring(data, size, "RGB")
        return surf

    def draw_graph(self):
        fig, ax = self._initialize_graph()
        self._set_graph_properties(ax)
        self._set_ticks(ax)
        return self._render_graph(fig)
    
# x_width -> print(size[0])
