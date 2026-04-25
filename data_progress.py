import pandas as pd

# 1. Cargar datos
df = pd.read_csv("https://raw.githubusercontent.com/NationalSpark37/Tratamiento-Datos-Parte1/main/pipol_datos%20(1).csv", index_col=0)

# 2. Renombrar columnas
df.columns = ["age", "sex", "income", "height", "city", "education", "children"]

# 3. Ver datos iniciales
print("Primeros datos:")
print(df.head())

# 4. Valores únicos (detectar errores)
print("\nValores únicos:")
print("Sex:", set(df["sex"]))
print("City:", set(df["city"]))
print("Education:", set(df["education"]))

# 5. Nulos
print("\nValores nulos:")
print(df.isnull().sum())

# ---------------- FUNCIONES ---------------- #

# Eliminar negativos
def eliminar_negativos(df, columnas):
    for col in columnas:
        df[col] = df[col].apply(lambda x: 0 if x < 0 else x)
    return df

# Rellenar nulos
def rellenar_nulos(df):
    df["sex"] = df["sex"].fillna("Unknown")
    df["age"] = df["age"].fillna(df["age"].mean())
    return df

# Detectar outliers con Z-score
def detectar_outliers(df, columna):
    media = df[columna].mean()
    std = df[columna].std()
    z_scores = (df[columna] - media) / std
    return df[abs(z_scores) > 3]

# Corregir texto
def corregir_texto(df):
    df["education"] = df["education"].str.lower()
    df["sex"] = df["sex"].str.lower()
    return df

# ---------------- APLICAR LIMPIEZA ---------------- #

df = rellenar_nulos(df)
df = eliminar_negativos(df, ["income", "children"])
df = corregir_texto(df)

# Detectar outliers
outliers_age = detectar_outliers(df, "age")

print("\nOutliers en edad:")
print(outliers_age)

# Resultado final
print("\nDatos limpios:")
print(df.head())


# In[ ]:




