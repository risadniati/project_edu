# -*- coding: utf-8 -*-
"""notebook_edu.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MmPypkOgxg6W6IA13L1ErsbibbNn4nVu

# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

- Nama: Maria Goretti Risadniati Madsun
- Email: risadniati@gmail.com
- Id Dicoding: icachan47

## Persiapan

### Menyiapkan library yang dibutuhkan

Menyiapkan direktori dan virtual environment
"""

# Commented out IPython magic to ensure Python compatibility.
# Membuat direktori project
!mkdir edu_project

# Memindahkan direktori
# %cd edu_project

# Menginstal 'virtualenv'
!pip install virtualenv

# Membuat virtual environment di dalam direktori proyek
!virtualenv env

# Mengaktifkan virtual environment
!source env/bin/activate

# Menginstall library
!pip install numpy pandas scipy matplotlib seaborn sqlalchemy scikit-learn joblib

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import sys
import os
import joblib
# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.utils import resample
from sklearn.utils import shuffle
from google.colab import files
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

# Menggunakan paket dari virtual environment
sys.path.append('/content/edu_project/env/lib/python3.8/site-packages')

# Verifikasi instalasi
print(np.__version__)

"""### Menyiapkan data yang akan digunakan"""

url = 'https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv'
main_df = pd.read_csv(url, encoding='windows-1252', delimiter=';')

print(main_df.head(5))

