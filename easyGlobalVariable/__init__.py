import sys
from .core import GlobalVariableManager

# Replace the module object in sys.modules with an instance of GlobalVariableManager
sys.modules[__name__] = GlobalVariableManager()
