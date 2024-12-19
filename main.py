import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def main():
    
    data = pd.read_excel('SALEStest.xlsx')

    if data['Month'].dtype == 'object':
        data['Month'] = data['Month'].apply(month_to_num)

    future_months = data[data['Sales'].isna()]
    future_months['Month_Year'] = future_months['Month'].astype(str) + '-' + future_months['Year'].astype(str)

    data = data.dropna(subset=['Sales'])

    # creating year and month together
    data['Month_Year'] = data['Month'].astype(str) + '-' + data['Year'].astype(str)

    X = data[['Month', 'Year']]
    y = data['Sales']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    model = LinearRegression()
    model.fit(X_train, y_train)

    future_sales_pred = model.predict(future_months[['Month', 'Year']])

    plt.figure(figsize=(10, 6))
    plt.scatter(data['Month_Year'], data['Sales'], color='red', label='Past Sales')
    plt.plot(future_months['Month_Year'], future_sales_pred, color='green', linestyle='dashed', label='Future Sales')
    plt.plot(data['Month_Year'], model.predict(X), color='blue', label='Regression Line')
    plt.xticks(rotation=45)
    plt.xlabel('Month-Year')
    plt.ylabel('Sales')
    plt.title('Sample Sales Business Forecasting')
    plt.legend()
    plt.tight_layout()
    plt.show()

def month_to_num(month):
    months = {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12
    }
    return months[month]

if __name__ == '__main__':
    main()