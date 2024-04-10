import open3d as o3d
import numpy as np
from glob import glob
from helper import *
import sys

def load_bin(path):
    pcd_arr = np.fromfile(path, dtype=np.float32).reshape(-1, 4) # x,y,x,r
    return pcd_arr[:,:3], pcd_arr[:,3:]

def load_ply(path):
    pcd     = o3d.io.read_point_cloud(path)
    pcd_arr = np.asarray(pcd.points)
    pcd_color = np.asarray(pcd.colors)
    return pcd_arr, pcd_color
    
def load_txt(path):
    pcd_arr = np.loadtxt(path)
    return pcd_arr[:,:3], pcd_arr[:,3:]

if __name__=="__main__": 
    
    data = sys.argv[1]
    if data == 'bin':       # Kitti
        for path in glob(f'./data/{data}_samples/*'):
            pcd_arr, pcd_feature = load_bin(path) 
            draw_point_clouds(array = pcd_arr[:,:3], color = np.ones(pcd_arr.shape[0], dtype = "int") , name = path.split('/')[2])
    if data == 'ply':       # PCN
        for path in glob(f'./data/{data}_samples/*'):
            pcd_arr, pcd_color = load_ply(path)
            colors = pcd_color
            if pcd_color.shape[0] == 0:
                colors = None
                
            draw_point_clouds(array = pcd_arr, color = colors, logits_color = True,  name = path.split('/')[2])
    if data == 'txt':       # S3DIS
        for path in glob(f'./data/{data}_samples/*'):
            pcd_arr, pcd_feature = load_txt(path) 
            draw_point_clouds(array = pcd_arr, color = pcd_feature, logits_color = True,  name = path.split('/')[2])