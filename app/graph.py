from pandas import DataFrame
import altair as alt

def chart(df: DataFrame, x: str, y: str, target: str) -> alt.Chart:
    """
    Create an Altair Chart.

    Parameters:
        df (DataFrame): The DataFrame containing the data.
        x (str): The column name for the x-axis.
        y (str): The column name for the y-axis.
        target (str): The column name for the target variable.

    Returns:
        alt.Chart: Altair Chart object.
    """
    # Properties dictionary
    properties = {
        'width': 400,
        'height': 300,
        'background': 'gray',
        'padding': {'left': 20, 'right': 20, 'top': 10, 'bottom': 20}
    }

    # Chart object creation
    chart = alt.Chart(df, title="Sample Chart").mark_circle()

    # Encodings
    chart = chart.encode(
        x=alt.X(x, title=x),
        y=alt.Y(y, title=y),
        color=alt.Color(target, title=target),
        tooltip=[x, y, target]
    )

    # Applying properties
    chart = chart.properties(**properties)

    # Configure options
    chart = chart.configure_axis(
        grid=False,
        titleFontSize=14,
        labelFontSize=12,
    ).configure_legend(
        titleFontSize=14,
        labelFontSize=12,
    )

    return chart
