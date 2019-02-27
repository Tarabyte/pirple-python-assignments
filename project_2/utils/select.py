"""
Keyboard Selector
"""
from pynput import keyboard
from .clear import clear


def select(options, selected=0, header='', empty=u'\u25EF', current=u'\u233E'):
    """
    Simulate keyboard selection using arrow up/down
    """
    total_options = len(options)

    def show_options():
        clear()
        print(header)
        for index, option in enumerate(options):
            print(f'{current if index == selected else empty}  {option}')

    def handle_arrows(key):
        # update outer selected value
        nonlocal selected

        # confirm choice on enter
        if key == keyboard.Key.enter:
            return False

        # handle up down
        if key == keyboard.Key.down:
            selected = min(selected + 1, total_options - 1)
        elif key == keyboard.Key.up:
            selected = max(selected - 1, 0)

        show_options()

    with keyboard.Listener(on_press=handle_arrows) as listener:
        show_options()
        listener.join()
        input('')  # swallow last input

    return selected
