import ipywidgets as widgets

class Checkbox:

    def __init__(self):
        """Initializes a Checkbox through uesr input."""

        self.description = input('Enter the description for your Checkbox: ')
        return widgets.Checkbox(description=self.description)