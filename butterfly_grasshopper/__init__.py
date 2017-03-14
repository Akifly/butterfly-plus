import sys
import os

if 'butterfly' not in sys.modules:
    sys.path.insert(
        0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    import butterfly
except ImportError as e:
    raise ImportError('Can\'t find butterfly in sys.path.\n'
                      'You need to install butterfly to use butterfly-grasshopper.\n'
                      'You can download butterfly from\n'
                      'https://github.com/mostaphaRoudsari/Butterfly')
