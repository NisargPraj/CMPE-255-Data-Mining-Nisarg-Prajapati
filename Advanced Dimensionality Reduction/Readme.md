


# **Advanced Dimensionality Reduction Techniques**

## **Introduction**

This repository contains the implementation of various dimensionality reduction techniques as part of a data mining assignment. The objective is to demonstrate and compare different methods used to reduce the dimensionality of datasets, both image and tabular, and to interpret their results. Interactive visualizations are incorporated to enhance the exploration and understanding of the data.

---

## **Datasets Used**

A variety of datasets were used to showcase each dimensionality reduction technique. Efforts were made to use distinct datasets for each method, including medical datasets where possible.

1. **Wine Dataset** - UCI Machine Learning Repository
2. **Two Moons Dataset** - Synthetic Dataset
3. **MNIST Digits Dataset** - Handwritten Digits
4. **Breast Cancer Wisconsin Dataset** - UCI Machine Learning Repository
5. **Fashion-MNIST Dataset** - Zalando's Article Images
6. **Olivetti Faces Dataset** - AT&T Laboratories Cambridge
7. **Swiss Roll Dataset** - Synthetic Dataset
8. **S-Curve Dataset** - Synthetic Dataset
9. **Iris Dataset** - UCI Machine Learning Repository
10. **Pima Indians Diabetes Dataset** - UCI Machine Learning Repository

---

## **Dimensionality Reduction Techniques**

### **1. Randomized PCA**

- **Dataset:** Wine Dataset
- **Description:** An efficient approximation of PCA for large datasets.
- **Notebook Section:** [Randomized PCA on Wine Dataset](https://colab.research.google.com/drive/1QcwvtkllAH1WT57okBWreCO-uMPRgBVo?usp=sharing#scrollTo=2knflH9sBfFA)

### **2. Kernel PCA**

- **Dataset:** Two Moons Dataset
- **Description:** Extends PCA to capture nonlinear structures using kernel methods.
- **Notebook Section:** [Kernel PCA on Two Moons Dataset]((https://colab.research.google.com/drive/1QcwvtkllAH1WT57okBWreCO-uMPRgBVo?usp=sharing#scrollTo=HQ-sHaBOCCHl))

### **3. Incremental PCA**

- **Dataset:** MNIST Digits Dataset
- **Description:** Processes data in batches for large datasets.
- **Notebook Section:** [Incremental PCA on MNIST Digits Dataset](https://colab.research.google.com/drive/1QcwvtkllAH1WT57okBWreCO-uMPRgBVo?usp=sharing#scrollTo=S-MS0FWGCMyR)

### **4. Factor Analysis**

- **Dataset:** Breast Cancer Wisconsin Dataset
- **Description:** Models observed variables as linear combinations of potential factors.
- **Notebook Section:** [Factor Analysis on Breast Cancer Dataset](https://colab.research.google.com/drive/1QcwvtkllAH1WT57okBWreCO-uMPRgBVo?usp=sharing#scrollTo=H_j7SyYICagr)

### **5. t-SNE with Interactive Visualization**

- **Dataset:** Fashion-MNIST Dataset
- **Description:** Visualizes high-dimensional data in 2D or 3D space, preserving local structure.
- **Notebook Section:** [t-SNE on Fashion-MNIST Dataset](https://colab.research.google.com/drive/1QcwvtkllAH1WT57okBWreCO-uMPRgBVo?usp=sharing#scrollTo=6LKsI037ClDz)

### **6. UMAP with Interactive Visualization**

- **Dataset:** Olivetti Faces Dataset
- **Description:** Preserves both local and global structure in data visualization.
- **Notebook Section:** [UMAP on Olivetti Faces Dataset](https://colab.research.google.com/drive/1QcwvtkllAH1WT57okBWreCO-uMPRgBVo?usp=sharing#scrollTo=sXhmJAcXC2bP)

### **7. Isomap**

- **Dataset:** Swiss Roll Dataset
- **Description:** Maintains geodesic distances to capture the underlying manifold.
- **Notebook Section:** [Isomap on Swiss Roll Dataset](https://colab.research.google.com/drive/1QcwvtkllAH1WT57okBWreCO-uMPRgBVo?usp=sharing#scrollTo=CQ7FI77KDBgQ)

### **8. Locally Linear Embedding (LLE)**

- **Dataset:** S-Curve Dataset
- **Description:** Preserves local neighborhood information to unfold manifolds.
- **Notebook Section:** [LLE on S-Curve Dataset](https://colab.research.google.com/drive/1QcwvtkllAH1WT57okBWreCO-uMPRgBVo?usp=sharing#scrollTo=CGwfs7dJDPlv)

### **9. Multidimensional Scaling (MDS)**

- **Dataset:** Iris Dataset
- **Description:** Attempts to preserve pairwise distances between data points.
- **Notebook Section:** [MDS on Iris Dataset](https://colab.research.google.com/drive/1QcwvtkllAH1WT57okBWreCO-uMPRgBVo?usp=sharing#scrollTo=-D56BTsbDZVH)

### **10. Autoencoders**

- **Dataset:** Pima Indians Diabetes Dataset
- **Description:** Neural networks that learn efficient data representations in an unsupervised manner.
- **Notebook Section:** [Autoencoder on Pima Indians Diabetes Dataset](https://colab.research.google.com/drive/1QcwvtkllAH1WT57okBWreCO-uMPRgBVo?usp=sharing#scrollTo=N7xMdWXMDi8S)

---

## **Databricks Implementation**

- **Technique Demonstrated:** PCA (and optionally t-SNE) using PySpark's MLlib
- **Dataset:** Wine Quality Dataset (White Wine)
- **Notebook:** [Databricks Notebook](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/1196590387878783/3824503541987814/7015553223106851/latest.html)
- **Description:** Demonstrated the use of PCA within the Databricks environment using PySpark on the Wine Quality dataset. Interactive visualizations were created using Plotly to interpret the PCA results, and comparisons were made with the implementations in Colab.

---

## **Interactive Visualizations**

Interactive visualizations have been incorporated using Plotly and ipywidgets to enhance data exploration and understanding.

- **t-SNE on Fashion-MNIST Dataset:**
  - Interactive scatter plot with hover information and legend interaction.
  - Slider widget to adjust the perplexity parameter dynamically.

- **UMAP on Olivetti Faces Dataset:**
  - Interactive scatter plot colored by person ID.
  - Widgets to adjust UMAP parameters such as `n_neighbors` and `min_dist`.

- **PCA on Wine Dataset:**
  - Interactive visualization to explore principal components.

- **Autoencoders:**
  - Visualizations of latent space representations with interactivity.

**Note:** Interactive visualizations are embedded in the Colab notebook and require running the notebook in a Jupyter environment that supports interactive widgets.

---

## **Results and Analysis**

The detailed results and analysis for each technique are included in the [Dimensionality_Reduction.ipynb](https://colab.research.google.com/drive/1QcwvtkllAH1WT57okBWreCO-uMPRgBVo?usp=sharing) notebook. Commentary is provided for each technique, discussing:

- The effectiveness of the technique on the chosen dataset.
- Observations about the visualizations and any patterns identified.
- Comparison with other techniques in terms of performance and suitability.
- Interpretation of how well each method preserved the structure of the data.

A comparative analysis summarizing the strengths and weaknesses of each method is included towards the end of the notebook.

---

## **Video Explanation**
[Video](https://youtu.be/gcKR-pJS-Yo)

---
