# LIBS‑SCReeN

**Screening raw materials from exploration to (post‑)beneficiation using Laser‑Induced Breakdown Spectroscopy (LIBS)**  
_BELSPO BRAIN‑be 2.0 project B2/191/P1 (2020 – 2024)_

This repository contains **proof‑of‑concept Python tools** developed in the framework of the **LIBS‑SCReeN** consortium to visualise and convert LIBS hyperspectral data cubes.  
The code is intended as an *illustrative starting‑point* rather than a production‑ready package.

---

## 📂 Repository layout

```text
LIBS-SCReeN/
├── LIBS Format conversion scripts (beta)/
│   ├── TIF_to_mat.py
│   ├── TIF_to_mat_and_netCDF.py
│   ├── mat_to_tif_hypercubes.py
│   └── netcdf_to_tif_test.py
├── LIBS hypercube explorer (netcdf)/
│   ├── LIBS_hypercube_explorer.pyw
│   └── Slider_hypercube.ui
└── README.md   ← you are here
```

* **LIBS Format conversion scripts (beta)** – stand‑alone scripts that convert hyperspectral image stacks between **TIFF ↔ MATLAB `.mat` ↔ NetCDF** formats.  
  > *Tip :* each script defines the *input file name* at the top – simply edit that variable or wrap the logic in your own CLI if you need batch processing.

* **LIBS hypercube explorer (netcdf)** – a small **PyQt5 + Matplotlib GUI** that lets you open a NetCDF hypercube, scroll through wavelength layers with a slider and inspect pixel spectra.

---

## ⚙️ Quick start

### 1. Create a Python environment

```bash
python -m venv venv          # or conda create -n libs-screen python=3.10
source venv/bin/activate     # Windows: venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install numpy scipy xarray h5py tifffile scikit-image                        matplotlib seaborn pandas PyQt5
```

### 2. Run the hypercube explorer

```bash
python "LIBS hypercube explorer (netcdf)/LIBS_hypercube_explorer.pyw"
```

A window will open – use **File → Open** to load your `.nc` hypercube and explore individual wavelength slices.

### 3. Convert data

```bash
# Example: convert a 3‑D TIFF stack called sample.tif to MATLAB .mat
python "LIBS Format conversion scripts (beta)/TIF_to_mat.py"
```

> The conversion scripts are minimal prototypes – open them in a text editor and
> adapt the hard‑coded `filename` / `imstack` variables to your dataset.

---

## 🧰 Dependencies summary

| Package | Why it’s needed |
|---------|-----------------|
| **numpy**, **scipy**, **pandas** | numerical & metadata handling |
| **xarray**, **h5py** | NetCDF / HDF5 hypercube I/O |
| **tifffile**, **scikit‑image** | reading & writing multi‑page TIFF |
| **matplotlib**, **seaborn** | plotting (GUI + notebooks) |
| **PyQt5** | cross‑platform GUI for the explorer |

---

## 🎯 Project scope & future work

* Provide open examples of **format conversion** between the most common LIBS hyperspectral container formats.  
* Offer a **lightweight viewer** for quick QC of NetCDF cubes.  
* ➡ Planned (community help welcome!):
  * add CLI arguments to the conversion scripts  
  * support large cubes with lazy‑loading / dask  
  * export false‑colour RGB composites from the GUI  

---

## 🤝 Consortium

| Institution | Expertise | Main contact |
|-------------|-----------|--------------|
| **Royal Belgian Institute of Natural Sciences – Geological Survey of Belgium (RBINS‑GSB)** | Coordination, field LIBS deployment | Christian Burlet |
| **Université de Mons (UMONS)** | Core LIBS instrumentation & mapping | Jean‑Marc Baele |
| **KU Leuven** | Machine learning & chemometrics | Anca Croitor Sava |
| **Université de Liège (ULiège)** | Engineering & process applications | Eric Pirard |

---

## 🌐 Further information

* Project website – <https://sites.google.com/view/libs-screen/>  
* Final BELSPO report – <https://www.belspo.be/belspo/brain2-be/projects/FinalReports/LIBS-SCReeN_FinRep.pdf>

---
