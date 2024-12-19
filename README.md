# Forecasting

This project demonstrates a simple business forecasting model using linear regression. The model predicts future sales based on historical sales data.

## Project Structure

- `main.py`: The main script that reads the data, trains the model, and generates predictions.
- `SALEStest.xlsx`: The Excel file containing historical sales data.

## How to Run

1. Install the required dependencies:
    ```sh
    pip install pandas scikit-learn matplotlib
    ```

2. Ensure you have the [SALEStest.xlsx](https://github.com/ryantoby40/Forecasting/blob/main/SALEStest.xlsx) file in the same directory as [main.py](https://github.com/ryantoby40/Forecasting/blob/main/main.py). The file should have columns `Month`, `Year`, and `Sales`. Rows with missing `Sales` values will be used for future predictions.

3. Run the main script:
    ```sh
    python main.py
    ```

## Data Format

The [SALEStest.xlsx]([http://_vscodecontentref_/4](https://github.com/ryantoby40/Forecasting/blob/main/SALEStest.xlsx)) file should have the following columns:
- `Month`: The month of the sales data (either as numbers or abbreviated month names).
- `Year`: The year of the sales data.
- `Sales`: The sales figures. Rows with missing `Sales` values will be used for future predictions.

## Example Data

| Month | Year | Sales |
|-------|------|-------|
| Jan   | 2022 | 200   |
| Feb   | 2022 | 220   |
| Mar   | 2022 | 250   |
| Apr   | 2022 | 270   |
| May   | 2022 | 300   |
| Jun   | 2022 | 320   |
| Jul   | 2022 | 340   |
| Aug   | 2022 | 360   |
| Sep   | 2022 | 380   |
| Oct   | 2022 | 400   |
| Nov   | 2022 | 420   |
| Dec   | 2022 | 450   |
| Jan   | 2023 |       |
| Feb   | 2023 |       |
| Mar   | 2023 |       |

## Output

The script will generate a plot showing:
- Past sales data as red scatter points.
- Predicted sales for the existing data as a blue line.
- Future sales predictions as a green dashed line.
