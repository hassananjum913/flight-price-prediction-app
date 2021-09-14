import streamlit as st
from PIL import Image
import pickle

model = pickle.load(open('./Model/rf.pkl', 'rb'))


def run():
    img1 = Image.open('flight.jpg')
    img1 = img1.resize((300, 200))
    st.image(img1, use_column_width=False)
    st.title("Flight Price Prediction using Machine Learning")
    st.subheader('Please Enter the following details to Predict Loan Eligibility Status')


     # ------ Airlines----------
    Airline_Air_India =0
    Airline_GoAir = 0
    Airline_IndiGo = 0
    Airline_Jet_Airways = 0
    Airline_Jet_Airways_Business = 0
    Airline_Multiplecarriers = 0
    Airline_Multiplecarriers_Premiumeconomy = 0
    Airline_Vistara = 0
    Airline_Vistara_Premiumeconomy = 0

    # ---- Source ------------

    Source_Chennai = 0
    Source_Delhi = 0
    Source_Kolkata = 0
    Source_Mumbai = 0

    # -------- Destination ---------

    Destination_Delhi = 0
    Destination_Hyderabad = 0
    Destination_Kolkata = 0
    Destination_New_Delhi =0

    # --------Additional Info----
    Additional_Info_2Longlayover = 0
    Additional_Info_In_flight_meal_not_included = 0
    Additional_Info_No_check_in_baggage_included = 0

    col1, col2 , col3 = st.columns(3)

    with col1:
        # Total stop
        total_stop = 0
        ts = st.radio('Select Number of Stops:',['Non_stop','1 stop','2 stop','3 stop','4 stop'])
        if ts == 'Non_stop':
            total_stops = 0
        elif ts =='1 stop':
            total_stops = 1
        elif ts =='2 stop':
            total_stop = 2
        elif ts == '3 stop':
            total_stop = 3
        else:
            total_stop = 4

        # Journey Day
        journey_day = st.slider('Select Journey Date: ', 1, 31)

        # Journey Month
        journey_month = st.slider('Select Journey Month: ', 1, 12)

    with col2:
        # Dept Hour and Min

        hr = st.time_input('Enter Hour and Min for Departure:')

        dep_hr = hr.hour
        dep_min = hr.minute

        # Arrival Hour and Min

        hr2 = st.time_input('Enter Hour and Min for Arrival:')

        arrival_hr = hr2.hour
        arrival_min = hr2.minute

        # Duration
        dur_hr = st.slider('Enter flight duration in hours: ', 0, 100, 1)
        dur_min = st.slider('Enter flight duration in minutes: ',0,100,1)


        # Airline
        airline_list = ['Air India','GoAir','IndiGo','Jet Airways','Jet Airways Business',
              'Multiple carriers','Multiple carriers Premium economy','Vistara','Vistara Premium economy']

        al = st.selectbox('Select Airline Details: ', airline_list)
        if al =='Air India':
            Airline_Air_India = 1
        elif al == 'GoAir':
            Airline_GoAir = 1
        elif al == 'Indigo':
            Airline_IndiGo = 1
        elif al == 'Jet Airways':
            Airline_Jet_Airways = 1
        elif al == 'Jet Airways Business':
            Airline_Jet_Airways_Business = 1
        elif al == 'Multiple carriers':
            Airline_Multiplecarriers = 1
        elif al == 'Multiple carriers Premium economy':
            Airline_Multiplecarriers_Premiumeconomy = 1
        elif al == 'Vistara':
            Airline_Vistara = 1
        else:
            Airline_Vistara_Premiumeconomy = 1

    with col3:     # Source

        source_list = ['Chennai','Delhi','Kolkata','Mumbai']
        sr = st.selectbox('Select Source Details: ', source_list)
        if sr == 'Chennai':
            Source_Chennai = 1
        elif sr == 'Delhi':
            Source_Chennai = 1
        elif sr == 'Kolkata':
            Source_Kolkata = 1
        else:
            Source_Mumbai = 1

        # Destination
        dest_list = ['Delhi','Hyderabad','Kolkata','New Delhi']
        dest = st.selectbox('Select Destination Details: ', dest_list)
        if dest == 'Delhi':
            Destination_Delhi = 1
        elif dest == 'Hyderabad':
            Destination_Hyderabad = 1
        elif dest == 'Kolkata':
            Destination_Kolkata = 1
        else:
            Destination_New_Delhi = 1

         # Additional Info
        add_info_list = ['2 Long layover','In-flight meal not included','No check-in baggage included']
        ai  = st.selectbox('Select Additional Information: ', add_info_list)
        if ai == '2 Long layover':
            Additional_Info_2Longlayover = 1
        elif ai == 'In-flight meal not included':
            Additional_Info_In_flight_meal_not_included = 1
        else:
            Additional_Info_No_check_in_baggage_included = 1



    features = [total_stop,journey_day,journey_month,dep_hr,dep_min,arrival_hr,arrival_min,dur_hr,dur_min,
                     Airline_Air_India,Airline_GoAir,Airline_IndiGo,Airline_Jet_Airways,Airline_Jet_Airways_Business,
                     Airline_Multiplecarriers,Airline_Multiplecarriers_Premiumeconomy,Airline_Vistara,Airline_Vistara_Premiumeconomy,
                     Source_Chennai,Source_Delhi,Source_Kolkata,Source_Mumbai,Destination_Delhi,Destination_Hyderabad,
                     Destination_Kolkata,Destination_New_Delhi,Additional_Info_2Longlayover,Additional_Info_In_flight_meal_not_included,
                      Additional_Info_No_check_in_baggage_included]

    print(features)

    if st.button("Predict Flight Price"):
        predictions = model.predict([features])[0]
        st.success(f'The Predicted Flight Price is {predictions}')

run()
