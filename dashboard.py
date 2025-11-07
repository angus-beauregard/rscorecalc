import re
import pandas as pd

def normalize_col_name(raw: str) -> str:
    """
    Turn whatever the user typed in the CSV header into one of:
    - course_name
    - mark
    - group_avg
    - group_sd
    - credits
    Super forgiving: ignores case, dots, dashes, extra words like 'your', 'class'.
    """
    s = raw.strip().lower()
    # remove dots and underscores
    s = s.replace(".", " ").replace("_", " ").replace("-", " ")
    # compress spaces
    s = " ".join(s.split())

    # course name-ish
    if any(k in s for k in ["course", "class name", "subject"]) or s in ["class"]:
        return "course_name"

    # mark / grade
    if "grade" in s or "mark" in s or "note" in s or "result" in s or "score" in s:
        return "mark"

    # average
    if "avg" in s or "average" in s or "class avg" in s or "group avg" in s:
        return "group_avg"

    # standard deviation
    if "std" in s or "sd" in s or "standard" in s or "écart" in s or "ecart" in s:
        return "group_sd"

    # credits
    if "credit" in s or "unit" in s or "unité" in s or "unites" in s:
        return "credits"

    # default: return cleaned string
    return s


def coerce_csv_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename whatever columns the user sent to our internal names.
    Doesn't care about order. Raises a clear error if we still can't match.
    """
    # first pass: normalize all column names
    col_map = {col: normalize_col_name(col) for col in df.columns}
    df = df.rename(columns=col_map)

    needed = ["course_name", "mark", "group_avg", "group_sd", "credits"]
    missing = [c for c in needed if c not in df.columns]

    if missing:
        # try a second pass: maybe user didn't give credits -> fill with 1
        if "credits" in missing:
            df["credits"] = 1
            missing.remove("credits")

    if missing:
        raise ValueError(
            f"CSV is missing these columns even after normalization: {missing}. "
            "We accept headers like: Course Name, Your Grade, Class Avg, Std. Dev, Credits."
        )

    # return only the columns we need, in the order we want
    return df[needed]
