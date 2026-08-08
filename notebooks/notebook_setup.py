import os
import sys

IN_COLAB = {}
HOME_DIRECTORY = {}
SETUP_EXECUTED = {}


def setup_home_directory(notebook_name):
    # Ensure global state dictionaries exist to prevent unexpected KeyError/NameError
    globals().setdefault("SETUP_EXECUTED", {})
    globals().setdefault("HOME_DIRECTORY", {})

    setup_executed = SETUP_EXECUTED.get(notebook_name, False)
    if not setup_executed:
        try:
            home_dir = os.path.dirname(os.getcwd())
            sys.path.insert(0, home_dir)
            rel_home_dir = home_dir.replace(os.path.expanduser("~"), "~")
            print(f"Setup completed - added home_dir to system path: {rel_home_dir}")

            # Update global state
            globals()["SETUP_EXECUTED"][notebook_name] = True
            globals()["HOME_DIRECTORY"][notebook_name] = home_dir
            return home_dir
        except (
            FileNotFoundError,
            PermissionError,
            NotADirectoryError,
            OSError,
            RuntimeError,
        ) as e:
            # Handle filesystem access failures or path expansion issues
            globals()["SETUP_EXECUTED"][notebook_name] = False
            globals()["HOME_DIRECTORY"][notebook_name] = None
            print(f"Failed to setup home directory due to a system or path error: {e}")
            return None
        except (KeyError, TypeError) as e:
            # Handle dictionary mapping or type-related discrepancies
            globals()["SETUP_EXECUTED"][notebook_name] = False
            globals()["HOME_DIRECTORY"][notebook_name] = None
            print(
                f"Failed to setup home directory due to a state configuration error: {e}"
            )
            return None
    else:
        home_dir = HOME_DIRECTORY.get(notebook_name)
        rel_home_dir = (
            home_dir.replace(os.path.expanduser("~"), "~") if home_dir else home_dir
        )
        print("Already added home_dir to system path:", rel_home_dir)
        return home_dir


def setup_google_colab(notebook_name):
    try:
        from google.colab import drive, files  # pyrefly: ignore [missing-import]

        # Update the global variable
        globals()["IN_COLAB"][notebook_name] = True
        print("Completed setup of Google Colab libraries!")
        return True, drive, files
    except ImportError:
        print("Google Colab libraries not found. Are you running in a Colab notebook?")
        globals()["IN_COLAB"][notebook_name] = False
        return False, None, None
