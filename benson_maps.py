# import vsketch
from prettymaps import *
# import matplotlib.font_manager as fm
from matplotlib import pyplot as plt

# Init matplotlib figure, a 12in by 12in constrained/tight layout
fig, ax = plt.subplots(figsize=(12, 12), constrained_layout=True)

backup = plot(
    # Address:
    'Benson, North Carolina, United States of America',
    # Plot geometries in a circle of radius:
    radius=1100,
    # Matplotlib axis
    ax=ax,
    # Which OpenStreetMap layers to plot and their parameters:
    layers={
        # Perimeter (in this case, a circle)
        'perimeter': {},
        # Streets and their widths
        'streets': {
            'width': {
                'motorway': 5,
                'trunk': 5,
                'primary': 4.5,
                'secondary': 4,
                'tertiary': 3.5,
                'residential': 3,
                'service': 2,
                'unclassified': 2,
                'pedestrian': 2,
                'footway': 1,
            }
        },
        # Other layers:
        #   Specify a name (for example, 'building') and which OpenStreetMap tags to fetch
        'building': {'tags': {'building': True, 'landuse': 'construction'}, 'union': False},
        'water': {'tags': {'natural': ['water', 'bay']}},
        'green': {'tags': {'landuse': 'grass', 'natural': ['island', 'wood'], 'leisure': 'park'}},
        'forest': {'tags': {'landuse': 'forest'}},
        'parking': {'tags': {'amenity': 'parking', 'highway': 'pedestrian'}}
    },
    # drawing_kwargs:
    #   Reference a name previously defined in the 'layers' argument and specify matplotlib parameters to draw it
    drawing_kwargs={
        'background': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'hatch': 'ooo...', 'zorder': -1},
        'perimeter': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'lw': 0, 'hatch': 'ooo...',  'zorder': 0},
        'green': {'fc': '#D0F1BF', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
        'forest': {'fc': '#64B96A', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
        'water': {'fc': '#a1e3ff', 'ec': '#2F3737', 'hatch': 'ooo...', 'hatch_c': '#85c9e6', 'lw': 1, 'zorder': 2},
        'parking': {'fc': '#F2F4CB', 'ec': '#2F3737', 'lw': 1, 'zorder': 3},
        'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 3},
        'building': {'palette': ['#FFC857', '#E9724C', '#C5283D'], 'ec': '#2F3737', 'lw': .5, 'zorder': 4},
    },
    osm_credit={'color': '#2F3737'}
)

plt.savefig('./prints/benson/benson-1.png')
plt.savefig('./prints/benson/benson-1.svg')
