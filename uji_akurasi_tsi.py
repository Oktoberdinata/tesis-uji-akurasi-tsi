# uji_akurasi_tsi.py
"""
Script untuk menghitung akurasi prediksi TSI
"""

import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Membaca dataset (CSV)
data = pd.read_csv("data_tsi.csv")

# Kolom 'observed' = nilai pengamatan TSI
# Kolom 'predicted' = nilai hasil model TSI
observed = data["observed"]
predicted = data["predicted"]

# Menghitung metrik akurasi
mae = mean_absolute_error(observed, predicted)
rmse = np.sqrt(mean_squared_error(observed, predicted))
r2 = r2_score(observed, predicted)

print(f"Mean Absolute Error (MAE): {mae:.3f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.3f}")
print(f"R-squared: {r2:.3f}")

# Plot scatter
plt.figure(figsize=(6, 6))
plt.scatter(observed, predicted, color="blue", edgecolors="k")
plt.plot([observed.min(), observed.max()], [observed.min(), observed.max()], "r--")
plt.xlabel("Observed TSI")
plt.ylabel("Predicted TSI")
plt.title("Observed vs Predicted TSI")
plt.grid(True)
plt.tight_layout()
plt.show()
