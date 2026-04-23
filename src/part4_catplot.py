'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.
def plot_felony_prediction_by_charge(pred_universe_felony):
    '''
    Produces a categorical bar plot of felony rearrest prediction by charge type

    Parameters:
    - pred_universe_felony dataframe

    Returns:
    - Categorical bar plot of charge types by prediction for felony rearrest saved to data/part4_plots
    '''
    sns.catplot(data=pred_universe_felony,
                x='has_felony_charge',
                y='prediction_felony',
                kind='bar')
    plt.savefig('./data/part4_plots/catplot_felony_prediction.png', bbox_inches='tight')
    plt.clf()


# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest
def plot_nonfelony_prediction_by_charge(pred_universe_felony):
    '''
    Produces a categorical bar plot of nonfelony rearrest prediction by charge type

    Parameters:
    - pred_universe_felony dataframe

    Returns:
    - Categorical bar plot of nonfelony rearrest prediction by charge type
    '''
    sns.catplot(data=pred_universe_felony,
                x='has_felony_charge',
                y='prediction_nonfelony',
                kind='bar')
    plt.savefig('./data/part4_plots/catplot_nonfelony_prediction.png', bbox_inches='tight')
    plt.clf()


# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
def plot_felony_prediction_by_charge_hued(pred_universe_felony):
    '''
    Produces a categorical bar plot of felony rearrest prediction by charge type, hued by actual felony rearrest

    Parameters:
    - pred_universe_felony dataframe

    Returns:
    - Categorical bar plot of felony rearrest prediction by charge type, hued by actual felony rearrest
    '''
    sns.catplot(data=pred_universe_felony,
                x='has_felony_charge',
                y='prediction_felony',
                kind='bar',
                hue='y_felony')
    plt.savefig('./data/part4_plots/catplot_felony_prediction_hued.png', bbox_inches='tight')
    plt.clf()