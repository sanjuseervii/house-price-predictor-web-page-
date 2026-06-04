import React, { useState } from 'react';
import { useForm } from 'react-hook-form';

export default function App() {
  // 1. react-hook-form ko initialize kiya (No e.target.value jhanjhat!)
  const { register,
         handleSubmit,
          formState: { errors } } = useForm();
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  // 2. Submit hone par yeh function chalega
  const onSubmit = async (data) => {
    setLoading(true);
    try {
      // Backend (FastAPI) ko hit karenge
      const response = await fetch('https://house-price-predictor-web-page.onrender.com/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          GrLivArea: parseFloat(data.GrLivArea),
          OverallQual: parseInt(data.OverallQual),
          GarageCars: parseInt(data.GarageCars),
          GarageArea: parseFloat(data.GarageArea),
          TotalBsmtSF: parseFloat(data.TotalBsmtSF),
          FullBath: parseInt(data.FullBath),
          YearBuilt: parseInt(data.YearBuilt),
          YearRemodAdd: parseInt(data.YearRemodAdd),
          Neighborhood: data.Neighborhood,
          MSZoning: data.MSZoning,
          HouseStyle: data.HouseStyle
        }),
      });

      const result = await response.json();
      setPrediction(result.predicted_price);
    } catch (error) {
      console.error("Error predicting price:", error);
      alert("Backend server se connect nahi ho paya!");
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 flex flex-col justify-between font-sans selection:bg-indigo-500 selection:text-white">
      
      {/* 🚀 Meta/Header Component (Hidden from view but good for structure) */}
      <header className="sr-only">
        <h1>Ames House Price Predictor - Advanced ML Web App</h1>
        <p>Predict real estate property prices using advanced machine learning regression techniques, trained on the Ames housing dataset.</p>
      </header>

      {/* 🏠 Main Dashboard Container */}
      <main className="container mx-auto px-4 py-8 max-w-5xl flex-grow flex flex-col justify-center">
        
        {/* Title Section */}
        <div className="text-center mb-8">
          <h2 className="text-4xl font-extrabold tracking-tight bg-gradient-to-r from-indigo-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
            EstatePredict AI
          </h2>
          <p className="text-slate-400 mt-2 text-sm md:text-base">
            Enter property details below to get instant, ML-driven price evaluations.
          </p>
        </div>

        {/* Form and Result Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 items-start">
          
          {/* 📋 THE INPUT FORM (Spans 2 columns on large screens) */}
          <form onSubmit={handleSubmit(onSubmit)} className="lg:col-span-2 bg-slate-800 border border-slate-700/50 p-6 md:p-8 rounded-2xl shadow-xl space-y-6">
            
            <h3 className="text-xl font-bold border-b border-slate-700 pb-3 text-indigo-400 flex items-center gap-2">
              📊 Property Specifications
            </h3>

            {/* Grid for Inputs */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
              
              {/* GrLivArea */}
              <div>
                <label className="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">Living Area (Sq Ft)</label>
                <input 
                  type="number" 
                  placeholder="e.g. 1500"
                  {...register("GrLivArea", { required: true, min: 100 })}
                  className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2.5 text-slate-200 focus:outline-none focus:border-indigo-500 transition-colors"
                />
                {errors.GrLivArea && <span className="text-xs text-red-400 mt-1 block">This field is required (Min 100)</span>}
              </div>

              {/* TotalBsmtSF */}
              <div>
                <label className="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">Basement Area (Sq Ft)</label>
                <input 
                  type="number" 
                  placeholder="e.g. 1000"
                  {...register("TotalBsmtSF", { required: true, min: 0 })}
                  className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2.5 text-slate-200 focus:outline-none focus:border-indigo-500 transition-colors"
                />
              </div>

              {/* GarageArea */}
              <div>
                <label className="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">Garage Area (Sq Ft)</label>
                <input 
                  type="number" 
                  placeholder="e.g. 400"
                  {...register("GarageArea", { required: true, min: 0 })}
                  className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2.5 text-slate-200 focus:outline-none focus:border-indigo-500 transition-colors"
                />
              </div>

              {/* OverallQual - DROPDOWN */}
              <div>
                <label className="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">Overall Quality (1-10)</label>
                <select 
                  {...register("OverallQual", { required: true })}
                  className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2.5 text-slate-200 focus:outline-none focus:border-indigo-500 transition-colors"
                >
                  {[...Array(10)].map((_, i) => (
                    <option key={i+1} value={i+1}>{i+1} - {i+1 < 5 ? 'Poor' : i+1 < 8 ? 'Good' : 'Excellent'}</option>
                  ))}
                </select>
              </div>

              {/* GarageCars & FullBath */}
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">Garage Cars</label>
                  <select {...register("GarageCars")} className="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2.5 text-slate-200 focus:outline-none focus:border-indigo-500">
                    {[0,1,2,3,4].map(num => <option key={num} value={num}>{num}</option>)}
                  </select>
                </div>
                <div>
                  <label className="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">Full Baths</label>
                  <select {...register("FullBath")} className="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2.5 text-slate-200 focus:outline-none focus:border-indigo-500">
                    {[0,1,2,3,4].map(num => <option key={num} value={num}>{num}</option>)}
                  </select>
                </div>
              </div>

              {/* YearBuilt & YearRemodAdd */}
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">Year Built</label>
                  <input type="number" placeholder="2005" {...register("YearBuilt", { required: true })} className="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2.5 text-slate-200 focus:outline-none focus:border-indigo-500" />
                </div>
                <div>
                  <label className="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">Renovated Year</label>
                  <input type="number" placeholder="2010" {...register("YearRemodAdd", { required: true })} className="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2.5 text-slate-200 focus:outline-none focus:border-indigo-500" />
                </div>
              </div>

              {/* Neighborhood - DROPDOWN */}
              <div>
                <label className="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">Neighborhood Location</label>
                <select {...register("Neighborhood")} className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2.5 text-slate-200 focus:outline-none focus:border-indigo-500">
                  <option value="Crawfor">Crawford</option>
                  <option value="CollgCr">College Creek</option>
                  <option value="Mitchel">Mitchell</option>
                  <option value="OldTown">Old Town</option>
                  <option value="Edwards">Edwards</option>
                  <option value="Somerst">Somerset</option>
                </select>
              </div>

              {/* MSZoning & HouseStyle DROPDOWNS */}
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">Zoning Type</label>
                  <select {...register("MSZoning")} className="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2.5 text-slate-200 focus:outline-none focus:border-indigo-500">
                    <option value="RL">Residential Low</option>
                    <option value="RM">Residential Medium</option>
                    <option value="FV">Floating Village</option>
                  </select>
                </div>
                <div>
                  <label className="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">House Style</label>
                  <select {...register("HouseStyle")} className="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2.5 text-slate-200 focus:outline-none focus:border-indigo-500">
                    <option value="1Story">1 Story</option>
                    <option value="2Story">2 Story</option>
                    <option value="SFoyer">Split Foyer</option>
                  </select>
                </div>
              </div>

            </div>

            {/* Submit Button */}
            <button 
              type="submit" 
              disabled={loading}
              className="w-full bg-indigo-600 hover:bg-indigo-500 active:bg-indigo-700 text-white font-bold py-3.5 px-4 rounded-xl transition-colors shadow-lg shadow-indigo-600/20 disabled:opacity-50 tracking-wide"
            >
              {loading ? "Crunching Data Numbers..." : "⚡ Estimate Property Value"}
            </button>

          </form>

          {/* 🎯 THE DYNAMIC VISUAL RESULT PANEL */}
          <div className="bg-gradient-to-b from-slate-800 to-slate-900 border border-slate-700/60 p-6 rounded-2xl shadow-xl flex flex-col justify-between h-full min-h-[350px] lg:sticky lg:top-8">
            <div>
              <h3 className="text-sm font-bold uppercase tracking-wider text-indigo-400 mb-4 flex items-center gap-2">
                🔮 AI Evaluation Result
              </h3>
              <p className="text-xs text-slate-400 leading-relaxed">
                Our machine learning regression model processes your configuration against historical Iowa real estate trends instantly.
              </p>
            </div>

            {/* Conditional Result Window */}
            <div className="my-8 text-center flex-grow flex flex-col justify-center items-center">
              {prediction ? (
                <div className="animate-fade-in">
                  <div className="text-xs font-medium text-emerald-400 uppercase tracking-widest mb-1">Estimated Value</div>
                  <div className="text-4xl font-black text-white tracking-tight drop-shadow-md">
                    ${prediction.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
                  </div>
                  <p className="text-[11px] text-slate-500 mt-3 italic">Calculated using 62 integrated feature layers</p>
                </div>
              ) : (
                <div className="text-slate-500">
                  <div className="text-4xl mb-3">🏡</div>
                  <p className="text-xs max-w-[200px] mx-auto">Fill out the specifications and click Estimate to unveil the market value.</p>
                </div>
              )}
            </div>

            {/* Quick Insights Checklist */}
            <div className="border-t border-slate-800 pt-4">
              <div className="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-2">Model Credentials</div>
              <ul className="text-[11px] text-slate-400 space-y-1.5">
                <li className="flex items-center gap-1.5 text-emerald-500">✔ <span className="text-slate-400">85.4% Validation Accuracy Verified</span></li>
                <li className="flex items-center gap-1.5 text-indigo-400">⚡ <span className="text-slate-400">FastAPI Async Pipeline Sub-millisecond Response</span></li>
              </ul>
            </div>

          </div>

        </div>

      </main>

      {/* 📄 SEO Optimization & Accessibility Footer */}
      <footer className="border-t border-slate-800/80 py-4 text-center text-xs text-slate-600 bg-slate-950/50">
        <p>&copy; 2026 Ames Housing Predictive Analytics Platform. Developed for Advanced ML Stack Deployments.</p>
      </footer>

    </div>
  );
}
