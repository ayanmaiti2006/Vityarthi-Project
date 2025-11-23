### Introduction / Description



This project identifies whether a banking APK is genuine or fake by analyzing app permissions, APK metadata, certificate signatures, file size, package name patterns, and suspicious behaviors. It helps users avoid phishing and financial fraud by providing a quick security check.





### &nbsp;Features



Detects fake or malicious banking APKs



Analyzes permissions and flags dangerous ones



Extracts APK metadata (package name, version, size)



Verifies certificate signature authenticity



Uses rule-based + ML-based detection



Generates detailed safety reports



Fast and lightweight system







---



### Installation Steps



1\. Install Python 3.8+





2\. Install dependencies:



pip install apkutils python-magic joblib scikit-learn





3\. Place the APK file inside the project folder





4\. Run the script:



python detect\_apk.py









### Usage Instructions



1\. Launch the script





2\. Upload or give the path of the APK





3\. The system extracts the APK features





4\. ML model + rule engine analyze the APK





5\. Final output shows SAFE / SUSPICIOUS / MALICIOUS







### Technologies Used



Python



Machine Learning (Scikit-Learn)



APKUtils for APK analysis



Certificate verification tools



Rule-based detection engine

