from helper import *
import cv2


def get_xyz_from_pts(u, v, depth, cx, cy, fx, fy, kernel_size=5):
    # print(f'get_xyz_from_pts = {pts_row}, depth = {depth.shape}')
    d = depth[int(v), int(u)] # height, width in depth image
    x = ((u - cx) / fx) * d
    y = ((v - cy) / fy )* d
    return np.array([x, y, d]).transpose()
    # return np.array([0, 0, d]).transpose()


def rgbd_reconstruction(name = "0"):
    color_raw = o3d.io.read_image(f"./data/rgbd/{name}.jpg")
    depth_raw = o3d.io.read_image(f"./data/rgbd/{name}.png")
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw)
    show_rgbd(rgbd_image)
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
        rgbd_image,
        o3d.camera.PinholeCameraIntrinsic(o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
    # Flip it, otherwise the pointcloud will be upside down
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    o3d.visualization.draw_geometries([pcd], window_name = name)
    
    
def get_xyz_from_pts(u, v, depth, cx=319.5, cy=239.5, fx=525.0, fy=525.0):
    # print(f'get_xyz_from_pts = {pts_row}, depth = {depth.shape}')
    d = depth[int(v), int(u)] # height, width in depth image
    x = ((u - cx) / fx) * d
    y = ((v - cy) / fy )* d
    return np.array([x, y, d]).transpose()
    # return np.array([0, 0, d]).transpose()

def show_rgbd(rgb, depth):
    plt.subplot(1, 2, 1)
    plt.title('RGB image')
    plt.imshow(rgb)
    plt.subplot(1, 2, 2)
    plt.title('Depth image')
    plt.imshow(depth)
    plt.show()
    
def np_to_pc(points, colors):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)    
    pcd.colors = o3d.utility.Vector3dVector(colors)    
    return pcd
    
def get_pcl(name = "0"):
    rgb = cv2.cvtColor(cv2.imread(f"./data/rgbd/{name}.jpg", cv2.IMREAD_UNCHANGED), cv2.COLOR_BGR2RGB) #read rgb
    # print(rgb[0:5,0:5])
    depth = cv2.imread(f"./data/rgbd/{name}.png", cv2.IMREAD_UNCHANGED)
    h, w = depth.shape
    print(w, h)
    N = w*h
    points = np.zeros((N,3))
    colors = np.zeros((N,3))
    index = 0
    for u in range(w):
        for v in range(h):
            points[index,:] = get_xyz_from_pts(u, v, depth)
            colors[index,:] = rgb[v,u]/255.0
            index += 1
    pcd = np_to_pc(points, colors)
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    show_rgbd(rgb, depth)
    o3d.visualization.draw_geometries([pcd], window_name = name)
    
    
if __name__ == "__main__":
    name_img = sys.argv[1]
    # rgbd_reconstruction(name = name_img)
    # intrinsic = o3d.camera.PinholeCameraIntrinsic(o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault)
    # print(intrinsic.intrinsic_matrix)
    get_pcl(name_img)