import streamlit as st
html_string ="<h2>Welcome to Anudip Attendance</h2>"
html_string ="<h3>Important Files & Formats,Raw Data,AF Student Attendance Sheet</h3>"
st.markdown("<h2><u>Welcome to Anudip Attendance</u></h2>",unsafe_allow_html=True)
st.markdown("<h3>AF Student Attendance Sheet</h3>",unsafe_allow_html=True)

d=st.link_button('click here',"https://docs.google.com/spreadsheets/d/1quHVptis1NEwsYOmL6SAkqY2JNHcFTfa/edit?usp=drive_link&ouid=104259911200573651669&rtpof=true&sd=true")

# Important Files and Formats

st.markdown("<h3>Important Files & Formats</h3>",unsafe_allow_html=True)
d=st.radio('choose from here :',('AF_AE_Common Errors_Online Attendance','Attendance Calculation Error Format','Attendance Contact Details','Email ID Updation Request Form','Introduction to the Attendance Process','Timely Mobile Application Usage Guideline','Backcalculation Status'))
if d=='AF_AE_Common Errors_Online Attendance':
    st.link_button('View Here',"https://drive.google.com/file/d/14feCjndJ8eWssVHqOTSVvr39PW8iuZ7s/view?usp=drive_link")
     
elif d=='Attendance Calculation Error Format':     
     st.link_button('View Here',"https://docs.google.com/spreadsheets/d/1NXefhto03Eeyh36ODX8-yaaou1vMlIXm/edit?usp=drive_link&ouid=104259911200573651669&rtpof=true&sd=true")

elif d=='Attendance Contact Details':
     st.link_button('view Here',"https://drive.google.com/file/d/1UwoeioW_oPbX2LTEGVEMjrLPZnNMKqcQ/view?usp=drive_link")

elif d=='Email ID Updation Request Form':
     st.link_button('view Here',"https://docs.google.com/spreadsheets/d/1Kl8aPQlTs9UyzxTDhKMTz2wXmEs8ZmyK/edit?usp=drive_link&ouid=104259911200573651669&rtpof=true&sd=true")
                    
elif d=='Introduction to the Attendance Process':
     st.link_button('view Here',"https://drive.google.com/file/d/103n-KpQJ0NsmmzshRVn-GHZX5yZdX8-w/view?usp=drive_link")                    
                    
elif d=='Timely Mobile Application Usage Guideline':
     st.link_button('view Here',"https://drive.google.com/file/d/1YO5RY0y5YgfmOUbHocY6QJ_CDPFbRGVN/view?usp=drive_link")
                    
elif d=='Backcalculation Status':
     st.link_button('view Here',"https://docs.google.com/spreadsheets/d/1D8wGjUwXW3Xs-N31e9cNRw1FqbvIAH1c/edit?usp=drive_link&ouid=104259911200573651669&rtpof=true&sd=true")

# For Raw Data
     
st.markdown("<h3>Raw Data</h3>",unsafe_allow_html=True)
d=st.radio('choose from here :',("Online_Attendance_Raw_Data","Offline_Attendance_Raw_Data"))

if d=='Online_Attendance_Raw_Data':
    st.link_button('View Here',"https://docs.google.com/spreadsheets/d/1laeTmQDsM0xguT3XgzkCo20pYzj7yGuv/edit?usp=sharing&ouid=104259911200573651669&rtpof=true&sd=true")

elif d=='Offline_Attendance_Raw_Data':
     st.link_button('View Here',"https://docs.google.com/spreadsheets/d/1lctlg5q7nJDNI00vXWTRA-y8Dp-SJN_2/edit?usp=drive_link&ouid=104259911200573651669&rtpof=true&sd=true")