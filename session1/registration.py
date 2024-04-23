
from helper import *

def point_to_point_ICP(source, target, threshold, trans_init):
    reg_p2p = o3d.pipelines.registration.registration_icp(
        source, target, threshold, trans_init,
        o3d.pipelines.registration.TransformationEstimationPointToPoint())
    draw_registration_result(source, target, reg_p2p.transformation, "Point to point ICP")
    return reg_p2p.transformation


def point_to_plane_ICP(source, target, threshold, trans_init):
    reg_p2l = o3d.pipelines.registration.registration_icp(
        source, target, threshold, trans_init,
        o3d.pipelines.registration.TransformationEstimationPointToPlane())
    draw_registration_result(source, target, reg_p2l.transformation, "Point to plane ICP")
    return reg_p2l.transformation

if __name__ == "__main__":
    demo_icp_pcds   = o3d.data.DemoICPPointClouds()
    source          = o3d.io.read_point_cloud(demo_icp_pcds.paths[0])
    target          = o3d.io.read_point_cloud(demo_icp_pcds.paths[1])
    threshold       = 0.02
    trans_init      = np.asarray([  [0.862, 0.011, -0.507, 0.5],
                                    [-0.139, 0.967, -0.215, 0.7],
                                    [0.487, 0.255, 0.835, -1.4], 
                                    [0.0, 0.0, 0.0, 1.0]])
    draw_registration_result(source, target, trans_init, "Initial alignment")
    # evaluation = o3d.pipelines.registration.evaluate_registration(
    #     source, target, threshold, trans_init)
    # print(evaluation)
    # reg_p2p_matrix = point_to_point_ICP(source, target, threshold, trans_init)
    # evaluation = o3d.pipelines.registration.evaluate_registration(
    #     source, target, threshold, reg_p2p_matrix)
    # print(evaluation)
    reg_p2l_matrix = point_to_plane_ICP(source, target, threshold, trans_init)
    # evaluation = o3d.pipelines.registration.evaluate_registration(
    #     source, target, threshold, reg_p2l_matrix)
    # print(evaluation)
    
    
    