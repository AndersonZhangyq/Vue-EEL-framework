import sys
import platform
import eel


@eel.expose  # Expose function to JavaScript
def say_hello_py(x):
    """Print message from JavaScript on app initialization, then call a JS function."""
    print("Hello from %s" % x)
    eel.say_hello_js("Python {from within say_hello_py()}!")


def start_eel(develop):
    """Start Eel with either production or development configuration."""
    if develop:
        directory = 'src'
        app = None
        page = {'port': 8080}
    else:
        directory = 'web'
        app = 'chrome-app'
        page = 'index.html'

    eel.init(directory)
    say_hello_py("Python World!")
    eel.say_hello_js(
        "Python World!"
    )  # Call a JavaScript function (must be after `eel.init()`)

    eel_kwargs = dict(
        host="localhost",
        port=9000,
        # size=(1280, 800),
    )
    try:
        eel.start(**eel_kwargs)

    except EnvironmentError:
        # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
        if sys.platform in ["win32", "win64"] and int(platform.release()) >= 10:
            eel.start(page, mode="edge", **eel_kwargs)
        else:
            raise


if __name__ == "__main__":
    print("Opening python...")
    start_eel(True)
