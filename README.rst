easyGlobalVariable
==================

A simple Python library to store, retrieve, and manage global variables across your project with a dictionary-like interface, supporting filtering and persistence.

Installation
------------

Clone the repository and install it in editable mode or just copy the package:

.. code-block:: bash

    pip install -e .

Usage
-----

Import the library and use it like a dictionary.

Basic Operations
^^^^^^^^^^^^^^^^

.. code-block:: python

    import easyGlobalVariable as gv

    # Store variables (supports any object)
    gv['api_key'] = "secret_key"
    gv['max_retries'] = 3
    gv['my_func'] = lambda x: x ** 2

    # Retrieve variables
    print(gv['api_key'])
    
    # Check type
    print(type(gv['max_retries']))  # <class 'int'>

    # Delete variables
    del gv['api_key']
    # OR
    gv.delete('max_retries')

Safe Access and Explicit Setting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use ``get()`` to safely retrieve variables with a default value, and ``set()`` to explictly store them.

.. code-block:: python

    # Get with default value (returns None if not found, or specified default)
    api_key = gv.get('api_key')
    timeout = gv.get('timeout', 30)

    # Explicit set (equivalent to gv['key'] = value)
    gv.set('status', 'active')

Filtering and Persistence
^^^^^^^^^^^^^^^^^^^^^^^^^

You can filter variables by name and save them to a file (pickle format).

.. code-block:: python

    # Store related variables
    gv['session_id'] = 123
    gv['session_user'] = 'admin'
    gv['config_mode'] = 'debug'

    # Filter by prefix 'session_' and save to 'session.pkl'
    gv.startswith('session_').save('session.pkl')

    # Filter by suffix
    gv.endswith('_mode').save('config.pkl')

    # Filter by substring
    gv.contains('user').save('user.pkl')

Loading Variables
^^^^^^^^^^^^^^^^^

Load variables back from a file into the global registry.

.. code-block:: python

    # Load variables
    gv.load('session.pkl')

    print(gv['session_id'])  # 123

Testing
-------

Run the tests using the included test script:

.. code-block:: bash

    python test_library.py
