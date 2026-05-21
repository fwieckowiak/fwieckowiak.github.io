---
title: "PatentME datasets"
excerpt: "Short description of portfolio item number 1<br/><img src='/images/500x300.png'>"
collection: portfolio
---

The PatentME datasets are part of the paper *PatentME: A Dataset and Reference-Free Post-OCR Verification Task for Printed Mathematical Expression Recognition*, accepted for publication at the ICDAR 2026 conference. The datasets consist of images of mathematical expressions extracted from patent documents of the European Patent Office (EPO), along with their corresponding ground truth annotations in MathML. 

Most of the mathematical expression datasets get their data from scientific publications on arXiv. They scan through the LaTeX files to extract the mathematical expressions, and render them in high quality. This is not the case for our datasets which are of real scanned documents associated with a MathML ground truth that is human validated.

In the process of patent publication, the original documents are scanned using Optical Character Recognition (OCR) systems as well as human annotators to extract the textual and mathematical content. OCR systems often struggle with accurately recognizing mathematical expressions due to their complex structure and diverse notations. Also, patent applications documents can be very heterogeneous in terms of formatting and quality, as you can see in Figure 1.

| ![Figure 1: Sample math expressions with varying quality and fonts](/images/PatentME/example_patentOCR.png) |
|:--:|
| *Figure 1: Sample math expressionsexpressions with varying quality and fonts* |


## PatentME-OCR Dataset


The PatentME-OCR dataset is composed of 40,955 images of mathematical expressions extracted from patent documents (*PatentME-OCR_raw_img*), along with their corresponding MathML annotations (*PatentME-OCR_mml*). We also included a "cleaned" version of the MathML (*PatentME-OCR_mml_cleaned*) where we normalize whitespace, standardize special characters, and replace deprecated MathML tags such as `<fenced>` with their modern equivalents, and finally the rendering of the cleaned MathML in both display and inline modes (*PatentME-OCR_mml_cleaned_display_img* and *PatentME-OCR_mml_cleaned_inline_img*).

The mathematical expressions are extracted from this EPO service : [https://data.epo.org/expert-services/](https://data.epo.org/expert-services/), using this Application Number request : [files/patent_numbers_query.txt](files/patent_numbers_query.txt)

We would recommend future work to instead use this source :  [https://publication-bdds.apps.epo.org/raw-data/products/public/product/32](https://publication-bdds.apps.epo.org/raw-data/products/public/product/32)



It is available on Zenodo for you to evaluate and train your mathematical expression recognition systems on real patent data, and to contribute to the improvement of OCR systems for patent publication and accessibility. I appreciate any feedback or suggestions for future work on this dataset, especially if you find a way to generate trustworthy LaTeX equivalent of the MathML annotations, which would be a great addition to the dataset. There may be annotation errors in the dataset, so please report any issues you find to help us improve the quality of the data.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

[**Download PatentME Dataset on Zenodo**](https://zenodo.org/search?q=PatentME){: .btn .btn--primary .btn--large}



A new version of this dataset, that include more expressions from all the patent applications of the year 2025 is currently in preparation, and will be released in the next few months. Stay tuned for updates!


## PatentME-Siamese Dataset

The Siamese dataset is composed of pairs of images of mathematical expressions. I ran the texteller (link) model on the PatentME-OCR dataset to generate and evaluated its accuracy. Then, I selected the pairs of images (raw image from the patent and the rendered prediction) where the model made an incorrect prediction (negative pairs) and the corresponding "correct" rendered image (from *PatentME-OCR_mml_cleaned_display_img*) paired with the patent image (positive pairs).

Using them, I trained a model to guess, when given the raw image and the prediction image, wheter the predictions is an exact match or not. The data acquisition process and the siamese model are detailed in figure 2 and 3:
| ![Figure 2: Data acquisition process for PatentME-Siamese dataset](/images/PatentME/good_snn-1.png) |
|:--:|
| *Figure 2: Data acquisition process for PatentME-Siamese dataset* |

| ![Figure 3: Siamese neural network architecture](/images/PatentME/snngoodv2-1.png) |
|:--:|

