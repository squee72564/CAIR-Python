# CAIR-Python
Content Aware Image Resizing in Python

Made using lessons from "Fundamentals of Dynamic Programming", a linkedin learning lesson made by Avik Das.

Das, Avik (2020). _Fundamentals of Dynamic Programming_ [Video]. LinkedIn.
	https://www.linkedin.com/learning/fundamentals-of-dynamic-programming

You can use the scripts in the `src` folder to create the images below.

`python energy.py <input_file> <output_file>` will give you the heatmap of the image.

`python seam.py <input_file> <output_file>` will give you the lowest energy seam in the image.

`python carve.py <input_file> <num_iterations> <output_file>` will remove `<num_iterations>` lowest vertical
seams from the image. 


Original picture:
<p align="center">
	<img src="/img/surfer.jpg">
</p>

Example of energy heatmap:
<p align="center">
	<img src="/img/surfer_energy.jpg">
</p>

Example of lowest energy seam visualized:
<p align="center">
	<img src="/img/surfer_seam.jpg">
</p>

End result of 200 lowest energy seams removed:
<p align="center">
	<img src="/img/surfer_200_resized.png">
</p>
