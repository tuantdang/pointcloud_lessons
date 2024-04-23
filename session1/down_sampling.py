from helper import *
import numpy as np
from load_point_clouds import *

def voxel_grid_sampling(pcd, voxel_size =0.05):
    downpcd = pcd.voxel_down_sample(voxel_size=voxel_size)
    return downpcd

def farthest_point_sampling(pcd, num_points = 100):
    downpcd = pcd.farthest_point_down_sample(num_samples=num_points)
    return downpcd


if __name__ == "__main__":
    
    name_file = sys.argv[1] 
    path = f'data/down_sampling/{name_file}.ply'
    if name_file == 'conferenceRoom':
        voxel_size = 0.08
        num_points = 15000
    if name_file == 'fragment':
        voxel_size = 0.04
        num_points = 5000
        
    print("Load a ply point cloud, print it, and render it")
    pcd = o3d.io.read_point_cloud(path)
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    print(pcd)
    print(np.asarray(pcd.points))
   
    o3d.visualization.draw_geometries([pcd], width=800, height=600, left=50, top=50)
    print(f"Downsample the point cloud with a voxel of {voxel_size}")
    downpcd = voxel_grid_sampling(pcd, voxel_size)
    o3d.visualization.draw_geometries([downpcd], window_name  = "voxel_grid_sampling", width=800, height=600, left=50, top=50)
    
    
    
    print(f"Farthest point sampling with number of points is {num_points}")
    downpcd = farthest_point_sampling(pcd, num_points)
    o3d.visualization.draw_geometries([downpcd], window_name  = "farthest_point_sampling", width=800, height=600, left=50, top=50)
    
