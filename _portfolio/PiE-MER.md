---

title: "PiE-MER: Multimodal Evaluation Pipeline for Mathematical Expression Recognition"

excerpt: "A comprehensive evaluation framework for printed mathematical expression recognition using multiple modalities: LaTeX, MathML, Label Graphs, and visual representations <br/><img src='/images/PIEMER/convGTv3.png' width='60%' height='auto'/>"

collection: portfolio

---



## A Multimodal Evaluation Pipeline for Mathematical Expression Recognition

The PiE-MER (Pipeline for Evaluation of Mathematical Expression Recognition) framework is part of the paper *A Multimodal Evaluation Pipeline for Mathematical Expression Recognition: Comparisons of Datasets, Metrics, and Models*, presented at ICDAR 2025. This evaluation pipeline provides a comprehensive methodology for assessing mathematical OCR systems using multiple complementary representations.

### The Problem with Current Evaluation Methods

Most Mathematical Expression Recognition (MER) systems are evaluated using traditional metrics like BLEU and Levenshtein distance on LaTeX strings alone. However, this approach suffers from **polymorphic ambiguity**, where different LaTeX expressions render identically (e.g., `x^{2}_{i}` and `x_i^2` both produce x²ᵢ) but are considered incorrect by string-based metrics. Additionally, evaluations typically focus only on syntactic accuracy, neglecting semantic correctness and visual fidelity.

![Figure 1: The PiE-MER evaluation pipeline](/images/PIEMER/pipeline_trans-1.png) 
*Complete conversion pipeline from raw dataset to multiple evaluation modalities*


## PiE-MER Architecture

PiE-MER evaluates mathematical expression recognition systems through a unified pipeline. Input images are first rescaled to match each model's expected training resolution before OCR inference. Ground-truth and predicted expressions are then converted into four complementary representations, allowing multiple evaluation metrics to be computed and compared.

The framework evaluates four modalities. **LaTeX** measures syntactic similarity using Levenshtein distance, BLEU, and Exact Match. **MathML**, generated with LaTeXML, provides a more consistent structural representation by reducing LaTeX polymorphic ambiguity. **Label Graphs**, extracted with LgEval ([LgEval](https://gitlab.com/dprl/lgeval)), capture the structural relationships between mathematical symbols. Finally, the **Visual Representation** compares normalized rendered images using Image Levenshtein, Pixel Difference Ratio, and Visual Exact Match to assess visual fidelity of the recognized expression.

![Figure 2: Sample conversion process](/images/PIEMER/convGTv3.png)
*Converting a single mathematical expression into all four modalities.*

## Results

Correlation analysis shows that Image Levenshtein (0.78) and LaTeX Levenshtein (0.52) are the metrics most strongly associated with overall model accuracy, while BLEU scores exhibit much weaker correlations (<0.40). The experiments also confirm that parsing and normalization, particularly through MathML, improve evaluation consistency by reducing representation ambiguity. More generally, combining visual and structural metrics provides a more reliable assessment than any single metric alone. The benchmark further highlights important differences in cross-dataset generalization, with models such as MathNet remaining robust across multiple datasets, and shows that image resolution and DPI rescaling have a significant impact on OCR performance.

![Figure 3: Performance heatmap](/images/PIEMER/heatmap_all_v12.png)
*Model performance across all datasets and metrics. Darker cells indicate better performance.*

### Recommended Metrics

Based on our correlation analysis, we recommend:

| Evaluation Goal | Primary Metrics | Secondary Metrics |
|-----------------|-----------------|-------------------|
| **Overall Quality** | Image Levenshtein, LaTeX Levenshtein | – |
| **Visual Similarity** | Image Levenshtein, Pixel Difference | Visual Exact Match |
| **Syntactic Accuracy** | LaTeX Levenshtein, ∆E_symlg | Exact Match |
| **Semantic Accuracy** | ∆E_symlg, MathML Levenshtein | MathML BLEU |



## Links and references

PiE-MER is available as open-source software on GitHub, enabling researchers to evaluate their own MER models and datasets. For more information, please see:

- **Full Paper**: [https://hal.science/hal-05172571](https://hal.science/hal-05172571)
- **PiE-MER GitHub**: [https://github.com/fwieckowiak/PiE-MER](https://github.com/fwieckowiak/PiE-MER)


```bibtex
@InProceedings{10.1007/978-3-032-04627-7_7,
author="Wieckowiak, Fran{\c{c}}ois
and Eglin, V{\'e}ronique
and Bonnet, Tony
and Bres, St{\'e}phane
and Rousseau, La{\"e}titia",
editor="Yin, Xu-Cheng
and Karatzas, Dimosthenis
and Lopresti, Daniel",
title="A Multimodal Evaluation Pipeline for Mathematical Expression Recognition: Comparisons of Datasets, Metrics, and Models",
booktitle="Document Analysis and Recognition --  ICDAR 2025",
year="2026",
publisher="Springer Nature Switzerland",
address="Cham",
pages="120--136",
isbn="978-3-032-04627-7"
}


```



## Funding & Acknowledgments

This work was carried out as part of a CIFRE PhD in collaboration between:
- **LIRIS** (Laboratoire d'Informatique en Image et Systèmes d'information, CNRS)
- **Luminess** (Industry partner)

CIFRE grant no. 2023/0356

---