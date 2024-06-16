# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Pada proyek ini, diangkat sebuah studi kasus pada Jaya Jaya Institut.
Institusi pendidikan ini telah berdiri sejak tahun 2000 dan telah mencetak banyak lulusan dengan reputasi yang sangat baik. 
Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.
Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. 
Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.


### Permasalahan Bisnis

Proyek ini akan menjawab permasalahan bisnis berikut : 
- Mengidentifikasi faktor yang mempengaruhi kelulusan mahasiswa
- Memberikan wawasan sebaran mahasiswa kepada institut, agar perkembangan mahasiswa dapat dimonitor 

### Cakupan Proyek

Untuk menjawab permasalahan bisnis, maka akan dibuat sebuah business dashboard yang memvisualisasikan faktor-faktor yang mempengaruhi dropout.
Selain itu, akan dikembangkan pula prototipe model prediksi dengan machine learning untuk memprediksi mahasiswa yang berpotensi untuk melakukan dropout.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md

Setup environment:
Menggunakan Google Colab

```
!mkdir edu_project
%cd edu_project
!pip install virtualenv
!virtualenv env
import sys
sys.path.insert(0, "/content/edu_project/env/lib/python3.7/site-packages")
!pip install -r requirements.txt

```

## Business Dashboard

Link Dashboard : https://lookerstudio.google.com/reporting/0f5c3306-196f-49ac-b8bd-33a08ecb9f30

Pada Dashboard, ditampilkan sebaran mahasiswa berdasarkan status perkuliahan, gender, usia pendaftaran dan faktor yang mempengaruhi kelulusan maupun dropout mahasiswa.
- Pada Jaya Jaya Institute, terdapat 2,209 mahasiswa yang telah lulus, sedangkan untuk mahasiswa yang dropout mencapai 1421, dan mahasiswa yang baru saja mendaftar sebanyak 794 mahasiswa.
- Apabila dilihat dari distribusi berdasarkan gender, terdapat lebih banyak mahasiswa perempuan dibanding laki-laki. Hal ini dapat dilihat dari persentase mahasiswa perempuan sekitar 64% dan mahasiswa laki-laki 35%.
- Jika dilihat dari sebaran mahasiswa berdasarkan usia pendaftaran, terdapat rentang usia yang cukup jauh yaitu dari 18 hingga 27 tahun.
- Lebih banyak pemegang beasiswa yang berhasil menyelesaikan kuliahnya dengan baik hingga lulus, dibandingkan yang akhirnya dropout.
- Mahasiswa yang lulus, memiliki nilai yang lebih tinggi untuk faktor-faktor tersebut, dengan nilai rata-rata mata kuliah yang diselesaikan di semester 1 dan 2 sebesar 12 dari total penilaian 20, dan jumlah mata kuliah yang berhasil diselesaikan sebanyak rata-rata 6 mata kuliah. Sedangkan, untuk mahasiswa yang dropout, memiliki nilai yang terendah untuk semua faktor

## Menjalankan Sistem Machine Learning
- Install streamlit pada perangkat.
- Run perintah streamlit run app.py pada command prompt atau terminal

## Conclusion

- Pada Jaya Jaya Institute, terdapat 2,209 mahasiswa yang telah lulus, sedangkan untuk mahasiswa yang dropout mencapai 1421 mahasiswa.
- Mahasiswa didominasi oleh kaum perempuan dengan persentase mencapai 64%.
- Usia pendaftar terbanyak yaitu pada usia 18 tahun.
- Pemegang beasiswa lebih banyak berhasil menyelesaikan kuliah, dibandingkan dengan yang dropout.
- Mahasiswa yang lulus memiliki nilai rata-rata mata kuliah yang diselesaikan di semester 1 dan 2 sebesar 12 dari total penilaian 20, dan jumlah mata kuliah yang berhasil diselesaikan sebanyak rata-rata 6 mata kuliah. 

### Rekomendasi Action Items (Optional)
Tindakan yang dapat dilakukan untuk mencegah dropout adalah dengan memberikan perhatian kepada mahasiswa yang memiliki nilai rata-rata mata kuliah yang lebih rendah daripada 12, serta memiliki jumlah mata kuliah yang berhasil diselesaikan kurang dari 6 atau dapat dikatakan kurang dari nilai yang diperoleh mahasiswa yang berhasil lulus.
