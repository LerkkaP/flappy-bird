import matplotlib
import matplotlib.backends.backend_agg as agg
import pylab
import pygame

matplotlib.use("Agg")

class Stats():

    def draw_graph(self):
        fig = pylab.figure(figsize=[4, 4], 
                   dpi=100,      
                   )
        ax = fig.gca()
        ax.plot([1, 2, 4])

        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()

        surf = pygame.image.fromstring(raw_data, size, "RGB")

        return surf
