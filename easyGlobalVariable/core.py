import pickle

gv_table_globals = {}

class VariableSubset:
    """Helper class to handle a subset of variables for operations like saving."""
    def __init__(self, data):
        self.data = data

    def save(self, filename):
        """Save the current subset of variables to a pickle file."""
        with open(filename, 'wb') as f:
            pickle.dump(self.data, f)
        print(f"Saved {len(self.data)} variables to {filename}")

class GlobalVariableManager:
    """
    A class to manage global variables across the project.
    It acts like a dictionary but is exposed as a module.
    """
    
    def __getitem__(self, key):
        """Retrieve a variable."""
        if key in gv_table_globals:
            return gv_table_globals[key]
        raise KeyError(f"Global variable '{key}' not found.")

    def __setitem__(self, key, value):
        """Store a variable."""
        gv_table_globals[key] = value

    def __delitem__(self, key):
        """Delete a variable using 'del gv[key]'."""
        if key in gv_table_globals:
            del gv_table_globals[key]
        else:
            raise KeyError(f"Global variable '{key}' not found.")

    def delete(self, key):
        """Delete a variable using 'gv.delete(key)'."""
        self.__delitem__(key)

    def startswith(self, prefix):
        """Return a VariableSubset of keys starting with prefix."""
        subset = {k: v for k, v in gv_table_globals.items() if k.startswith(prefix)}
        return VariableSubset(subset)

    def endswith(self, suffix):
        """Return a VariableSubset of keys ending with suffix."""
        subset = {k: v for k, v in gv_table_globals.items() if k.endswith(suffix)}
        return VariableSubset(subset)

    def contains(self, substring):
        """Return a VariableSubset of keys containing substring."""
        subset = {k: v for k, v in gv_table_globals.items() if substring in k}
        return VariableSubset(subset)

    def load(self, filename):
        """Load variables from a pickle file into the global registry."""
        try:
            with open(filename, 'rb') as f:
                data = pickle.load(f)
                if isinstance(data, dict):
                    gv_table_globals.update(data)
                    print(f"Loaded {len(data)} variables from {filename}")
                else:
                    print(f"Error: {filename} does not contain a dictionary.")
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")

    def __repr__(self):
        return f"<GlobalVariableManager storing {len(gv_table_globals)} items>"
