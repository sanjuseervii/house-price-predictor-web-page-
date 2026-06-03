import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import math

data='train.csv'
df=pd.read_csv(data)
print(df.head())
print(df.info())

#taking the neccessary columns 
print(df.columns)
selected_columns = [
    'GrLivArea', 'OverallQual', 'GarageCars', 'GarageArea', 'TotalBsmtSF', 
    '1stFlrSF', 'FullBath', 'TotRmsAbvGrd', 'YearBuilt', 'YearRemodAdd',
    'Neighborhood', 'ExterQual', 'KitchenQual', 'BsmtQual', 'GarageFinish', 
    'Foundation', 'MSZoning', 'CentralAir', 'FireplaceQu', 'HouseStyle',
    'SalePrice' # Yeh tumhara target variable (y) hai
]

# Naya dataframe filter kar lo
df_filtered = df[selected_columns]

print("Naw data shape:", df_filtered.shape)
print("Missing values in filtered data:")
print(df_filtered.isnull().sum())
# 1. replace missing values with none because it indicates the absence of a feature (like no fireplace)
df_filtered['FireplaceQu'] = df_filtered['FireplaceQu'].fillna('None')
df_filtered['GarageFinish'] = df_filtered['GarageFinish'].fillna('None')
df_filtered['BsmtQual'] = df_filtered['BsmtQual'].fillna('None')
print("Missing values:")
print(df_filtered.isnull().sum())
print(df_filtered.info())
numeric_cols = df_filtered.select_dtypes(include=['number']).columns
numeric_cols = [col for col in numeric_cols if col != 'SalePrice']
num_plots = len(numeric_cols)
num_cols = 3  # Ek line mein 3 plots dikhenge
num_rows = math.ceil(num_plots / num_cols)  # Rows calculate karna

# # 3. Canvas size bade rakhna taaki khichdi na bane
# fig, axes = plt.subplots(num_rows, num_cols, figsize=(18, num_rows * 4))
# axes = axes.flatten()  # 2D array ko 1D banana taaki loop aasan ho sake

# # 4. Loop chala kar ek hi canvas par saare plots chhapna
# for i, col in enumerate(numeric_cols):
#     sns.scatterplot(data=df_filtered, x=col, y='SalePrice', ax=axes[i], color='royalblue', alpha=0.7)
#     axes[i].set_title(f'{col} vs SalePrice', fontsize=12)
#     axes[i].set_xlabel(col, fontsize=10)
#     axes[i].set_ylabel('SalePrice', fontsize=10)
#     axes[i].grid(True, linestyle='--', alpha=0.6)

# # 5. Jo khali dabba (extra subplots) bach jayein, unhe chhupa do
# for j in range(i + 1, len(axes)):
#     fig.delaxes(axes[j])

# # Layout ko set karna taaki titles aapas mein takrayein nahi
# plt.tight_layout()
# plt.show()

print("--- Outlier Detection Report ---")

# 2. Har ek numeric column par loop chalao
for col in numeric_cols:
    # Q1 (25th percentile) aur Q3 (75th percentile) nikalna
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    
    # IQR (Interquartile Range) calculate karna
    IQR = Q3 - Q1
    
    # Limit set karna (Standard rule: 1.5 * IQR)
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Is range ke bahar wale data points dhoondhna
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    
    # Result print karna
    print(f"Column: {col:<15} | Total Outliers: {len(outliers)}")
    df_clean = df_filtered[(df_filtered[col] >= lower_bound) & (df_filtered[col] <= upper_bound)]
    print("Outliers removed successfully")

numeric_cols = df_clean.select_dtypes(include=['number']).columns

# # 2. Grid (Subplots) ki setting (`math.ceil` aur `enumerate` ka fir se jalwa)
# num_plots = len(numeric_cols)
# num_cols = 3
# num_rows = math.ceil(num_plots / num_cols)

# # 3. Canvas taiyar karna
# fig, axes = plt.subplots(num_rows, num_cols, figsize=(18, num_rows * 4))
# axes = axes.flatten()

# # 4. Loop chala kar har column ka Histogram aur Density Curve banana
# for i, col in enumerate(numeric_cols):
#     # sns.histplot mein kde=True likhne se histogram ke upar frequency polygon (smooth line) apne aap ban jati hai
#     sns.histplot(data=df_clean, x=col, kde=True, ax=axes[i], color='teal', bins=30)
#     axes[i].set_title(f'Distribution of {col}', fontsize=12)
#     axes[i].set_xlabel(col, fontsize=10)
#     axes[i].set_ylabel('Count / Density', fontsize=10)