"""## Data Understanding

Students' Performance

A dataset created from a higher education institution (acquired from several disjoint databases) related to students enrolled in different undergraduate degrees, such as agronomy, design, education, nursing, journalism, management, social service, and technologies. The dataset includes information known at the time of student enrollment (academic path, demographics, and social-economic factors) and the students' academic performance at the end of the first and second semesters. The data is used to build classification models to predict students' dropout and academic sucess.

| Column name | Description |
| --- | --- |
|Marital status | The marital status of the student. (Categorical) 1 – single 2 – married 3 – widower 4 – divorced 5 – facto union 6 – legally separated |
| Application mode | The method of application used by the student. (Categorical) 1 - 1st phase - general contingent 2 - Ordinance No. 612/93 5 - 1st phase - special contingent (Azores Island) 7 - Holders of other higher courses 10 - Ordinance No. 854-B/99 15 - International student (bachelor) 16 - 1st phase - special contingent (Madeira Island) 17 - 2nd phase - general contingent 18 - 3rd phase - general contingent 26 - Ordinance No. 533-A/99, item b2) (Different Plan) 27 - Ordinance No. 533-A/99, item b3 (Other Institution) 39 - Over 23 years old 42 - Transfer 43 - Change of course 44 - Technological specialization diploma holders 51 - Change of institution/course 53 - Short cycle diploma holders 57 - Change of institution/course (International)|
|Application order | The order in which the student applied. (Numerical) Application order (between 0 - first choice; and 9 last choice) |
|Course | The course taken by the student. (Categorical) 33 - Biofuel Production Technologies 171 - Animation and Multimedia Design 8014 - Social Service (evening attendance) 9003 - Agronomy 9070 - Communication Design 9085 - Veterinary Nursing 9119 - Informatics Engineering 9130 - Equinculture 9147 - Management 9238 - Social Service 9254 - Tourism 9500 - Nursing 9556 - Oral Hygiene 9670 - Advertising and Marketing Management 9773 - Journalism and Communication 9853 - Basic Education 9991 - Management (evening attendance)|
|Daytime/evening attendance | Whether the student attends classes during the day or in the evening. (Categorical) 1 – daytime 0 - evening |
|Previous qualification| The qualification obtained by the student before enrolling in higher education. (Categorical) 1 - Secondary education 2 - Higher education - bachelor's degree 3 - Higher education - degree 4 - Higher education - master's 5 - Higher education - doctorate 6 - Frequency of higher education 9 - 12th year of schooling - not completed 10 - 11th year of schooling - not completed 12 - Other - 11th year of schooling 14 - 10th year of schooling 15 - 10th year of schooling - not completed 19 - Basic education 3rd cycle (9th/10th/11th year) or equiv. 38 - Basic education 2nd cycle (6th/7th/8th year) or equiv. 39 - Technological specialization course 40 - Higher education - degree (1st cycle) 42 - Professional higher technical course 43 - Higher education - master (2nd cycle) |
|Previous qualification (grade) | Grade of previous qualification (between 0 and 200) |
| Nacionality | The nationality of the student. (Categorical) 1 - Portuguese; 2 - German; 6 - Spanish; 11 - Italian; 13 - Dutch; 14 - English; 17 - Lithuanian; 21 - Angolan; 22 - Cape Verdean; 24 - Guinean; 25 - Mozambican; 26 - Santomean; 32 - Turkish; 41 - Brazilian; 62 - Romanian; 100 - Moldova (Republic of); 101 - Mexican; 103 - Ukrainian; 105 - Russian; 108 - Cuban; 109 - Colombian|
|Mother's qualification | The qualification of the student's mother. (Categorical) 1 - Secondary Education - 12th Year of Schooling or Eq. 2 - Higher Education - Bachelor's Degree 3 - Higher Education - Degree 4 - Higher Education - Master's 5 - Higher Education - Doctorate 6 - Frequency of Higher Education 9 - 12th Year of Schooling - Not Completed 10 - 11th Year of Schooling - Not Completed 11 - 7th Year (Old) 12 - Other - 11th Year of Schooling 14 - 10th Year of Schooling 18 - General commerce course 19 - Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv. 22 - Technical-professional course 26 - 7th year of schooling 27 - 2nd cycle of the general high school course 29 - 9th Year of Schooling - Not Completed 30 - 8th year of schooling 34 - Unknown 35 - Can't read or write 36 - Can read without having a 4th year of schooling 37 - Basic education 1st cycle (4th/5th year) or equiv. 38 - Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv. 39 - Technological specialization course 40 - Higher education - degree (1st cycle) 41 - Specialized higher studies course 42 - Professional higher technical course 43 - Higher Education - Master (2nd cycle) 44 - Higher Education - Doctorate (3rd cycle)|
|Father's qualification | The qualification of the student's father. (Categorical) 1 - Secondary Education - 12th Year of Schooling or Eq. 2 - Higher Education - Bachelor's Degree 3 - Higher Education - Degree 4 - Higher Education - Master's 5 - Higher Education - Doctorate 6 - Frequency of Higher Education 9 - 12th Year of Schooling - Not Completed 10 - 11th Year of Schooling - Not Completed 11 - 7th Year (Old) 12 - Other - 11th Year of Schooling 13 - 2nd year complementary high school course 14 - 10th Year of Schooling 18 - General commerce course 19 - Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv. 20 - Complementary High School Course 22 - Technical-professional course 25 - Complementary High School Course - not concluded 26 - 7th year of schooling 27 - 2nd cycle of the general high school course 29 - 9th Year of Schooling - Not Completed 30 - 8th year of schooling 31 - General Course of Administration and Commerce 33 - Supplementary Accounting and Administration 34 - Unknown 35 - Can't read or write 36 - Can read without having a 4th year of schooling 37 - Basic education 1st cycle (4th/5th year) or equiv. 38 - Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv. 39 - Technological specialization course 40 - Higher education - degree (1st cycle) 41 - Specialized higher studies course 42 - Professional higher technical course 43 - Higher Education - Master (2nd cycle) 44 - Higher Education - Doctorate (3rd cycle) |
| Mother's occupation | The occupation of the student's mother. (Categorical) 0 - Student 1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers 2 - Specialists in Intellectual and Scientific Activities 3 - Intermediate Level Technicians and Professions 4 - Administrative staff 5 - Personal Services, Security and Safety Workers and Sellers 6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry 7 - Skilled Workers in Industry, Construction and Craftsmen 8 - Installation and Machine Operators and Assembly Workers 9 - Unskilled Workers 10 - Armed Forces Professions 90 - Other Situation 99 - (blank) 122 - Health professionals 123 - teachers 125 - Specialists in information and communication technologies (ICT) 131 - Intermediate level science and engineering technicians and professions 132 - Technicians and professionals, of intermediate level of health 134 - Intermediate level technicians from legal, social, sports, cultural and similar services 141 - Office workers, secretaries in general and data processing operators 143 - Data, accounting, statistical, financial services and registry-related operators 144 - Other administrative support staff 151 - personal service workers 152 - sellers 153 - Personal care workers and the like 171 - Skilled construction workers and the like, except electricians 173 - Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like 175 - Workers in food processing, woodworking, clothing and other industries and crafts 191 - cleaning workers 192 - Unskilled workers in agriculture, animal production, fisheries and forestry 193 - Unskilled workers in extractive industry, construction, manufacturing and transport 194 - Meal preparation assistants |
| Father's occupation | The occupation of the student's father. (Categorical) 0 - Student 1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers 2 - Specialists in Intellectual and Scientific Activities 3 - Intermediate Level Technicians and Professions 4 - Administrative staff 5 - Personal Services, Security and Safety Workers and Sellers 6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry 7 - Skilled Workers in Industry, Construction and Craftsmen 8 - Installation and Machine Operators and Assembly Workers 9 - Unskilled Workers 10 - Armed Forces Professions 90 - Other Situation 99 - (blank) 101 - Armed Forces Officers 102 - Armed Forces Sergeants 103 - Other Armed Forces personnel 112 - Directors of administrative and commercial services 114 - Hotel, catering, trade and other services directors 121 - Specialists in the physical sciences, mathematics, engineering and related techniques 122 - Health professionals 123 - teachers 124 - Specialists in finance, accounting, administrative organization, public and commercial relations 131 - Intermediate level science and engineering technicians and professions 132 - Technicians and professionals, of intermediate level of health 134 - Intermediate level technicians from legal, social, sports, cultural and similar services 135 - Information and communication technology technicians 141 - Office workers, secretaries in general and data processing operators 143 - Data, accounting, statistical, financial services and registry-related operators 144 - Other administrative support staff 151 - personal service workers 152 - sellers 153 - Personal care workers and the like 154 - Protection and security services personnel 161 - Market-oriented farmers and skilled agricultural and animal production workers 163 - Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence 171 - Skilled construction workers and the like, except electricians 172 - Skilled workers in metallurgy, metalworking and similar 174 - Skilled workers in electricity and electronics 175 - Workers in food processing, woodworking, clothing and other industries and crafts 181 - Fixed plant and machine operators 182 - assembly workers 183 - Vehicle drivers and mobile equipment operators 192 - Unskilled workers in agriculture, animal production, fisheries and forestry 193 - Unskilled workers in extractive industry, construction, manufacturing and transport 194 - Meal preparation assistants 195 - Street vendors (except food) and street service providers |
| Admission grade | Admission grade (between 0 and 200) |
| Displaced | Whether the student is a displaced person. (Categorical) 	1 – yes 0 – no |
| Educational special needs | Whether the student has any special educational needs. (Categorical) 1 – yes 0 – no |
|Debtor | Whether the student is a debtor. (Categorical) 1 – yes 0 – no|
|Tuition fees up to date | Whether the student's tuition fees are up to date. (Categorical) 1 – yes 0 – no|
|Gender | The gender of the student. (Categorical) 1 – male 0 – female |
|Scholarship holder | Whether the student is a scholarship holder. (Categorical) 1 – yes 0 – no |
|Age at enrollment | The age of the student at the time of enrollment. (Numerical)|
|International | Whether the student is an international student. (Categorical) 1 – yes 0 – no|
|Curricular units 1st sem (credited) | The number of curricular units credited by the student in the first semester. (Numerical) |
| Curricular units 1st sem (enrolled) | The number of curricular units enrolled by the student in the first semester. (Numerical) |
| Curricular units 1st sem (evaluations) | The number of curricular units evaluated by the student in the first semester. (Numerical) |
| Curricular units 1st sem (approved) | The number of curricular units approved by the student in the first semester. (Numerical) |

- Memeriksa apakah terdapat missing value
"""

