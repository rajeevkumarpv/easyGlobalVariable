import easyGlobalVariable as gv
import os

def demo():
    print("--- Easy Global Variable Demo ---")

    # 1. Storing Variables
    print("\n[One] Storing variables...")
    gv['api_key'] = "12345-ABCDE"
    gv['max_retries'] = 3
    gv['login_related_token'] = "sometoken"
    gv['login_related_expiry'] = "2025-12-31"
    gv['config_txt_file'] = "settings.txt"
    gv['data_txt_file'] = "data.txt"
    gv['web_session'] = "active"
    gv['web_cache'] = "cleared"
    
    print(f"Stored {len(gv._GlobalVariableManager__repr__().split()[-2]) if hasattr(gv, '_GlobalVariableManager__repr__') else 'multiple'} variables.") 
    # (Note: direct access to len isn't exposed on the class instance wrapper easily without a method, 
    # but the repr shows it. For demo, we just print.)

    # 2. Filtering and Saving
    print("\n[Two] Filtering and Saving...")
    
    # Method A: startswith -> save
    print("Saving variables starting with 'login_related_'...")
    gv.startswith('login_related_').save('login.pkl')

    # Method B: endswith -> save
    print("Saving variables ending with '_txt_file'...")
    gv.endswith('_txt_file').save('textfiles.pkl')

    # Method C: contains -> save
    print("Saving variables containing 'web_'...")
    gv.contains('web_').save('web_session.pkl')

    # 3. Loading
    print("\n[Three] Loading...")
    # Simulate a fresh start by clearing globals (for demo purposes only, using private dict)
    from easyGlobalVariable.core import gv_table_globals
    gv_table_globals.clear()
    print("Globals cleared.")

    print("Loading 'login.pkl'...")
    gv.load('login.pkl')
    try:
        print(f"Loaded 'login_related_token': {gv['login_related_token']}")
    except KeyError:
        print("Failed to load token.")

    print("Loading 'web_session.pkl'...")
    gv.load('web_session.pkl')
    try:
        print(f"Loaded 'web_session': {gv['web_session']}")
    except KeyError:
        print("Failed to load web session.")

    # Cleanup demo files
    for f in ['login.pkl', 'textfiles.pkl', 'web_session.pkl']:
        if os.path.exists(f):
            os.remove(f)
            print(f"Deleted demo file {f}")

    print("\n--- Demo Complete ---")

if __name__ == "__main__":
    demo()