# # 5. Extra khali dabbe delete karna
# for j in range(i + 1, len(axes)):
#     fig.delaxes(axes[j])

# plt.tight_layout()
# plt.show()
# #converting the target variable to log scale to reduce skewness
# df_clean['SalePrice'] = np.log1p(df_clean['SalePrice'])
# sns.histplot(df_clean['SalePrice'], kde=True, color='teal')
# plt.title('New Normal Distribution of SalePrice')
# plt.show()
# fig, axes = plt.subplots(num_rows, num_cols, figsize=(18, num_rows * 4))
# axes = axes.flatten()
# #exploring the categorical variables
# categorical_cols = df_clean.select_dtypes(include=['object']).columns
# # Loop chala kar har categorical column ka bar plot banana
# for i, col in enumerate(categorical_cols):
#     # sns.countplot apne aap har category ki frequency (count) ginte hain
#     sns.countplot(data=df_clean, x=col, ax=axes[i], palette='viridis', order=df_clean[col].value_counts().index)
    
#     axes[i].set_title(f'Distribution of {col}', fontsize=12)
#     axes[i].set_xlabel(col, fontsize=10)
#     axes[i].set_ylabel('Count', fontsize=10)
    
#     # Agar x-axis par naam bade hain (jaise Neighborhood), toh unhe thoda ghuma (rotate) dete hain taaki saaf dikhein
#     axes[i].tick_params(axis='x', rotation=45)

# # 5. Extra khali dabba delete karna
# for j in range(i + 1, len(axes)):
#     fig.delaxes(axes[j])

# plt.tight_layout()
# plt.show()
#label encoding for categorical variables
# 1. Quality wale columns ke liye ek dictionary (map) banate hain
quality_map = {
    'None': 0,  # Jahan basement nahi hai
    'Fa': 1,    # Fair
    'TA': 2,    # Typical/Average
    'Gd': 3,    # Good
    'Ex': 4     # Excellent
}

# 2. Teeno quality columns par yeh map apply karte hain
df_clean['ExterQual'] = df_clean['ExterQual'].map(quality_map)
df_clean['KitchenQual'] = df_clean['KitchenQual'].map(quality_map)
df_clean['BsmtQual'] = df_clean['BsmtQual'].map(quality_map)

# 3. CentralAir (AC) ke liye simple mapping: N ko 0, Y ko 1
df_clean['CentralAir'] = df_clean['CentralAir'].map({'N': 0, 'Y': 1})

# Check karte hain ki text numbers mein badla ya nahi
print(df_clean[['ExterQual', 'KitchenQual', 'BsmtQual', 'CentralAir']].head())
df_final = pd.get_dummies(df_clean, columns=['Neighborhood', 'Foundation', 'MSZoning', 'GarageFinish', 'FireplaceQu', 'HouseStyle'], drop_first=True)
# 2. Yeh check karne ke liye ki saare columns ab numbers ban chuke hain
print("Naye Dataframe ka shape:", df_final.shape)
print("\nKya koi text column bacha hai?", df_final.select_dtypes(include=['object']).columns.any())
# Pure filtered data ka statistical overview
print("--- Statistical Summary ---")
print(df_clean.describe())
# Sirf numeric columns ka correlation nikalna
numeric_df = df_clean.select_dtypes(include=['number'])
corr_matrix = numeric_df.corr()

# SalePrice ke sath kiska kitna solid rishta hai (Sorted)
print("--- Correlation with SalePrice ---")
print(corr_matrix['SalePrice'].sort_values(ascending=False))

# Ek mast heatmap plot karna
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Sirf numeric columns ka correlation nikalna
numeric_df = df_clean.select_dtypes(include=['number'])
corr_matrix = numeric_df.corr()

# SalePrice ke sath kiska kitna solid rishta hai (Sorted)
print("--- Correlation with SalePrice ---")
print(corr_matrix['SalePrice'].sort_values(ascending=False))

#save the final featured data to a new csv file
df_final.to_csv('cleaned_data.csv', index=False)   
print("Cleaned data saved to 'cleaned_data.csv' successfully!")