main_df.isna().sum()

"""Data cukup baik, karena tidak ada kolom yang memiliki missing value

- Memeriksa apakah ada invalid value
"""

print(main_df.dtypes)

"""Data cukup baik, dimana tipe data sesuai dengan deskripsi data

- Memeriksa apakah ada data duplikat
"""

# Memeriksa baris duplikat
baris_duplikat = main_df[main_df.duplicated()]

print('Baris duplikat:')
print(baris_duplikat)

"""Tidak ada baris yang duplikat dalam data, maka data sudah cukup baik, karena memiliki nilai unik.

- Memeriksa apakah ada inaccurate value
"""

main_df.describe()

"""Statistik data terlihat normal. Data dapat digunakan untuk proses selanjutnya.

- Exploratory Data Analysis

Melihat sebaran pada kolom Status
"""

main_df['Status'].value_counts()

"""Terdapat 3 nilai pada kolom status, yaitu Graduate, Dropout dan Enrolled.
Namun, pada proyek ini hanya akan dianalisa status Graduate dan Dropout. Oleh karena itu, status Enrolled akan dihapus
"""

main_df = main_df[main_df['Status'] != 'Enrolled']

"""Melihat kembali sebaran kolom status setelah menghapus nilai Enrolled"""

main_df['Status'].value_counts()

