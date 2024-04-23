from helper import *
import numpy as np
from load_point_clouds import *
import os


def kd_tree_nearest_neighbor_knn(pcd, point_index = 5,number_of_neighbor = 100):
    pcd.paint_uniform_color([0.5, 0.5, 0.5])
    pcd_tree        = o3d.geometry.KDTreeFlann(pcd)
    pcd.colors[point_index] = [1, 0, 0]
    [k, idx, _] = pcd_tree.search_knn_vector_3d(pcd.points[point_index], number_of_neighbor)
    np.asarray(pcd.colors)[idx[1:], :] = [0, 0, 1]
    o3d.visualization.draw_geometries([pcd], "Kd_tree_nearest_neighbor_knn", width=800, height=600, left=50, top=50)


def kd_tree_nearest_neighbor_radius(pcd, point_index = 5, radius = 0.02):
    pcd.paint_uniform_color([0.5, 0.5, 0.5])
    pcd_tree        = o3d.geometry.KDTreeFlann(pcd)
    pcd.colors[point_index] = [1, 0, 0]
    [k, idx, _] = pcd_tree.search_radius_vector_3d(pcd.points[point_index], radius)
    np.asarray(pcd.colors)[idx[1:], :] = [0, 0, 1]
    o3d.visualization.draw_geometries([pcd], "Kd_tree_radius_knn", width=800, height=600, left=50, top=50)
    

def octree_nearest_neighbor(pcd, point_index = 5, max_depth = 4, size_expand=0.01):
    pcd.colors  = o3d.utility.Vector3dVector(np.random.uniform(0, 1, size=(np.asarray(pcd.points).shape[0], 3)))
    octree      = o3d.geometry.Octree(max_depth=max_depth)
    octree.convert_from_point_cloud(pcd, size_expand=size_expand)
    o3d.visualization.draw_geometries([octree] , f"Octree_depth_{max_depth}", width=800, height=600, left=50, top=50)
    octree.traverse(f_traverse)
    octree.locate_leaf_node(pcd.points[point_index])
    

if __name__ == "__main__":
    n           = 5000
    armadillo   = o3d.data.ArmadilloMesh()
    mesh        = o3d.io.read_triangle_mesh(armadillo.path)
    pcd         = mesh.sample_points_poisson_disk(n)
    pcd.scale(1 / np.max(pcd.get_max_bound() - pcd.get_min_bound()),
        center=pcd.get_center())
    kd_tree_nearest_neighbor_knn(pcd,5,100)
    kd_tree_nearest_neighbor_radius(pcd,5, 0.15)
    octree_nearest_neighbor(pcd)
    
    