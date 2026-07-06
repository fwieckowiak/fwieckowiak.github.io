---
title: "PatentME datasets"
excerpt: "Mathematical Expressions from Patent Documents <br/><img src='/images/PatentME/ex_ME_2.png'/>"
collection: portfolio
---

The PatentME datasets are part of the paper *PatentME: A Dataset and Reference-Free Post-OCR Verification Task for Printed Mathematical Expression Recognition*, accepted for publication at the ICDAR 2026 conference. The datasets consist of images of mathematical expressions extracted from patent documents of the European Patent Office (EPO), along with their corresponding ground truth annotations in MathML. 

Most of the mathematical expression datasets get their data from scientific publications on arXiv. They scan through the LaTeX files to extract the mathematical expressions, and render them in high quality. This is not the case for our datasets which are of real scanned documents associated with a MathML ground truth that is human validated.

In the process of patent publication, the original documents are scanned using Optical Character Recognition (OCR) systems as well as human annotators to extract the textual and mathematical content. OCR systems often struggle with accurately recognizing mathematical expressions due to their complex structure and diverse notations. Also, patent applications documents can be very heterogeneous in terms of formatting and quality, as you can see in Figure 1.

| ![Figure 1: Sample math expressions with varying quality and fonts](/images/PatentME/ex_ME_2.png) |
|:--:|
| *Figure 1: Sample math expressions with varying quality and fonts found in patent documents* |


## PatentME-OCR Dataset
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20446086.svg)](https://doi.org/10.5281/zenodo.20446086)
| ![PatentME-OCR Logo](/images/PatentME/patentmeocr_logo.png) |
|:--:|


The PatentME-OCR dataset is composed of 40,000 images of mathematical expressions extracted from patent documents (*PatentME-OCR_raw_img*), along with their corresponding MathML annotations (*PatentME-OCR_mml*). We also included a "cleaned" version of the MathML (*PatentME-OCR_mml_cleaned*) where we normalize whitespace, standardize special characters, and replace deprecated MathML tags such as `<fenced>` with their modern equivalents, and finally the rendering of the cleaned MathML in both display and inline modes (*PatentME-OCR_mml_cleaned_display_img* and *PatentME-OCR_mml_cleaned_inline_img*).

The mathematical expressions are extracted from this EPO service : [https://data.epo.org/expert-services/](https://data.epo.org/expert-services/).

New : We would recommend future work to instead use this source :  [https://publication-bdds.apps.epo.org/raw-data/products/public/product/32](https://publication-bdds.apps.epo.org/raw-data/products/public/product/32)



It is available on Zenodo for you to evaluate and train your mathematical expression recognition systems on real patent data, and to contribute to the improvement of OCR systems for patent publication and accessibility. I appreciate any feedback or suggestions for future work on this dataset, especially if you find a way to generate trustworthy LaTeX equivalent of the MathML annotations, which would be a great addition to the dataset. There may be annotation errors in the dataset, so please report any issues you find to help us improve the quality of the data.

<!--[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX) -->

[**Download on Zenodo**](https://doi.org/10.5281/zenodo.20446086){: .btn .btn--primary .btn--large}


## PatentME-Siamese Dataset
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20446086.svg)](https://doi.org/10.5281/zenodo.20446086)
| ![PatentME-Siamese Logo](/images/PatentME/patentmesiamese_logo.png) |
|:--:|

The Siamese dataset is composed of pairs of images of mathematical expressions. I ran the texteller (link) model on the PatentME-OCR dataset to generate and evaluated its accuracy. Then, I selected the pairs of images (raw image from the patent and the rendered prediction) where the model made an incorrect prediction (negative pairs) and the corresponding "correct" rendered image (from *PatentME-OCR_mml_cleaned_display_img*) paired with the patent image (positive pairs).

Using them, I trained a model to guess, when given the raw image and the prediction image, wheter the predictions is an exact match or not. The data acquisition process and the siamese model are detailed in figure 2 and 3. You can find more about this model in our paper : PatentME : A Dataset and Reference-Free Post-OCR Verification Task for Printed Mathematical Expression Recognition, accepted at the ICDAR 2026 conference !

| ![Figure 2: Data acquisition process for PatentME-Siamese dataset](/images/PatentME/good_snn-1.png) |
|:--:|
| *Figure 2: Data acquisition process for PatentME-Siamese dataset* |

| ![Figure 3: Siamese neural network architecture](/images/PatentME/snngoodv2-1.png) |
|:--:|
| *Figure 3: Siamese neural network architecture* |

The PatentME-Siamese dataset is also available on Zenodo for you to train on this post-OCR verification task.

[**Download on Zenodo**](https://doi.org/10.5281/zenodo.20446086){: .btn .btn--primary .btn--large}


## NEW : PatentME-600k Dataset
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20446086.svg)](https://doi.org/10.5281/zenodo.20446086)
| ![PatentME-600k Logo](/images/PatentME/patentme600k_logo.png) |
|:--:|

After the initial ICDAR paper subbmission, i kept working on data extraction from the EPO website, and used this webpage [https://publication-bdds.apps.epo.org/raw-data/products/public/product/32](https://publication-bdds.apps.epo.org/raw-data/products/public/product/32) to extract more mathematical expressions from all the patent applications of the year 2025. This new version of the dataset, called PatentME-600k, contains  600,000 images of mathematical expressions extracted from around 60,000 patent documents, along with their corresponding MathML annotations. It contains the same kind of data as PatentME-OCR, which I will keep on this page for reference, but if you plan on training large vision models on mathematical expression recognition, I would recommend using the new PatentME-600k dataset which is much larger and more diverse. 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20446086.svg)](https://doi.org/10.5281/zenodo.20446086)

[**Download on Zenodo**](https://doi.org/10.5281/zenodo.20446086){: .btn .btn--primary .btn--large}

## Data Acquisition

You can check our GitHub repo https://github.com/fwieckowiak/PatentME for more details on the data acquisition process.