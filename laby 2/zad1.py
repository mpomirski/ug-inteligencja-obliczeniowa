# Michał Pomirski 27.02.2024
import pandas as pd

def clean_up_varieties(df: pd.DataFrame) -> pd.DataFrame:
    # Clean up varieties
    mapping: dict[str, str] = {
        'se': "Setosa",
        've': "Versicolor",
        'vi': "Virginica"
    }
    for row in df["variety"]:
        if row not in ["Setosa", "Versicolor", "Virginica"]:
            try:
                df["variety"].replace(row, mapping[row.lower()[:2]])
                print(f"Replaced {row} with {mapping[row.lower()[:2]]}")
            except KeyError:
                df.drop(df[df["variety"] == row].index)
                print(f"Deleted row with {row} variety")
    return df

def clean_up_values(df: pd.DataFrame) -> pd.DataFrame:
    #Drop rows with NaN
    df = df.dropna()

    # Clean up data not between 0 and 15
    for col_name in df.columns:
        median: float | None = df[col_name].median() if df[col_name].dtype == "float64" else None
        for row in df[col_name]:
            try:
                float(row)
            except ValueError:
                break
            if not (0.0 < row < 15.0):
                print(f"Replaced {row} with {median} in {col_name}")
                df[col_name].replace(row, median)

    df = clean_up_varieties(df)

    return df
                

def main():
    na_values: list[str] = ["-", "nan"]
    df: pd.DataFrame  = pd.read_csv("H:\\mpomirski\\4 semestr\\inteligencja obliczeniowa\\laby 2\\iris_with_errors.csv", na_values=na_values)
    print(df.head())
    print("-----------------")
    print("Empty values: ")
    print(df.isnull().sum())
    print("-----------------")
    df = clean_up_values(df)


if __name__ == "__main__":
    main()