"""Untuk memudahkan pemrosesan data selanjutnya, data pada kolom Status akan diubah menjadi numerik :
- Graduate = 1
- Dropout = 0
"""

# Mengubah nilai 'graduate' menjadi 1 dan 'dropout' menjadi 0
main_df['Status'] = main_df['Status'].map({'Graduate': 1, 'Dropout': 0})
print(main_df['Status'].value_counts)

"""## Data Preparation / Preprocessing

- Memeriksa korelasi
"""

correlation_matrix = main_df.corr()

plt.figure(figsize=(30, 15))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()

"""Heatmap di atas menampilkan hubungan antaran semua kolom. Selanjutnya, mari kita lihat heatmap yang berkorelasi dengan kolom status"""

correlation_matrix = main_df.corr()
status_correlation = correlation_matrix[['Status']].sort_values(by='Status', ascending=False)

plt.figure(figsize=(5, 10))
sns.heatmap(status_correlation, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation with Status')
plt.show()

"""Berdasarkan korelasi dengan kolom Status, maka untuk pre-processing dapat digunakan kolom :
- Curricular_units_2nd_sem_approved
- Curricular_units_2nd_sem_grade
- Curricular_units_1st_sem_approved
- Curricullar_units_1st_sem_grade
- Tuition_fees_up_to_date

Hal ini karena kolom di atas berkaitan erat dengan kolom Status, atau dengan kata lain kelima fitur di atas mempengaruhi dropout atau lulusnya mahasiswa.
"""

selected_features = [
  'Curricular_units_2nd_sem_approved',
  'Curricular_units_2nd_sem_grade',
  'Curricular_units_1st_sem_approved',
  'Curricular_units_1st_sem_grade',
  'Tuition_fees_up_to_date'
]

new_main_df = main_df[selected_features + ['Status']]
new_main_df.head(5)

"""Train-Test Split"""

# Membagi data menjadi fitur dan target
X = new_main_df.drop('Status', axis=1)
y = new_main_df['Status']

# Memisahkan data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, shuffle=True)

"""Selanjutnya, dilihat banyaknya data untuk 'dropout' dan 'graduate'. Apabila data belum seimbang, maka akan dilakukan oversampling terlebih dahulu"""

plt.figure(figsize=(8, 6))
sns.countplot(x=y_train)
plt.title('Distribusi Kelas Status')
plt.show()

"""Data latih didominasi kategori status = 1, ini menunjukkan adanya imbalance data yang berpotensi menghasilkan bias dan membuat model cenderung memprediksi kelas dominan. Untuk mengatasi hal tersebut, maka digunakan teknik oversampling, untuk memperbanyak data secara acak dari kelas minoritas."""

df_majority = X_train[y_train == 1]
df_minority = X_train[y_train == 0]
y_majority = y_train[y_train == 1]
y_minority = y_train[y_train == 0]

# Oversampling
df_minority_oversampled, y_minority_oversampled = resample(df_minority, y_minority,
                                                           replace=True,
                                                           n_samples=len(df_majority),
                                                           random_state=42)

# Menggabungkan data mayoritas dan data minoritas yang sudah di-oversampling
X_train = pd.concat([df_majority, df_minority_oversampled])
y_train = pd.concat([y_majority, y_minority_oversampled])

X_train, y_train = shuffle(X_train, y_train, random_state=42)

if not isinstance(y_train, pd.Series):
  if not y_train.empty:
    y_train = pd.Series(y_train.values.flatten())

plt.figure(figsize=(8, 6))
sns.countplot(x=y_train)
plt.title('Distribusi Kelas Status')
plt.show()

"""Melalui grafik di atas, maka dapat diketahui bahwa distribusi kelas sudah seimbang. Selanjutnya, akan dibuat fungsi helper untuk scaling"""

# Definisi fungsi helper untuk scaling
def scaling(features, df, df_test=None):
    if df_test is not None:
        df = df.copy()
        df_test = df_test.copy()
        for feature in features:
            scaler = MinMaxScaler()
            df[feature] = scaler.fit_transform(df[[feature]])
            df_test[feature] = scaler.transform(df_test[[feature]])

            # Memastikan direktori 'model' ada
            if not os.path.exists("model"):
                os.makedirs("model")

            joblib.dump(scaler, f"model/scaler_{feature}.joblib")
        return df, df_test
    else:
        df = df.copy()
        for feature in features:
            scaler = MinMaxScaler()
            df[feature] = scaler.fit_transform(df[[feature]])

            # Memastikan direktori 'model' ada
            if not os.path.exists("model"):
                os.makedirs("model")

            joblib.dump(scaler, f"model/scaler_{feature}.joblib")
        return df

# Melakukan scaling pada fitur-fitur yang dipilih
X_train_scaled, X_test_scaled = scaling(selected_features, X_train, X_test)

print(X_train_scaled.head())
print(X_test_scaled.head())

# Menampilkan shape dari DataFrame asli dan hasil split
print("Shape of X_train:", X_train.shape)
print("Shape of X_test:", X_test.shape)
print("Shape of y_train:", y_train.shape)
print("Shape of y_test:", y_test.shape)

"""## Modeling

- Decision Tree
"""

# Inisialisasi parameter grid
param_grid = {
    'max_features': ['auto', 'sqrt', 'log2'],
    'max_depth': [5, 6, 7, 8],
    'criterion': ['gini', 'entropy']
}

# Inisialisasi model Decision Tree
tree_model = DecisionTreeClassifier(random_state=123)

# Inisialisasi GridSearchCV
CV_tree = GridSearchCV(estimator=tree_model, param_grid=param_grid, cv=5, n_jobs=-1)

# Melatih model dengan data latih yang telah di-scaling
CV_tree.fit(X_train_scaled, y_train)

# Menampilkan hyperparameter terbaik
print("Best Parameters:", CV_tree.best_params_)

# Menggunakan parameter terbaik dari GridSearchCV
best_params = {'criterion': 'gini', 'max_depth': 6, 'max_features': 'auto'}

# Inisialisasi Decision Tree dengan parameter terbaik
tree_model = DecisionTreeClassifier(**best_params, random_state=123)

# Melatih model dengan data latih yang telah di-preprocessing
tree_model.fit(X_train_scaled, y_train)

# Menyimpan model
joblib.dump(tree_model, "model/best_tree_model.joblib")

"""- Random Forest"""

# Inisialisasi RandomForestClassifier dengan GridSearchCV
param_grid = {
    'n_estimators': [100, 200, 300],  # jumlah pohon dalam hutan
    'max_depth': [None, 10, 20, 30],   # kedalaman maksimum setiap pohon
    'min_samples_split': [2, 5, 10],   # jumlah sampel minimum yang diperlukan untuk membagi simpul dalam pohon
    'min_samples_leaf': [1, 2, 4]      # jumlah sampel minimum yang diperlukan untuk menjadi daun pada pohon
}

rf_model = RandomForestClassifier(random_state=123)
CV_rf = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, n_jobs=-1)

