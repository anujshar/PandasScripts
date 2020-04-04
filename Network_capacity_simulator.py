#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 08:46:43 2019

@author: anuj
"""
import csv
import pandas as pd


#TIL: don't hardcode column numbers, use the row with carrier name to parse data frames in get spectrum holdings methods
#TIL: create one method where name of carrier is passed as parameter

def get_spectrum_holdings():
    #dictionary of dictionaries of data frames to hold spectrum holdings [VZ][2018]
    dict_spectrum_cma = {}
    
    #VZ
    dict_vz_spectrum_cma = {}
    dict_vz_spectrum_cma['2018'] = pd.DataFrame([])
    dict_vz_spectrum_cma['2018'] = pd.read_excel('Spectrum holdings data.xlsx', sheet_name = 'Spectrum Holding', skiprows = 7, usecols = 'B,D,I:Q', index_col = 0)
    dict_spectrum_cma['VZ'] = dict_vz_spectrum_cma
    
    #ATT
    dict_att_spectrum_cma = {}
    dict_att_spectrum_cma['2018'] = pd.DataFrame([])
    dict_att_spectrum_cma['2018'] = pd.read_excel('Spectrum holdings data.xlsx', sheet_name = 'Spectrum Holding', skiprows = 7, usecols = 'B,D,W:AE', index_col = 0)
    dict_spectrum_cma['ATT'] = dict_att_spectrum_cma
    
    #TMO
    dict_tmo_spectrum_cma = {}
    dict_tmo_spectrum_cma['2018'] = pd.DataFrame([])
    dict_tmo_spectrum_cma['2018'] = pd.read_excel('Spectrum holdings data.xlsx', sheet_name = 'Spectrum Holding', skiprows = 7, usecols = 'B,D,AK:AS', index_col = 0)
    dict_spectrum_cma['TMO'] = dict_tmo_spectrum_cma
    
    #SPRINT
    dict_sprint_spectrum_cma = {}
    dict_sprint_spectrum_cma['2018'] = pd.DataFrame([])
    dict_sprint_spectrum_cma['2018'] = pd.read_excel('Spectrum holdings data.xlsx', sheet_name = 'Spectrum Holding', skiprows = 7, usecols = 'B,D,AY:BG', index_col = 0)
    dict_spectrum_cma['SPRINT'] = dict_sprint_spectrum_cma
    
    return dict_spectrum_cma

# returns end of the year macro towers
def get_macro_towers():
    #dictionary of data frames to hold macro towers
    dict_macro_towers = {}
    
    # VZ towers
    df_macro_towers_vz = pd.read_excel('Spectrum holdings data.xlsx', sheet_name = 'Macro Towers', index_col = 0, usecols = 'A,B')
    df_macro_towers_vz.columns = ['2018']
    dict_macro_towers['VZ'] = df_macro_towers_vz
    
    # VZ towers
    df_macro_towers_att = pd.read_excel('Spectrum holdings data.xlsx', sheet_name = 'Macro Towers', index_col = 0, usecols = 'A,C')
    df_macro_towers_att.columns = ['2018']
    dict_macro_towers['ATT'] = df_macro_towers_att
    
    # TMO towers
    df_macro_towers_tmo = pd.read_excel('Spectrum holdings data.xlsx', sheet_name = 'Macro Towers', index_col = 0, usecols = 'A,D')
    df_macro_towers_tmo.columns = ['2018']
    dict_macro_towers['TMO'] = df_macro_towers_tmo
    
    # SPRINT towers
    df_macro_towers_sprint = pd.read_excel('Spectrum holdings data.xlsx', sheet_name = 'Macro Towers', index_col = 0, usecols = 'A,E')
    df_macro_towers_sprint.columns = ['2018']
    dict_macro_towers['SPRINT'] = df_macro_towers_sprint
    
    return dict_macro_towers

def get_spectral_efficiency():
    df_spectral_efficiency = pd.read_excel('Spectrum holdings data.xlsx', sheet_name = 'Spectral Efficiency', index_col = 0)
    return df_spectral_efficiency


#TIL: refactor the method so that you can pass a parameter for each carrier instead of copying code 4 times
def get_technology():
    # 3 level dictionary to hold technologies - [VZ][3G][2018]
    
    dict_technology = {}
    
    
    # VZ
    df_Technology_Spread_temp = pd.read_excel('Spectrum holdings data.xlsx', sheet_name = 'Technology Spread', index_col =0, skiprows = 1, usecols = 'A:J')
    
    df_3G_VZ_2018 = pd.read_excel('Spectrum holdings data.xlsx', sheet_name = 'Macro Towers', index_col = 0, usecols = 'A')
    df_4G_VZ_2018 = df_3G_VZ_2018.copy()
    df_4GU_VZ_2018 = df_3G_VZ_2018.copy()
    df_5G_VZ_2018 = df_3G_VZ_2018.copy()
    
    columns = df_Technology_Spread_temp.columns
    
    for col in columns:
        df_3G_VZ_2018[col] = df_Technology_Spread_temp.loc['3G'][col]
        df_4G_VZ_2018[col] = df_Technology_Spread_temp.loc['4G'][col]
        df_4GU_VZ_2018[col] = df_Technology_Spread_temp.loc['4GU'][col]
        df_5G_VZ_2018[col] = df_Technology_Spread_temp.loc['5G'][col]
    
    dict_VZ_3G = {}
    dict_VZ_3G['2018'] = df_3G_VZ_2018
    dict_VZ_4G = {}
    dict_VZ_4G['2018'] = df_4G_VZ_2018
    dict_VZ_4GU = {}
    dict_VZ_4GU['2018'] = df_4GU_VZ_2018
    dict_VZ_5G = {}
    dict_VZ_5G['2018'] = df_5G_VZ_2018
    
    dict_VZ = {}
    dict_VZ['3G'] = dict_VZ_3G
    dict_VZ['4G'] = dict_VZ_4G
    dict_VZ['4GU'] = dict_VZ_4GU
    dict_VZ['5G'] = dict_VZ_5G
    
    dict_technology['VZ'] = dict_VZ
    
    #ATT
        
    #TMO
    
    #SPRINT
    
    return dict_technology

#compute capacity in each cma
def compute_initial_capacity():
    #dictionary of data frames [VZ]
    dict_capacity = {}
    
    dict_spectrum_cma = get_spectrum_holdings()
    dict_macro_towers = get_macro_towers()
    df_spectral_efficiency = get_spectral_efficiency()
    dict_technology = get_technology()
    
    # instantiate dataframe for holding capacity
    df_capacity_VZ = pd.DataFrame([])
    df_capacity_VZ = pd.read_excel('Spectrum holdings data.xlsx', sheet_name = 'Macro Towers', index_col = 0, usecols = 'A')
    
    # compute weighted average of spectal efficiency
    temp_3G_df = dict_technology['VZ']['3G']['2018']*(df_spectral_efficiency.loc["3G"])
    temp_4G_df = dict_technology['VZ']['4G']['2018']*(df_spectral_efficiency.loc["4G"])
    temp_4GU_df = dict_technology['VZ']['4GU']['2018']*(df_spectral_efficiency.loc["4G"])
    temp_5G_df = dict_technology['VZ']['5G']['2018']*(df_spectral_efficiency.loc["5G"])
    spec_eff_wa_df = temp_3G_df + temp_4G_df + temp_5G_df
    
    # compute capacity
    temp_capacity = dict_spectrum_cma['VZ']['2018']*spec_eff_wa_df
    
    return (temp_capacity)


print(get_spectral_efficiency().head())