# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 21:56:06 2021

@author: Jorge
"""

import pandas as pd
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
import numpy as np

from scipy import ndimage
from shapely.geometry import Point

import os
import dataframe_image as dfi


def table_to_image(df):
    df_styled = df.style.highlight_max("Unnamed: 0")
    dfi.export(df_styled, 'df_styled.png')

def heatmap(filename, d, bins=(100,100), smoothing=1.3, cmap='jet'):
    def getx(pt):
        return pt.coords[0][0]

    def gety(pt):
        return pt.coords[0][1]

    x = list(d.geometry.apply(getx))
    y = list(d.geometry.apply(gety))
    heatmap, xedges, yedges = np.histogram2d(y, x, bins=bins)
    extent = [yedges[0], yedges[-1], xedges[-1], xedges[0]]

    logheatmap = np.log(heatmap)
    logheatmap[np.isneginf(logheatmap)] = 0
    logheatmap = ndimage.filters.gaussian_filter(logheatmap, smoothing, mode='nearest')
    
    plt.imshow(logheatmap, cmap=cmap, extent=extent)
    cbar = plt.colorbar()
    cbar.ax.set_title('# every 1000 feet')
    plt.title(f"{filename.replace('.csv', '').title()} concentration")
    plt.gca().invert_yaxis()
    plt.savefig(f'concentration/{filename.replace(".csv", "")}_concentration.jpg')
    plt.show()
    plt.clf()
    

def map_iteration():
    street_map = gpd.read_file('shape_files/Street_Network_Database_(SND).shp')
    
    
    for filename in os.listdir("POIs"):
        
        try:
            df = pd.read_csv(f'POIs/{filename}')
        except:
            print(f"Couldn't process file {filename}")
            print("\n\n\n")
            continue
        fig, ax = plt.subplots(figsize=(15,15))
        
        street_map.plot(ax=ax, color="white", alpha=0.5)
        
    
        df = pd.read_csv(f'POIs/{filename}')
        
        
        
        crs = {"init":"epsg:4326"}
        
        geometry = [Point(xy) for xy in zip(df["longitude"], df["latitude"])]
        
        geo_df = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)
        
        #geo_df.plot(ax = ax, markersize = 10, color = "blue", marker = "o", label = "POI")
        
        heatmap(filename, geo_df, bins=50, smoothing=1.5)


def map_creation():
    street_map = gpd.read_file('shape_files/Street_Network_Database_(SND).shp')
    
    
    df = pd.read_csv('csvs/sale_data.csv')
    df = df.sort_values(by=["price"], ascending=False)

    table_to_image(df)
    fig, ax = plt.subplots(figsize=(15,15))
        
    street_map.plot(ax=ax, color="white", alpha=0.5)
        
    crs = {"init":"epsg:4326"}
        
    geometry = [Point(xy) for xy in zip(df["longitude"], df["latitude"])]
        
    geo_df = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)
        
    #geo_df.plot(ax = ax, markersize = 10, color = "blue", marker = "o", label = "POI")
        
    heatmap('For Sale 40 Most Expensive Real Estate', geo_df, bins=50, smoothing=1.5)
        
df = pd.read_csv('csvs/sale_data.csv')
df = df[df['closest_type'] == 'primary_school']
df = df[df['bedrooms'] >= 3]
df = df[df['price'] < 1000000]
table_to_image(df)