# Melatih model dengan data latih yang telah di-preprocessing
CV_rf.fit(X_train_scaled, y_train)

# Menampilkan hyperparameter terbaik
print("Best Parameters:", CV_rf.best_params_)

# Gunakan parameter terbaik untuk membuat model
best_rf_model = RandomForestClassifier(**CV_rf.best_params_, random_state=123)

# Latih model dengan data latih yang telah di-preprocessing
best_rf_model.fit(X_train_scaled, y_train)

# Menyimpan model
joblib.dump(best_rf_model, "model/best_rf_model.joblib")

"""- Gradien Boosting"""

# Inisialisasi GradientBoostingClassifier dengan GridSearchCV
param_grid = {
    'n_estimators': [100, 200, 300],    # jumlah iterasi boosting
    'learning_rate': [0.1, 0.01, 0.001], # laju pembelajaran
    'max_depth': [3, 5, 7]               # kedalaman maksimum setiap pohon
}

gb_model = GradientBoostingClassifier(random_state=123)
CV_gb = GridSearchCV(estimator=gb_model, param_grid=param_grid, cv=5, n_jobs=-1)

# Melatih model dengan data latih yang telah di-preprocessing
CV_gb.fit(X_train_scaled, y_train)

# Menampilkan hyperparameter terbaik
print("Best Parameters:", CV_gb.best_params_)

