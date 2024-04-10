from helper import *


def rgbd_reconstruction(name = "0"):
    color_raw = o3d.io.read_image(f"./data/rgbd/{name}.jpg")
    depth_raw = o3d.io.read_image(f"./data/rgbd/{name}.png")
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        color_raw, depth_raw)
    show_rgbd(rgbd_image)
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
    rgbd_image,
    o3d.camera.PinholeCameraIntrinsic(o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
    # Flip it, otherwise the pointcloud will be upside down
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    o3d.visualization.draw_geometries([pcd], window_name = name)
    
    
if __name__ == "__main__":
    name_img = sys.argv[1]
    rgbd_reconstruction(name = name_img)