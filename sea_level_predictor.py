import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="blue", label="Data")

    # Get slope and y-intercept of the line of best fit
    slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Plot line of best fit through 2050
    plt.plot(df["Year"], slope * df["Year"] + intercept, color="red", label="Line of Best Fit (1880-2013)")
    plt.plot([df["Year"].iloc[-1], 2050], [df["CSIRO Adjusted Sea Level"].iloc[-1], slope * 2050 + intercept], color="green", linestyle="--", label="Projection to 2050 (1880-2013)")

    # Filter data for years 2000 and later
    recent_years_df = df[df["Year"] >= 2000]

    # Get slope and y-intercept of the line of best fit for recent years
    recent_slope, recent_intercept, _, _, _ = linregress(recent_years_df["Year"], recent_years_df["CSIRO Adjusted Sea Level"])

    # Plot line of best fit for recent years through 2050
    plt.plot(recent_years_df["Year"], recent_slope * recent_years_df["Year"] + recent_intercept, color="orange", label="Line of Best Fit (2000-Present)")
    plt.plot([recent_years_df["Year"].iloc[-1], 2050], [recent_years_df["CSIRO Adjusted Sea Level"].iloc[-1], recent_slope * 2050 + recent_intercept], color="purple", linestyle="--", label="Projection to 2050 (2000-Present)")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Add legend
    plt.legend()

    plt.savefig('sea_level_plot.png')
    return plt.gca()