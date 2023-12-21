import matplotlib
import matplotlib.backends.backend_agg as agg
import pylab
import pygame
from db.database_actions import get_highest_score, get_number_of_items, get_list_of_scores
from utils.text import Text


class Stats():
    """Class for managing the stats phase of the game

    Attributes:
        text: Instance of Text class
    """

    def __init__(self):
        """Initializes the Stats class
        """
        self.text = Text(480)

    def handle_back_click(self, mouse_pos):
        """Handles the clicking of the back button

        Args:
            mouse_pos: A tuple containing the x and y coordinates of the mouse click.

        Returns:
            True if the mouse click was on the back button, False otherwise
        """
        _, back_text_rect = self.text.back_button()
        return self.text.check_collision(back_text_rect, mouse_pos)

    def _initialize_graph(self):
        """Initializes the graph with Matplotlib

        Returns:
            A tuple containing the Matplotlib figure and axes objects for the graph.
        """
        matplotlib.use("Agg")
        fig = pylab.figure(figsize=[4, 4], dpi=100)
        ax = fig.gca()
        return fig, ax

    def _set_graph_properties(self, ax):
        """Sets graph properties

        Args:
            ax: Matplotlib axes object"""
        ax.plot(get_list_of_scores(), color=[1.0, 0.5, 0.25])
        ax.set_title("Development of scores")
        ax.set_xlabel('Session', fontsize=10)
        ax.set_ylabel('Score', fontsize=10)

        ax.set_ylim(0, get_highest_score() + 1)
        ax.set_xlim(0, get_number_of_items())
        ax.xaxis.set_major_locator(pylab.MultipleLocator(1))
        ax.yaxis.set_major_locator(pylab.MultipleLocator(1))

    def _set_ticks(self, ax, ticks=8):
        """Sets ticks on the graph

        Args:
            ax: Matplotlib axes object
            ticks (int): The number of ticks to be set on the x-axis
        """
        x_values = range(1, get_number_of_items() + 1,
                         max(1, get_number_of_items() // ticks))
        ax.set_xticks(x_values)

    def _render_graph(self, fig):
        """Renders the graph

        Args:
            fig: Matplotlib figure object representing the graph

        Returns:
            A surface of the rendered graph
        """
        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        surf = pygame.image.fromstring(data, size, "RGB")
        pylab.close(fig)
        return surf

    def draw_graph(self):
        """Draws the graph

        Returns:
            A surface of the rendered graph ready for display in the pygame window
        """
        fig, ax = self._initialize_graph()
        self._set_graph_properties(ax)
        self._set_ticks(ax)
        return self._render_graph(fig)
