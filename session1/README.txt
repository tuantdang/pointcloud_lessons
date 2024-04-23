Create envs: 

conda create -n aivn python=3.8
pip install open3d==0.18.0
pip install seaborn


1.load_point_clouds.py
Lệnh chạy:
    - python load_point_clouds.py bin
    - python load_point_clouds.py ply
    - python load_point_clouds.py txt

2.down_sampling.py
Lệnh chạy:
    - python down_sampling.py conferenceRoom
    - python down_sampling.py fragment

3.noise_removal.py
Lệnh chạy:
    - python noise_removal.py

4.neighbor_search.py
Lệnh chạy:
    - python neighbor_search.py

5.registration.py
Lệnh chạy:
    - python registration.py
6.rgbd_reconstruction.py
Lệnh chạy:
    - python rgbd_rescontruction.py 0
    - python rgbd_reconstruction.py 1
    - python rgbd_reconstruction.py 2

