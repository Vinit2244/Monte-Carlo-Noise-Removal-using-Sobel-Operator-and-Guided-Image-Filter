# Monte-Carlo-Noise-Removal-using-Sobel-Operator-and-Guided-Image-Filter

Digital Image Processing Course Project (B.Tech. 5th Semester - IIIT Hyderabad)

Team Members:

- Vinit Mehta: 2022111001
- Pearl Shah: 2022102073

This project replicates the implementation of the following research paper:

> Liu, Yu & Zheng, Changwen & Zheng, Quan & Yuan, Hongliang. (2018). Removing Monte Carlo noise using a Sobel operator and a guided image filter. The Visual Computer. 34. 10.1007/s00371-017-1363-z. In this study, a novel adaptive rendering approach is proposed to remove Monte Carlo noise while preserving image details through a feature-based reconstruction. First, noise in the additional features is removed using a guided image filter that reduces the impact of noisy features involving strong motion blur or depth of field. The Sobel operator is then employed to recognize the geometric structures by robustly computing a gradient buffer for each feature. Given the gradient information for high-dimensional features, we compute the optimal filter parameters using a data-driven method. Finally, an error analysis is derived through a two-step smoothing strategy to produce a smooth image and guide the adaptive sampling process. Experimental results indicate that our approach outperforms state-of-the-art methods in terms of visual image quality and numerical error.

## Repository Directory Structure

```text
📦 Monte-Carlo-Noise-Removal-using-Sobel-Operator-and-Guided-Image-Filter
├── 📁 media/
│   ├── 📁 input/
│   │   ├── 📁 cuboids/
│   │   │   ├── 📄 10.png
│   │   │   ├── 📄 100.png
│   │   │   ├── 📄 1000.png
│   │   │   ├── 📄 BW_10.png
│   │   │   ├── 📄 BW_100.png
│   │   │   ├── 📄 BW_1000.png
│   │   │   ├── 📄 depth.png
│   │   │   ├── 📄 normal.png
│   │   │   └── 📄 texture.png
│   ├── 📁 output/
│   │   ├── 📄 alpha_heatmap10.png
│   │   ├── 📄 alpha_heatmap100.png
│   │   ├── 📄 alpha_heatmap1000.png
│   │   ├── 📄 feature_choice_10.png
│   │   ├── 📄 feature_choice_100.png
│   │   ├── 📄 feature_choice_1000.png
│   │   ├── 📄 filtered_10.png
│   │   ├── 📄 filtered_100.png
│   │   ├── 📄 filtered_1000.png
│   │   ├── 📄 filtered_depth_map_10.png
│   │   ├── 📄 filtered_depth_map_100.png
│   │   ├── 📄 filtered_depth_map_1000.png
│   │   ├── 📄 filtered_normal_map_10.png
│   │   ├── 📄 filtered_normal_map_100.png
│   │   ├── 📄 filtered_normal_map_1000.png
│   │   ├── 📄 filtered_texture_map_10.png
│   │   ├── 📄 filtered_texture_map_100.png
│   │   ├── 📄 filtered_texture_map_1000.png
│   │   ├── 📄 gradient_map_10.png
│   │   ├── 📄 gradient_map_100.png
│   │   └── 📄 gradient_map_1000.png
├── 📁 src/
│   ├── 📄 alpha_value.txt
│   └── 📄 main.ipynb
├── 📁 docs/
│   ├── 📄 Proposal.pdf
│   ├── 📄 Presentation.pdf
│   ├── 📄 Report.pdf
│   └── 📄 Research_Paper.pdf
├── 📄 .gitignore
└── 📄 README.md
```

## Assumptions and Specifications

- All the image processing is done on RGB channeled image (if colored) and the datatype of image array is np.int32 in range [0, 255]
