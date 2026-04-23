'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 

'''
    Produces a scatter plot of felony vs nonfelony predictions, hued by whether the current charge is a felony
 
    Parameters:
    - pred_universe_felony dataframe
 
    Returns:
    - A scatter plot of felony vs nonfelony predictions hued by whether the current charge is a felony
'''
def plot_scatter_by_felony_charge(pred_universe_felony):
    sns.lmplot(data=pred_universe_felony,
               x='prediction_felony',
               y='prediction_nonfelony',
               hue='has_felony_charge',
               fit_reg=False)
    plt.savefig('./data/part5_plots/scatter_felony_charge.png', bbox_inches='tight')
    plt.clf()
    print (" Part 5 #1"
        "\n\n" 
        " Same issue is here, with the fact that there are two big clusters with only a little overlap between them shows the strength of the current felony charge and how the model is going almost purely off of it. " \
        "\n\n"
        " And I guess this is the problem with it and the cluster on the right is what tells us that there is a heavy reliance on one feature. Real data wouldn't look like this - especially not with crime-related statistics where everything is occluded."
        "\n\n")



# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
    '''
    Produces a scatter plot of felony rearrest prediction vs actual rearrest outcome
 
    Parameters:
    - pred_universe_felony dataframe
 
    Returns:
    - Scatter plot of prediction_felony vs y_felony with regression line saved to data/part5_plots
    '''
def plot_scatter_prediction_vs_actual(pred_universe_felony):
    '''
    Produces a scatter plot of felony rearrest prediction vs actual rearrest outcome
 
    Parameters:
    - pred_universe_felony dataframe
 
    Returns:
    - Scatter plot of felony rearrest prediction vs actual rearrest outcome
    '''
    sns.lmplot(data=pred_universe_felony,
               x='prediction_felony',
               y='y_felony')
    plt.savefig('./data/part5_plots/scatter_prediction_vs_actual.png', bbox_inches='tight')
    plt.clf()
    print ("Part 5 #2" 
        "\n\n"
        " Well, looking at the plot, the line is pretty much perfect and it's saying the plot is perfectly calibrated. But I'm pretty sure that that is what makes it untrustworthy. All of the above issues I've talked about before, and then the plot shows perfect calibration?" 
        "\n\n"
        " That tells me that either the model is absurdly overfitted or the dataset isn't accurate or there was no train-test split done. "
        "\n\n"
        " An actual calibration plot that is based on properly split training and test data and using real-life crime data as foundation would look way worse than this. So, no - I would not use this plot to reasonably say whether the model is calibrated or not. There's something wrong somewhere.")