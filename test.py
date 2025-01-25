import os
from nmco.utils.run_nuclear_feature_extraction import run_nuclear_chromatin_feat_ext

# Get current directory
current_dir = os.getcwd()

# Point to example data that should be in the repository
raw_image_path = os.path.join(current_dir, 'example_data/raw_image.tif')
labelled_image_path = os.path.join(current_dir, 'example_data/nuc_labels.tif')
feature_path = os.path.join(current_dir, 'example_data/')

# Extract features
features = run_nuclear_chromatin_feat_ext(raw_image_path, labelled_image_path, feature_path)

# Print first few features to verify
print("Extracted features:", features.head())