import pandas as pd
import matplotlib.pyplot as plt

# heart disease
#
# age - in years
# sex - (1 = male; 0 = female)
# cp - chest pain type
# trestbps - resting blood pressure (in mm Hg on admission to the hospital)
# chol - serum cholestoral in mg/dl
# fbs - (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
# restecg - resting electrocardiographic results
# thalach - maximum heart rate achieved
# exang - exercise induced angina (1 = yes; 0 = no)
# oldpeak - ST depression induced by exercise relative to rest
# slope - the slope of the peak exercise ST segment
# ca - number of major vessels (0-3) colored by flourosopy
# thal - 3 = normal; 6 = fixed defect; 7 = reversable defect 
# target - 1 or 0

def plot_target_count(data):
    if data is None:
        data=pd.read_csv("heart disease.csv")
        
    data.target.value_counts().plot(kind="bar", color=["salmon", "lightblue"])
    
    plt.ylabel("Total")
    plt.xlabel("Heart disease")   
    plt.show()

def plot_nulls(data):
    if data is None:
        data=pd.read_csv("heart disease.csv")

    pd.set_option("display.float", "{:.2f}".format)
    print ("Null values", data.isnull().sum())

def plot_age_heart_rate(data):
    if data is None:
        data=pd.read_csv("heart disease.csv")
    
    plt.figure(figsize=(10, 8))

    plt.scatter(data.age[data.target==1], data.thalach[data.target==1], c="red")        # heart disease
    plt.scatter(data.age[data.target==0], data.thalach[data.target==0], c="lightblue")  # no heart disease

    plt.title("Age vs. max heart rate")
    plt.xlabel("Age")
    plt.ylabel("Max heart rate")
    plt.legend(["Heart disease", "No heart disease"]);

    plt.show()
    

if __name__=="__main__":
    
    data=pd.read_csv("heart disease.csv")

    plot_nulls(data)
    plot_age_heart_rate(data)