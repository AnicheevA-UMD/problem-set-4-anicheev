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
    print(" For felony rearrests, the model is much more heavily weighed by a current charge since looking at the main database tells us that way less people have a felony rearrest overall."
          " This forces the model to exaggerate more on the basis of less - with the basis here being whether there's a current felony charge. If there is one, the model jumps on it and singles it out."
          " For non-felony rearrests, roughly half of the records in the csv have a non-felony rearrest which means that the model would have to use other features and can't rely on this one indicator to point fingers.")

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
    print(" It means that, again, the model is using a felony charge as a cudgel in the sense that if one has a current federal charge, that makes the model's propensity to predict a rearrest shoot up."
          " It's a problem because it definitely is one of the cases where a ML model reflects real-life institutional biases - once somebody is a felon, they become much more singled out by the system for that fact."
          " Like I said above, once that feature isn't there, whatever else the model uses is much more diluted as it can't look at the felony feature and just throw its hands up.")
