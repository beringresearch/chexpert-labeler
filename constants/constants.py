from pathlib import Path

# Paths
HOME_DIR = Path.home()
PARSING_MODEL_DIR = HOME_DIR / ".local/share/bllipparser/GENIA+PubMed"

# Observation constants
CARDIOMEGALY = "Cardiomegaly"
ENLARGED_CARDIOMEDIASTINUM = "Enlarged Cardiomediastinum"
SUPPORT_DEVICES = "Support Devices"
NO_FINDING = "No Finding"
OBSERVATION = "observation"
CATEGORIES = ["No Finding", "Abnormal Mediastinal Contour", "Abnormality of Cardiac Contour", "Atelectasis",
"Calcification", "Cardiac Calcification", "Cardiomegaly", "Cavitation", "Chest Wall Deformity", "Chest Wall Mass",
"Colonic Interposition", "Consolidation", "Diffuse Bony Abnormality", "Dislocation", "Effusion", "Emphysema",
"External", "Focal Bony Lesion", "Fracture", "Hiatus Hernia", "Hilar Elevation/Depression", "Hilar Enlargement",
"Increased Hilar Density", "Spport Devices", "Interstitial Opacity", "Lobar Collapse", "Loculated Effusion",
"Mass", "Mass Lesion", "Metalwork", "Neck Mass", "Nodule", "Spinal Deformity", "Perihilar Congestion","Pneumomediastinum",
"Pneumoperitoneum", "Pneumothorax", "Raised Hemidiaphragm", "Spinal Deformity", "Subcutaneous Emphysema", "Thickening",
"Vascular Calcification"]

# Numeric constants
POSITIVE = 1
NEGATIVE = 0
UNCERTAIN = -1

# Misc. constants
UNCERTAINTY = "uncertainty"
NEGATION = "negation"
REPORTS = "Reports"
