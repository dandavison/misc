import matplotlib
matplotlib.use('Qt5Agg')
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from mlxtend.plotting import plot_confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn import model_selection

DATA_FILE = '/tmp/creditcard.csv'

# %matplotlib inline
pd.options.display.max_columns = None


def tn(y_true, y_pred):
    return metrics.confusion_matrix(y_true, y_pred)[0, 0]

def fp(y_true, y_pred):
    return metrics.confusion_matrix(y_true, y_pred)[0, 1]

def fn(y_true, y_pred):
    return metrics.confusion_matrix(y_true, y_pred)[1, 0]

def tp(y_true, y_pred):
    return metrics.confusion_matrix(y_true, y_pred)[1, 1]

def tp_rate(y_true, y_pred):
    # Proportion of positives that are predicted positive.
    # aka "sensitivity", "recall"
    _tp = tp(y_true, y_pred)
    _fn = fn(y_true, y_pred)
    return _tp / (_tp + _fn)

def tn_rate(y_true, y_pred):
    # Proportion of negatives that are predicted negative.
    # aka "specificity"
    _tn = tn(y_true, y_pred)
    _fp = fp(y_true, y_pred)
    return _tn / (_tn + _fp)

def ppv(y_true, y_pred):
    # Proportion of predicted-positives that are truly positive.
    # "Positive Predictive Value"
    # aka "precision"
    _tp = tp(y_true, y_pred)
    _fp = fp(y_true, y_pred)
    return _tp / (_tp + _fp)

def npv(y_true, y_pred):
    # Proportion of predicted-negatives that are truly negative.
    # "Negative Predictive Value"
    _tn = tn(y_true, y_pred)
    _fn = fn(y_true, y_pred)
    return _tn / (_tn + _fn)


data = pd.read_csv(DATA_FILE)

y = data['Class'].values
X = data.drop(['Class', 'Time'], axis=1).values

gsc = model_selection.GridSearchCV(
    estimator=LogisticRegression(),
    param_grid={
        'class_weight': [{0: x, 1: 1.0-x} for x in np.linspace(0.5, 0.999, 10)]
    },
    scoring={
        'tp': metrics.make_scorer(tp),
        'tn': metrics.make_scorer(tn),
        'fp': metrics.make_scorer(fp),
        'fn': metrics.make_scorer(fn),

        'tpr': metrics.make_scorer(tp_rate),
        'tnr': metrics.make_scorer(tn_rate),
        'ppv': metrics.make_scorer(ppv),
        'npv': metrics.make_scorer(npv),

        'f1': metrics.make_scorer(metrics.f1_score),
        'roc_auc': metrics.make_scorer(metrics.roc_auc_score),
    },
    refit='f1',
    cv=2,
    n_jobs=-1,
    return_train_score=False,
)
grid_result = gsc.fit(X, y)

print("Best parameters : %s" % grid_result.best_params_)

cv_results = pd.DataFrame(grid_result.cv_results_)
cv_results['class_weight_0'] = [w[0] for w in cv_results['param_class_weight']]
scores_to_plot = [f'mean_test_{score}' for score in ['tpr', 'tnr', 'ppv', 'npv', 'f1', 'roc_auc']]
cv_results.plot(x='class_weight_0', y=scores_to_plot)
