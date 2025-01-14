import argparse
import math
import os
from copy import deepcopy

import numpy as np
import open3d as o3d
import pinocchio as pin
from scipy.spatial.transform import Rotation

from seebelow.utils.data_utils import SEEBELOW_PKG_PATH
from seebelow.utils.pcd_utils import (animate_point_cloud, stl_to_pcd,
                                  visualize_pcds)
from seebelow.utils.transform_utils import pose2mat

quat_gt = np.array([0, -0.7071068, 0, 0.7071068])
pos_gt = np.array([0.56616064, 0.12552764, 0.0545865 - 0.009845])
pos_quat = np.hstack([pos_gt, quat_gt])
gt_T = pose2mat(pos_quat)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Time-series Heatmap Generator")
    parser.add_argument(
        "--dataset_path",
        type=str,
        default="./data/dataset_08-12-2023_05-02-59",
        help="Folder containing time-series data",
    )
    args = parser.parse_args()

    # Data Load
    dataset_path = args.dataset_path
    print(f"{dataset_path}/reconstruction.ply")

    recon_pcd = o3d.io.read_point_cloud(f"{dataset_path}/reconstruction.ply")
    recon_pcd.estimate_normals()
    recon_pcd.orient_normals_consistent_tangent_plane(10)
    recon_pcd.paint_uniform_color([0, 0, 0])

    hemistere_gt = stl_to_pcd(str(SEEBELOW_PKG_PATH / 'meshes' / 'tumor_big.stl'), transform=gt_T)
    phantom_mesh = o3d.io.read_triangle_mesh(str(SEEBELOW_PKG_PATH / 'meshes' / 'phantom_mesh.ply'))

    animate_point_cloud(recon_pcd, [phantom_mesh, hemistere_gt])
