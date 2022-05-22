# Heart-Disease-Prediction
Predicts the presence of one of four types of heart disease(or none at all) using a patient's medical test report data.

## Dataset
The [Heart disease data set](https://archive.ics.uci.edu/ml/datasets/heart+Disease) consists of patient data from Cleveland, Hungary, Long Beach and Switzerland. The combined dataset consists of 14 features and 916 samples with many missing values. 
The features used in here are,
1. age: The patients age in years
2. sex: The patients gender(1=male; 0=female)
3. cp: Chest pain type,
	*Value 1: typical angina 
	*Value 2: atypical angina 
	*Value 3: non-anginal pain 
	*Value 4: asymptomatic 
4. trestbps: Resting blood pressure (in mm Hg on admission to the hospital)
5. chol: Serum cholestoral in mg/dl
6. fbs: Fasting blood sugar > 120 mg/dl? (1=true; 0=false) 
7. restecg: Resting electrocardiographic results
	*Value 0: normal 
	*Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) 
	*Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria 
8. thalach: Maximum heart rate achieved
9. exang: Chest pain(angina) after exercise? (1=yes; 0=no)
10. thal: Not described 
	*Value 3=normal
	*Value 6=treated defect 
	*Value 7=reversible defect 
11. num: Target
	*Value 0: less than 50% narrowing of coronary arteries(no heart disease)
	*Value 1,2,3,4: >50% narrowing. The value indicates the stage of heart disease

Dataset creators,
1. Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D. 
2. University Hospital, Zurich, Switzerland: William Steinbrunn, M.D. 
3. University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D. 
4. V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D. 

## Running the web app
#### Locally
- Install requirements  
   `pip install -r requirements.txt`
- Run flask web app  
    `python main_file.py`

## Models used and accuracy
A Random forest classifier achieves an average multi-class classification accuracy of 56-60%(183 test samples).
It gets 75-80% average binary classification accuracy(heart disease or no heart disease).



https://user-images.githubusercontent.com/49685839/169673598-3de1cc01-64a4-4316-8657-512f8ecdade9.mp4
![Capture](https://user-images.githubusercontent.com/49685839/169673754-01aea12c-6c43-431c-931b-ad33a38cceb7.PNG)
![Capture1](https://user-images.githubusercontent.com/49685839/169673756-1691f5b4-509c-4ab1-acdb-19d2bc9a5f65.PNG)
![Capture2](https://user-images.githubusercontent.com/49685839/169673757-5f8c20db-165d-43cc-a29d-c7ba6914e341.PNG)
![Capture3](https://user-images.githubusercontent.com/49685839/169673758-b30213a3-01bb-4070-a4dc-33b82403fdc6.PNG)
![Capture4](https://user-images.githubusercontent.com/49685839/169673759-25fb2052-bf78-469f-984f-6fcad38fa97d.PNG)
![Capture5](https://user-images.githubusercontent.com/49685839/169673760-c54faf50-d2f3-4dfc-befa-b5fb798580f7.PNG)
![Capture6](https://user-images.githubusercontent.com/49685839/169673761-5ad4db6a-5d60-4043-ae49-9e8704c8a20b.PNG)
![Capture7](https://user-images.githubusercontent.com/49685839/169673762-091144d2-90e7-4e4b-9f6d-2e0d26438a3e.PNG)
![Capture8](https://user-images.githubusercontent.com/49685839/169673763-5c31507b-77b2-4f6a-8fe2-9dfff2129545.PNG)
![Capture9](https://user-images.githubusercontent.com/49685839/169673764-c22da6ba-ff75-4f61-bcd1-6b6160ffc8ae.PNG)
![Capture10](https://user-images.githubusercontent.com/49685839/169673766-3b143150-4603-4f9b-a912-c847e6c7ad94.PNG)
![COMPARISON OF MODELS](https://user-images.githubusercontent.com/49685839/169673767-dd8a206e-fad1-4556-863f-27129a5a1b21.png)

