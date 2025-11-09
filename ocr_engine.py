# ocr_engine.py
import pytesseract
from PIL import Image
import pandas as pd
import io

def extract_courses_from_image(image_bytes: bytes) -> pd.DataFrame:
    """Extract course data from screenshot (approximate OCR)."""
    try:
        img = Image.open(io.BytesIO(image_bytes))
        text = pytesseract.image_to_string(img)

        # Simple text line parsing
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        data = []
        for line in lines:
            parts = line.split()
            nums = [p for p in parts if p.replace('.', '', 1).isdigit()]
            if len(nums) >= 3:
                try:
                    mark, avg, sd = map(float, nums[:3])
                    course_name = " ".join([p for p in parts if p not in nums])
                    data.append({
                        "course_name": course_name or "Unknown",
                        "mark": mark,
                        "group_avg": avg,
                        "group_sd": sd,
                        "credits": 2
                    })
                except ValueError:
                    continue

        if not data:
            return pd.DataFrame(columns=["course_name", "mark", "group_avg", "group_sd", "credits"])

        return pd.DataFrame(data)
    except Exception as e:
        return pd.DataFrame(columns=["course_name", "mark", "group_avg", "group_sd", "credits"])
