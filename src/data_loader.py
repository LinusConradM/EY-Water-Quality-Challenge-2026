"""
Data loading utilities for EY Water Quality Challenge
"""
import pandas as pd
from pathlib import Path

def load_training_data():
    '''Load water quality training dataset'''
    data_path = Path(__file__).parent.parent / 'data' / 'raw' / 'water_quality_training_dataset.csv'
    return pd.read_csv(data_path)

def load_landsat_features(split='training'):
    '''Load Landsat features'''
    data_path = Path(__file__).parent.parent / 'data' / 'features' / f'landsat_features_{split}.csv'
    return pd.read_csv(data_path)

def load_terraclimate_features(split='training'):
    '''Load TerraClimate features'''
    data_path = Path(__file__).parent.parent / 'data' / 'features' / f'terraclimate_features_{split}.csv'
    return pd.read_csv(data_path)

def load_submission_template():
    '''Load submission template'''
    data_path = Path(__file__).parent.parent / 'data' / 'raw' / 'submission_template.csv'
    return pd.read_csv(data_path)
