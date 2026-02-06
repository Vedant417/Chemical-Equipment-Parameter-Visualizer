import pandas as pd


def analyze_equipment_csv(csv_file):
    """
    Reads equipment CSV file and returns summary statistics + records
    """

    df = pd.read_csv(csv_file)

    required_columns = {
        "Equipment Name",
        "Type",
        "Flowrate",
        "Pressure",
        "Temperature",
    }

    if not required_columns.issubset(set(df.columns)):
        raise ValueError("CSV file is missing required columns")

    summary = {
        "total_equipment": len(df),
        "avg_flowrate": round(df["Flowrate"].mean(), 2),
        "avg_pressure": round(df["Pressure"].mean(), 2),
        "avg_temperature": round(df["Temperature"].mean(), 2),
        "type_distribution": df["Type"].value_counts().to_dict(),
        "records": df.to_dict(orient="records"),
    }

    return summary