# MMEPL-CSC: A Hybrid Ensemble-Based Parallel Learning Framework for Multi-Omics Data Integration and Cancer Subtype Classification

## 🔬 Overview
MMEPL-CSC (Multimodal Ensemble Parallel Learning for Cancer Subtype Classification) is a deep learning and machine learning hybrid framework for multi-omics data integration and robust cancer subtype classification. The framework uses parallel processing, multimodal autoencoders, ensemble learning, and optimization via a hybrid Backpropagation–Particle Swarm Optimization (PSO) strategy.

---

## 📄 Abstract
Integrating multi-omics data to understand biological processes in human diseases is a complex bioinformatic task. Machine learning (ML), particularly deep learning (DL), offers a promising approach but is often limited by naïve data concatenation, single-model architectures, and inefficient optimization methods. 

This framework addresses these challenges by:
- Using multimodal autoencoders for feature extraction across different omics layers
- Combining multiple DL and ML models in a two-layer ensemble architecture
- Applying PSO for better optimization
- Executing all tasks in a parallelized environment to improve computational efficiency

Tested on TCGA Pan-cancer and TCGA BRCA datasets, MMEPL-CSC achieves 89.51% and 90.9% accuracy, respectively, and delivers speed-ups of 3x and 2.5x via parallel computing.

---

## 🧪 Experimental Setup
- **Base models (L0):** 5 DNNs
- **Meta-model (L1):** 8 learners (DNN, RF, DT, KNN, XGB)
- **Optimization:** Hybrid Backpropagation + PSO
- **Training/Test Split:** 4:1
- **Repetitions:** 10 times (average reported)
- **Environment:** Python + Ray, Ubuntu 22.04, Intel i7, 4GB & 8GB RAM machines
- **Performance Metrics:** Accuracy, Precision, Recall, F1-score, Speed-up, Percentage Improvement (PI)

---

## 📊 Datasets
### TCGA Pan-Cancer
- RPPA and miRNA data
- 6241 samples with matched omics and molecular labels
- Source:
  - https://xenabrowser.net/
  - https://tcpaportal.org/tcpa/

### TCGA-BRCA
- RNA-seq (transcriptomics)
- CNV (genomics)
- Labels from UCSC Xena

---

## 📁 Repository Contents
- `notebooks/`: Jupyter notebooks for model training, optimization, and evaluation
- `data/`: Scripts for dataset preprocessing and formatting
- `results/`: Sample output files and logs
- `README.md`: Overview and setup instructions
- `requirements.txt`: Python dependencies

---

## ⚙️ Installation & Requirements
To run the framework, make sure you have Python 3.7+ installed. Then install the required libraries:

```bash
pip install -r requirements.txt
```

### Key Dependencies:
- `tensorflow` (for deep learning models)
- `scikit-learn` (for machine learning algorithms)
- `ray` (for parallel processing)
- `numpy`, `pandas`, `matplotlib`, and other common scientific libraries

---

## 🚀 Running the Code
Open the Jupyter notebook inside the `notebooks/` directory and follow the execution cells step by step. Make sure dataset paths are updated accordingly in your environment.

To launch Jupyter:
```bash
jupyter notebook
```