# Gunakan parameter terbaik untuk membuat model
best_gb_model = GradientBoostingClassifier(**CV_gb.best_params_, random_state=123)

# Latih model dengan data latih yang telah di-preprocessing
best_gb_model.fit(X_train_scaled, y_train)

# Menyimpan model
joblib.dump(best_gb_model, "model/best_gb_model.joblib")

"""## Evaluation"""

def evaluate_model(model, X_test, y_test):
    '''Evaluates the model and displays the classification report and confusion matrix.'''
    y_pred = model.predict(X_test)

    # Classification report
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    # Confusion matrix
    print("Confusion Matrix:")
    cnf_matrix = confusion_matrix(y_test, y_pred)
    print(cnf_matrix)

    # Plot confusion matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(cnf_matrix, annot=True, cmap='Blues', fmt='g')
    plt.xlabel('Predicted labels')
    plt.ylabel('True labels')
    plt.title('Confusion Matrix')
    plt.show()

# Evaluasi model Decision Tree
print("Evaluation for Decision Tree Model:")
evaluate_model(tree_model, X_test_scaled, y_test)

# Evaluasi model Random Forest
print("Evaluation for Random Forest Model:")
evaluate_model(best_rf_model, X_test_scaled, y_test)

# Evaluasi model Gradient Boosting
print("Evaluation for Gradient Boosting Model:")
evaluate_model(best_gb_model, X_test_scaled, y_test)

"""Analisis :

1. Precision, Recall, dan F1-Score:
- Model Random Forest dan Gradient Boosting memiliki nilai precision, recall dan F1-Score yang lebih tinggi dari model Decision Tree untuk kelas 'dropout' atau 1. Ini menunjukkan bahwa kedua model cukup baik untuk memprediksi siswa yang dropout.

2. Accuracy
- Akurasi dari model Random Forest dan Gradient Boosting memiliki akurasi 0.89, nilai ini lebih tinggi dari akurasi Decision Tree (0.87)

3. Confusion Matrix
- Random Forest dan Gradient Boosting memiliki jumlah prediksi benar yang lebih tinggi dibandingkan dengan Decision Tree (dapat dilihat dari TP + TN)
- Jumlah False Negatives (FN) dari Random Forest merupakan yang terendah. Ini menunjukkan bahwa lebih sedikit kasus dropout yang salah terprediksi.


Kesimpulan :

Berdasarkan evaluasi di atas, model Random Forest dan Gradient Boosting memiliki performa yang sangat mirip, dengan keunggulan Random Forest dalam nilai precision dan jumlah False Negatives. Oleh karena itu, akan digunakan model Random Forest untuk memprediksi dropout.

"""