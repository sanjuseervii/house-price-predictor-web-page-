from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from fastapi.middleware.cors import CORSMiddleware  # 1. Yeh import hona chahiye
import numpy as np

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Isse har origin (jaise localhost:5173) ko permission milti hai
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model load kiya
model = joblib.load('house_price_model.pkl')

class HouseFeatures(BaseModel):
    GrLivArea: float
    OverallQual: float
    GarageCars: int
    GarageArea: float      # 🔥 Yeh naya add kiya frontend input ke liye
    TotalBsmtSF: float
    FullBath: int
    YearBuilt: int
    YearRemodAdd: int
    Neighborhood: str
    MSZoning: str
    HouseStyle: str

@app.post("/predict")
def predict_price(data: HouseFeatures):
    
    # 📝 EXACT 62 COLUMNS (Verified & Matched with your list)
    all_columns = [
        'GrLivArea', 'OverallQual', 'GarageCars', 'GarageArea', 'TotalBsmtSF', '1stFlrSF', 
        'FullBath', 'TotRmsAbvGrd', 'YearBuilt', 'YearRemodAdd', 'ExterQual', 'KitchenQual', 
        'BsmtQual', 'CentralAir', 'Neighborhood_Blueste', 'Neighborhood_BrDale', 'Neighborhood_BrkSide', 
        'Neighborhood_ClearCr', 'Neighborhood_CollgCr', 'Neighborhood_Crawfor', 'Neighborhood_Edwards', 
        'Neighborhood_Gilbert', 'Neighborhood_IDOTRR', 'Neighborhood_MeadowV', 'Neighborhood_Mitchel', 
        'Neighborhood_NAmes', 'Neighborhood_NPkVill', 'Neighborhood_NWAmes', 'Neighborhood_NoRidge', 
        'Neighborhood_NridgHt', 'Neighborhood_OldTown', 'Neighborhood_SWISU', 'Neighborhood_Sawyer', 
        'Neighborhood_SawyerW', 'Neighborhood_Somerst', 'Neighborhood_StoneBr', 'Neighborhood_Timber', 
        'Neighborhood_Veenker', 'Foundation_CBlock', 'Foundation_PConc', 'Foundation_Slab', 
        'Foundation_Stone', 'Foundation_Wood', 'MSZoning_FV', 'MSZoning_RH', 'MSZoning_RL', 
        'MSZoning_RM', 'GarageFinish_None', 'GarageFinish_RFn', 'GarageFinish_Unf', 'FireplaceQu_Fa', 
        'FireplaceQu_Gd', 'FireplaceQu_None', 'FireplaceQu_Po', 'FireplaceQu_TA', 'HouseStyle_1.5Unf', 
        'HouseStyle_1Story', 'HouseStyle_2.5Fin', 'HouseStyle_2.5Unf', 'HouseStyle_2Story', 
        'HouseStyle_SFoyer', 'HouseStyle_SLvl'
    ]
    
    # Sabko default 0.0 kiya
    feature_dict = {col: 0.0 for col in all_columns}
    
    # Numerical values fill ki
    feature_dict['GrLivArea'] = data.GrLivArea
    feature_dict['OverallQual'] = data.OverallQual
    feature_dict['GarageCars'] = data.GarageCars
    feature_dict['GarageArea'] = data.GarageArea  # 🔥 Map kar diya
    feature_dict['TotalBsmtSF'] = data.TotalBsmtSF
    feature_dict['FullBath'] = data.FullBath
    feature_dict['YearBuilt'] = data.YearBuilt
    feature_dict['YearRemodAdd'] = data.YearRemodAdd
    
    # Backup logical math columns
    feature_dict['1stFlrSF'] = data.GrLivArea * 0.5
    feature_dict['TotRmsAbvGrd'] = int(data.FullBath * 2) + 1
    feature_dict['CentralAir'] = 1.0  # Default assume kiya ki AC hai ghar mein
    
    # Dynamic Encoding Logic
    target_neighborhood = f"Neighborhood_{data.Neighborhood}"
    if target_neighborhood in feature_dict:
        feature_dict[target_neighborhood] = 1.0
        
    target_zoning = f"MSZoning_{data.MSZoning}"
    if target_zoning in feature_dict:
        feature_dict[target_zoning] = 1.0
        
    target_style = f"HouseStyle_{data.HouseStyle}"
    if target_style in feature_dict:
        feature_dict[target_style] = 1.0

    # Array format conversion
    input_array = np.array([[feature_dict[col] for col in all_columns]])
    
    # Prediction
    prediction = model.predict(input_array)
    
    return {"predicted_price": float(prediction[0])}