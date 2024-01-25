# Functions for `streamlined_ratio_model.ipynb`
# Author: Erin Watson

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy import stats


# Sum Data by Region section
def regional_numbers_to_ratios(region_speakers_df):
    """Returns a dataframe where the number of language speakers is expressed as a fraction of the total population."""
    # for each language, create a new column with the fraction of the population that speaks that language

    # create a new df with the fraction of the population that speaks each language
    ratio_region_speakers_df = pd.DataFrame(index=region_speakers_df.index, columns=region_speakers_df.columns)

    # for each language, create a new column with the fraction of the population that speaks that language
    for lang in region_speakers_df.columns:
        ratio_region_speakers_df[lang] = region_speakers_df[lang] / region_speakers_df["Population"]

    # drop the population column
    ratio_region_speakers_df.drop("Population", axis=1, inplace=True)

    return ratio_region_speakers_df


# Plotting sections
def plot_region(region, lang_codes, lang_names, df, y_axis_label, plot_title, color_list):
    fig, ax = plt.subplots(figsize=(10, 4))

    regional_df = df.loc[region]

    for i, lang in enumerate(lang_codes):
        ax.scatter(regional_df.index, regional_df[lang], label=lang_names[lang], color=color_list[i])
        ax.plot(regional_df.index, regional_df[lang], color_list[i]) # remove this line to remove the lines connecting the points

    # move the legend outside the plot
    # https://builtin.com/data-science/matplotlib-legend-outside-plot 
    pos = ax.get_position()
    ax.set_position([pos.x0, pos.y0, pos.width * 0.9, pos.height])
    ax.legend(loc='center right', bbox_to_anchor=(1.35, 0.5))

    fig.suptitle(f"{region} {plot_title}")
    ax.set_ylabel(f"{y_axis_label}")
    ax.set_xlabel("Year")
    plt.show()
    plt.close()

# Log odds section
def only_non_nan(x, y): 
    """Prepares x and y (vectors) for linear regression by removing missing values"""
    new_x = []
    new_y = []

    for x_val, y_val in zip(x, y):
        if not np.isnan(x_val) and not np.isnan(y_val):
            new_x.append(x_val)
            new_y.append(y_val)

    if len(new_x) == 0:
        return [np.nan], [np.nan] # return nan if there are no non-nan values
    
    else:
        return new_x, new_y
    

def create_log_odds_regression_line(log_odds_region_speakers_df, regions, lang_codes):
    """Create a regression line for each region-language pair. Store the slope, intercept and r-value in a dataframe that is returned"""

    regression_speakers_df = pd.DataFrame(index=pd.MultiIndex.from_product([regions, lang_codes]), columns=["slope", "intercept", "r_value", "p_value", "std_err"])

    for region in regions:
        for lang in lang_codes:
            x = log_odds_region_speakers_df.loc[region].index
            y = log_odds_region_speakers_df.loc[region][lang]

            x, y = only_non_nan(x, y)

            slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

            regression_speakers_df.loc[(region, lang)] = [slope, intercept, r_value, p_value, std_err]

    return regression_speakers_df

def create_future_log_odds_df(regression_speakers_df, regions, lang_codes, future_years=[2025, 2030, 2035, 2040, 2045, 2050]):
    """Create a dataframe with the predicted log odds for each region-language pair"""
    future_log_odds_region_df = pd.DataFrame(index=pd.MultiIndex.from_product([regions, future_years]), columns=lang_codes)

    for region in regions:
        for lang in lang_codes:
            slope, intercept, r_value, p_value, std_err = regression_speakers_df.loc[(region, lang)]
            x = np.array(future_years)
            y = slope * x + intercept
            future_log_odds_region_df.loc[(region, slice(None)), lang] = y

    return future_log_odds_region_df


def create_future_speakers_df(future_ratio_region_speakers_df):
    """Create a dataframe with the predicted number of speakers for each region-language pair"""
    language_cols = future_ratio_region_speakers_df.columns[:-1]

    # create a new df with the number of speakers for each language 
    future_speakers_df = pd.DataFrame(index=future_ratio_region_speakers_df.index, columns=language_cols)

    # for each language, create a new column with the number of speakers
    for lang in language_cols:
        future_speakers_df[lang] = future_ratio_region_speakers_df[lang] * future_ratio_region_speakers_df["Population"]

    # Add back the population column
    future_speakers_df = future_speakers_df.assign(Population=future_ratio_region_speakers_df["Population"])

    return future_speakers_df

# Plot the final results
def plot_proj_region(region, lang_codes, lang_names, df, y_axis_label, plot_title, color_list):
    fig, ax = plt.subplots(figsize=(10, 4))

    regional_df = df.loc[region]

    for i, lang in enumerate(lang_codes):
        ax.scatter(regional_df.index, regional_df[lang], label=lang_names[lang], color=color_list[i])
        ax.plot(regional_df.index, regional_df[lang], color_list[i]) # remove this line to remove the lines connecting the points

    # Add a dashed line for the total population
    ax.plot(regional_df.index, regional_df["Population"], "k--", label="Total Population")

    # move the legend outside the plot
    # https://builtin.com/data-science/matplotlib-legend-outside-plot 
    pos = ax.get_position()
    ax.set_position([pos.x0, pos.y0, pos.width * 0.9, pos.height])
    ax.legend(loc='center right', bbox_to_anchor=(1.35, 0.5))

    fig.suptitle(f"{region} {plot_title}")
    ax.set_ylabel(f"{y_axis_label}")
    ax.set_xlabel("Year")
    plt.show()
    plt.close()