import matplotlib
import matplotlib.backends.backend_agg as agg
import pylab
import pygame
from db.database_actions import get_highest_score, get_number_of_items, get_list_of_scores
from utils.button import Button

class Stats():
    def __init__(self):
        self._init_back_button()

    def _init_back_button(self):
        """Initialize back button attributes"""
        self.back_button = Button('BACK', 'center', 480)

    def handle_back_click(self, mouse_pos):
        """Handles the clicking of the back button"""
        return self.back_button.check_collision(mouse_pos)

    def _initialize_graph(self):
        '''Initialize graph'''
        matplotlib.use("Agg")
        fig = pylab.figure(figsize=[4, 4], dpi=100)
        ax = fig.gca()
        return fig, ax
    
    def _set_graph_properties(self, ax):
        ax.plot(get_list_of_scores(), color=[1.0, 0.5, 0.25])
        ax.set_title("Development of scores")
        ax.set_xlabel('Session', fontsize=10)
        ax.set_ylabel('Score', fontsize=10)
        
        ax.set_ylim(0, get_highest_score() + 1)
        ax.set_xlim(0, get_number_of_items())
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
        pylab.close(fig)
        return surf

    def draw_graph(self):
        fig, ax = self._initialize_graph()
        self._set_graph_properties(ax)
        self._set_ticks(ax)
        return self._render_graph(fig)
    
# x_width -> print(size[0])
