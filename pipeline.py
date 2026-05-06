import joblib
pipeline_data = joblib.load("preprocessing/preprocessing_pipeline.pkl")
print(type(pipeline_data))
if isinstance(pipeline_data, dict):
    print("Keys found:", pipeline_data.keys())