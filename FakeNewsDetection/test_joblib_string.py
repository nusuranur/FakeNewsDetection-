import joblib
import string

# Test joblib
dummy_data = {"test": 123}
joblib.dump(dummy_data, "test_model.pkl")
loaded_data = joblib.load("test_model.pkl")
print("Joblib test:", loaded_data)

# Test string
print("String test:", string.ascii_lowercase)
