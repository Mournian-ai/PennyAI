import os
import sys

# Add the Penny directory to sys.path so tests can import project modules
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Penny'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Provide a minimal pydantic stub so tests can run without installing the
# external dependency. Only the small subset needed for these tests is
# implemented.
import types
if 'pydantic' not in sys.modules:
    pydantic_stub = types.ModuleType('pydantic')

    class BaseModel:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

    pydantic_stub.BaseModel = BaseModel
    sys.modules['pydantic'] = pydantic_stub
