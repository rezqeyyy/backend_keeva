import joblib
import os

path = "preprocessing/preprocessing_pipeline.pkl"
print(f"File exists: {os.path.exists(path)}")
print(f"File size: {os.path.getsize(path)} bytes")

data = joblib.load(path)
print(f"Type: {type(data)}")

if isinstance(data, dict):
    print(f"Keys: {list(data.keys())}")
    for key, value in data.items():
        print(f"  key='{key}' | type={type(value).__name__} | has_transform={hasattr(value, 'transform')} | has_predict_proba={hasattr(value, 'predict_proba')}")
else:
    print(f"Bukan dict")
    print(f"has_transform: {hasattr(data, 'transform')}")
    print(f"has_predict_proba: {hasattr(data, 'predict_proba')}")
    print(f"Attributes: {[a for a in dir(data) if not a.startswith('_')]}")