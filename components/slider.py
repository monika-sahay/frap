# slider.py

"""
This module defines a class for rendering a custom slider element.

Classes:
    CustomSlider: A class representing a custom slider element.
"""


class CustomSlider:
    """
    A class representing a custom slider element.

    Attributes:
        label (str): The label or description for the slider.
        min_value (int): The minimum value of the slider.
        max_value (int): The maximum value of the slider.
        default_value (int): The initial or default value of the slider.
        step (int): The step size for incrementing or decrementing the slider value.
    """
    def __init__(self, slider_config):
        """
        Initialize a CustomSlider instance.

        Parameters:
        - label (str): The label or description for the slider.
        - min_value (int): The minimum value of the slider.
        - max_value (int): The maximum value of the slider.
        - default_value (int): The initial or default value of the slider.
        - step (int): The step size for incrementing or decrementing the
            slider value.
        """
        self.label = slider_config["label"]
        self.min_value = slider_config["min_value"]
        self.max_value = slider_config["max_value"]
        self.default_value = slider_config["default_value"]
        self.step = slider_config["step"]

    def render_html(self):
        """
        Generate HTML markup for the custom slider element.

        Returns:
        - str: A string containing HTML markup for the custom slider element.
        """
        html = f"""
            <label>{self.label}</label>
            <input type="range" id="{self.label}" name="{self.label}"
                   min="{self.min_value}" max="{self.max_value}"
                   value="{self.default_value}" step="{self.step}">
            <span id="{self.label}-value">{self.default_value}</span>
            <br>
        """
        return html

    def render_js(self):
        """
        Generate JavaScript code for the custom slider element.

        Returns:
        - str: A string containing JavaScript code for updating the slider's value display.
        """
        js = f"""
            $(document).ready(function() {{
                $('input[type="range"]').on('input', function() {{
                    var label = $(this).attr('id');
                    var value = $(this).val();
                    $('#{self.label}-value').text(value);
                }});
            }});
        """
        return js
