# star.py

"""
This module defines a class for rendering an HTML star rating component.

Classes:
    StarRating: A class representing a star rating component.
"""


class StarRating:
    """
    A class representing a star rating component.

    Attributes:
        name (str): The name of the star rating component, used for grouping radio inputs.
        num_stars (int): The number of stars in the rating.
    """

    def __init__(self, name, num_stars):
        """
        Initializes the StarRating instance with the provided parameters.

        Args:
            name (str): The name of the star rating component, used for grouping radio inputs.
            num_stars (int): The number of stars in the rating.
        """
        self.name = name
        self.num_stars = num_stars

    def render_html(self):
        """
        Renders the HTML representation of the star rating component.

        Returns:
            str: HTML representation of the star rating component.
        """
        star_elements = "".join(
            f"""
            <input type="radio" name="{self.name}" id="{self.name}-{self.num_stars - i}" value="{self.num_stars - i}"/>
            <label for="{self.name}-{self.num_stars - i}"></label>
            """
            for i in range(self.num_stars)
        )

        css = """
        <style>
            .star-rating {
                display: flex;
                align-items: center;
                width: 160px;
                flex-direction: row-reverse;
                justify-content: space-between;
                margin: 0px auto;
                position: relative;
            }
            /* hide the inputs */
            .star-rating input {
                display: none;
            }
            /* set properties of all labels */
            .star-rating > label {
                width: 30px;
                height: 30px;
                font-family: Arial;
                font-size: 30px;
                transition: 0.2s ease;
                color: orange;
            }
            /* give label a hover state */
            .star-rating label:hover {
                color: #ff69b4;
                transition: 0.2s ease;
            }
            .star-rating label:active::before {
                transform:scale(1.1);
            }

            /* set shape of unselected label */
                .star-rating label::before {
                content: '\\2606';
                position: absolute;
                top: 0px;
                line-height: 26px;
            }
            /* set full star shape for checked label and those that come after it */
            .star-rating input:checked ~ label:before {
            content:'\\2605';
            }

            @-moz-document url-prefix() {
            .star-rating input:checked ~ label:before {
            font-size: 36px;
            line-height: 21px;
            }
            }
        </style>
        """

        html = f"""
            {css}
            <div class="star-rating">
                {star_elements}
            </div>
        """
        return html
