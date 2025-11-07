# ocr_engine.py
import pandas as pd

def extract_courses_from_image(image_bytes: bytes) -> pd.DataFrame:
    """
    Stub OCR.
    Right now we just return example data so the app always works.
    Replace this function with real OCR later.
    """
    sample = [
        {
            "course_name": "Calculus I",
            "mark": 82,
            "group_avg": 74,
            "group_sd": 7.5,
            "credits": 2.0,
        },
        {
            "course_name": "General Chemistry",
            "mark": 88,
            "group_avg": 76,
            "group_sd": 6.8,
            "credits": 2.0,
        },
        {
            "course_name": "Humanities",
            "mark": 90,
            "group_avg": 80,
            "group_sd": 5.5,
            "credits": 2.0,
        },
    ]
    return pd.DataFrame(sample)
