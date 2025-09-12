#!/usr/bin/env python3

import os
from Bio.PDB import PDBParser, PDBIO
from Bio.PDB.SASA import ShrakeRupley

def process_pdb_file(pdb_path, out_path, probe_radius=1.4, n_points=100):
    """
    读取一个 pdb 文件 -> 计算 SASA -> 将 SASA 值写入每个原子的 B-factor -> 存为新的 pdb 文件。
    """
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(os.path.basename(pdb_path), pdb_path)

    # 计算 SASA 原子级别
    sr = ShrakeRupley(probe_radius=probe_radius, n_points=n_points)
    sr.compute(structure, level="A")  # "A" 表示 atom 级别，每个原子都有 .sasa 属性

    # 将 SASA 写入每个原子的 B‐factor
    for atom in structure.get_atoms():
        # atom.sasa 是浮点数，B-factor 通常也浮点
        atom.set_bfactor(atom.sasa)

    # 保存新的 PDB
    io = PDBIO()
    io.set_structure(structure)
    io.save(out_path)

def process_folder(input_folder, output_folder, probe_radius=1.4, n_points=100):
    """
    批量处理一个文件夹里的所有 pdb 文件。
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for fname in os.listdir(input_folder):
        if not (fname.lower().endswith(".pdb")):
            continue
        in_path = os.path.join(input_folder, fname)
        out_fname = os.path.splitext(fname)[0] + "_sasa_b.pdb"
        out_path = os.path.join(output_folder, out_fname)
        print(f"Processing {fname} → {out_fname}")
        process_pdb_file(in_path, out_path, probe_radius=probe_radius, n_points=n_points)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Compute SASA for all PDBs in a folder, write SASA into B-factor, output new PDBs.")
    parser.add_argument("input_folder", help="Folder containing PDB files")
    parser.add_argument("output_folder", help="Folder to save PDBs with SASA‐in‐B‐factor")
    parser.add_argument("--probe", type=float, default=1.4, help="Probe radius in Å (default: 1.4)")
    parser.add_argument("--points", type=int, default=100, help="Number of points per atom surface (default: 100)")
    args = parser.parse_args()

    process_folder(args.input_folder, args.output_folder, probe_radius=args.probe, n_points=args.points)
