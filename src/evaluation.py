"""
Model evaluation and metrics calculation
"""
from sklearn.metrics import r2_score

def calculate_mean_r2(y_true_dict, y_pred_dict):
    '''Calculate mean R² across all three parameters'''
    r2_scores = []
    for param in ['alkalinity', 'ec', 'drp']:
        r2 = r2_score(y_true_dict[param], y_pred_dict[param])
        r2_scores.append(r2)
    return sum(r2_scores) / len(r2_scores)
