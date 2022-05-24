import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)

# pickle_in = open('classifier.pkl', 'rb') 
# classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,
               Oldpeak,ST_Slope):   
 
    # Pre-processing user input
    if Age == "Old":
      Age=50
    elif Age == "Adult":
      Age=30
    else:
      Age=15

    if Sex == "Male":
        Sex = 0
    else:
        Sex = 1
        
    if ChestPainType == "TA":
      ChestPainType=3
    elif ChestPainType == "ATA":
      ChestPainType=1
    elif ChestPainType == "NAP":
      ChestPainType=2
    else:
      ChestPainType=0

    if RestingBP == "Very_High":
       RestingBP=200
    elif RestingBP == "High":
       RestingBP=150   
    else:
       RestingBP=130


    if FastingBS == ">120 mg/dl":
       FasttingBS=1
    else:
       FastingBS=0 
    if Oldpeak == "Very_High":
        Oldpeak=5
    elif Oldpeak == "high":    
         Oldpeak=3.5
    else:
        Oldpeak=1

    if ST_Slope == "Up":
      ST_Slope=2
    elif ST_Slope == "Flat":
      ST_Slope=1
    else:
        ST_Slope=0

    if Cholesterol == "Very_High":
      Cholestrol=350
    elif Cholesterol == "Medium":
      Cholesterol=300
    else:
      Cholesterol=200  

    if MaxHR == "Very_High":
        MaxHR=190
    elif MaxHR == "High":
        MaxHR=150      
    else:
        MaxHR=90
 
    if RestingECG == "Normal":
       RestingECG  = 2
    if RestingECG == "LVH":
        RestingECG = 1  
    else:
        RestingECG = 0

    if ExerciseAngina == "No":
        ExerciseAngina = 0
    else:
        ExerciseAngina = 1
 
    
 
    # Making predictions 
    prediction = classifier.predict( 
        [[Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,
               Oldpeak,ST_Slope]])
     
    if prediction == 0:
        pred = 'Person does not have heart disease'
    else:
        pred = 'Person has a higher probability of having heart disease'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:blue;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Heart Disease Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Age = st.selectbox('Age',("Old","Adult","Young"))
    Sex = st.selectbox('Sex',("Male","Female")) 
    ChestPainType = st.selectbox('ChestPainType',("ATA","TA","NAP","ASY")) 
    RestingBP = st.selectbox('RestingBP',("Very High","High","Low")) 
    Cholesterol = st.selectbox('Cholesterol',("Very High","Medium","Low")) 
    FastingBS = st.selectbox('FastingBS',(">120mg/dl","<=120mg/dl")) 
    RestingECG = st.selectbox('RestingECG',("Normal","ST","LVH")) 
    MaxHR = st.selectbox('MaxHR',("Very High","High","Low")) 
    ExerciseAngina = st.selectbox('ExcerciseAngina',("Yes","No")) 
    Oldpeak = st.selectbox('Oldpeak',("very high","high")) 
    # ApplicantIncome = st.number_input("Applicants monthly income") 
    # LoanAmount = st.number_input("Total loan amount")
    ST_Slope = st.selectbox('ST_Slope',("Up","Flat","Down"))
    # result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,
               Oldpeak,ST_Slope) 
        st.success('Your Status:  {}'.format(result))
        #print(LoanAmount)
     
if __name__=='__main__': 
    main()