
# LIBS‑SCReeN

**Screening raw materials from exploration to (post-)beneficiation using LIBS techniques**  
_BELSPO BRAIN-be 2.0 – B2/191/P1/LIBS‑SCReeN (2020–2024)_

A collection of Python scripts, notebooks and tools developed to process LIBS spectra and hyperspectral imaging data, aimed at robust elemental screening across multiple scales.

---

## 📌 Consortium

The LIBS‑SCReeN project is driven by a strong collaboration between Belgian universities and research institutes:

| Institution | Role / Expertise | Key Contacts |
|-------------|------------------|--------------|
| **Royal Belgian Institute of Natural Sciences – Geological Survey of Belgium (RBINS‑GSB)** | Coordination and LIBS instrumentation |  Christian Burlet |
| **Université de Mons (UMONS)** | Core LIBS instrumentation and mapping workflows | Jean‑Marc Baele |
| **Katholieke Universiteit Leuven (KU Leuven)** | Machine learning & chemometrics | Anca Croitor Sava |
| **Université de Liège (ULiège)** | Environmental engineering & core LIBS setup | Eric Pirard |

- Project site: https://sites.google.com/view/libs-screen/

---

## 🛠 Repository Structure

```


````

---

## ⚙️ Getting Started

### Requirements

- Python 3.8+  
- Dependencies: `numpy`, `scipy`, `pandas`, `matplotlib`, `netCDF4`, `xarray`, etc.

### Installation

```bash
git clone https://github.com/Niphargusproject/LIBS-SCReeN.git
cd LIBS-SCReeN
pip install -r requirements.txt
````

---

## 🚀 Usage

Use the scripts and notebooks to:

* **Convert** raw LIBS files (CSV, netCDF, TIFF).
* **Process** LIBS hyperspectral cubes interactively.
* **Extract** elemental peaks and generate concentration maps.
* **Visualize** results via notebooks and plotting modules.

---

## 📚 Examples & Tutorials

See `notebooks/` for workflows covering raw data ingestion to final analysis.
Scripts in `scripts/` can be used standalone or embedded into pipelines.

---

## 📖 References

* Project summary & description on Belgium’s natural sciences institute site ([sites.google.com][4], [belspo.be][2], [naturalsciences.be][3])
* Partner and context details from Belspo PDF documentation ([belspo.be][1])


[1]: https://www.belspo.be/belspo/brain2-be/projects/LIBS-SCReeN_E.pdf "[PDF] LIBS-SCReeN - Belspo"
[2]: https://www.belspo.be/belspo/brain2-be/projects/FinalReports/LIBS-SCReeN_FinRep.pdf "[PDF] LIBS-SCReeN - Belspo"
[3]: https://www.naturalsciences.be/en/science/research/geosciences-for-a-sustainable-society/projects/libs-screen "LIBS-SCReeN | Institute of Natural Sciences"
[4]: https://sites.google.com/view/libs-screen/ "LIBS-SCReeN"


