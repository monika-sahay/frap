# components.py
class CustomSlider:
    def __init__(self, label, min_value, max_value, default_value, step):
        """
        Initialize a CustomSlider instance.

        Parameters:
        - label (str): The label or description for the slider.
        - min_value (int): The minimum value of the slider.
        - max_value (int): The maximum value of the slider.
        - default_value (int): The initial or default value of the slider.
        - step (int): The step size for incrementing or decrementing the slider value.
        """
        self.label = label
        self.min_value = min_value
        self.max_value = max_value
        self.default_value = default_value
        self.step = step

    def render_html(self):
        """
        Generate HTML markup for the custom slider element.

        Returns:
        - str: A string containing HTML markup for the custom slider element.
        """
        html = f'''
            <label>{self.label}</label>
            <input type="range" id="{self.label}" name="{self.label}" 
                   min="{self.min_value}" max="{self.max_value}" 
                   value="{self.default_value}" step="{self.step}">
            <span id="{self.label}-value">{self.default_value}</span>
            <br>
        '''
        return html

    def render_js(self):
        """
        Generate JavaScript code for the custom slider element.

        Returns:
        - str: A string containing JavaScript code for updating the slider's value display.
        """
        js = f'''
            $(document).ready(function() {{
                $('input[type="range"]').on('input', function() {{
                    var label = $(this).attr('id');
                    var value = $(this).val();
                    $('#{self.label}-value').text(value);
                }});
            }});
        '''
        return js

# class CustomSlider:
#     def __init__(self, label, min_value, max_value, default_value, step):
#         """
#         Initialize a CustomSlider instance.

#         Parameters:
#         - label (str): The label or description for the slider.
#         - min_value (int): The minimum value of the slider.
#         - max_value (int): The maximum value of the slider.
#         - default_value (int): The initial or default value of the slider.
#         - step (int): The step size for incrementing or decrementing the slider value.
#         """
#         self.label = label
#         self.min_value = min_value
#         self.max_value = max_value
#         self.default_value = default_value
#         self.step = step

#     def render(self):
#         """
#         Generate HTML markup for the custom slider element.

#         Returns:
#         - str: A string containing HTML markup for the custom slider element.
#         """
#         html = f'''
#             <label>{self.label}</label>
#             <input type="range" id="{self.label}" name="{self.label}" 
#                    min="{self.min_value}" max="{self.max_value}" 
#                    value="{self.default_value}" step="{self.step}">
#             <span id="{self.label}-value">{self.default_value}</span>
#             <br>
#         '''
#         return html

# def custom_slider(label, min_value, max_value, default_value, step):
#     """
#     Generate an HTML custom slider input element with label and value display.

#     This function generates HTML markup for a custom slider input element that allows users to select a value within a specified range. It also includes a label and a dynamically updated value display.

#     Parameters:
#     - label (str): The label or description for the slider.
#     - min_value (int): The minimum value of the slider.
#     - max_value (int): The maximum value of the slider.
#     - default_value (int): The initial or default value of the slider.
#     - step (int): The step size for incrementing or decrementing the slider value.

#     Returns:
#     - str: A string containing HTML markup for the custom slider element.

#     Example Usage:
#     ```python
#     slider_html = custom_slider("Volume", 0, 100, 50, 1)
#     ```

#     This example will generate HTML markup for a slider with the label "Volume," a range from 0 to 100, an initial value of 50, and a step size of 1.
#     """
#     html = f'''
#         <label>{label}</label>
#         <input type="range" id="{label}" name="{label}" min="{min_value}" max="{max_value}" value="{default_value}" step="{step}">
#         <span id="{label}-value">{default_value}</span>
#         <br>
#     '''
#     return html