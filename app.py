import streamlit as st
import requests
import pandas as pd
import os

# Get API URL from environment variable or use default
API_URL = os.environ.get("API_URL", "http://localhost:8000")

# Then use this URL in your API calls
# For example:
response = requests.get(f"{API_URL}/models")

st.set_page_config(
    page_title="FrugalAI",
    page_icon="🌍",
)

st.sidebar.success("Select a page above")

st.title("Frugal AI")
st.write("The world's greatest tool to fight climate change misinformation")

# # Get available models from API
# def get_models():
#     try:
#         response = requests.get(f"{API_URL}/models")
#         if response.status_code == 200:
#             return response.json().get("available_models", {})
#         else:
#             st.error(f"Error fetching models: {response.status_code}")
#             return {}
#     except Exception as e:
#         st.error(f"Could not connect to API: {e}")
#         return {}

# Available models
# models_dict = get_models()
model_names = ["ClimateDetector"]


#input field
with st.form("frugal"):
    user_input = st.text_input("Copy-paste here the article you want to analyze:", placeholder="Copy-paste here...")

    # Model selection
    selected_model = st.selectbox("Select model:", model_names)

# Every form must have a submit button
    submitted = st.form_submit_button("GO!")

    if submitted:
        if user_input:
            # Show loading spinner
            with st.spinner('Analyzing your text...'):
                try:
                    # API call
                    payload = {
                        "quote": user_input,
                        "model": selected_model
                    }

                    response = requests.post(f"{API_URL}/predict/", json=payload)
                    print(f"{API_URL}/predict/")

                    if response.status_code == 200:
                        apiresult = response.json()
                    else:
                        st.error(f"Error from API: {response.status_code}")
                        apiresult = {
                            "category": "7",  # Fallback
                            "gCo2eq": "4",
                            "model_name": selected_model,
                            "accuracy": "N/A",
                            "F1": "N/A",
                            "prediction_time_seconds": 0
                        }
                except Exception as e:
                    st.error(f"Error connecting to API: {e}")
                    # Fallback for demo or development
                    apiresult = {
                        "category": "7",
                        "gCo2eq": "4",
                        "model_name": selected_model,
                        "accuracy": "N/A",
                        "F1": "N/A",
                        "prediction_time_seconds": 0
                    }

            #convert to dataframe
            df = pd.DataFrame([apiresult])

             # Get the category value
            category = str(df['category'].iloc[0])
            F1score = str(df['F1'].iloc[0]) if 'F1' in df.columns else "N/A"

            # Display different text based on the category value
            if category == "0":
                # Display prediction information
                st.write("No relevant claim detected or claims that don't fit other categories")
                st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2t6YW16NW5rZGRndHZuYmtyamhkdzNuaHl6aHh5M284enIzOXdxMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/121YQW1OQhqGLS/giphy.gif", caption="Category 0", width=300)
                st.write("Our model has detected that the claim is irrelevant.")
                # Display model information
                st.write(f"Analysis confidence score : {F1score}%")
                st.write("The claim either isn't about climate or isn’t disinformation.")

            elif category == "1":
                # Display prediction information
                st.write("Our model has flagged this claim as one that denies global warming.")
                st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3dscG90aTBtdXB0Y2EwbGlzcGZ5MWR3dTYyZWRyZGt4d2RmMmM3bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TJawtKM6OCKkvwCIqX/giphy.gif", caption="Category 1", width=300)
                # Display model information
                st.write(f"Analysis confidence score: {F1score}%")
                st.write("""Yet the facts tell a different story: In the last 30 years, glacier melt has increased by 65% and sea levels have risen by 10 cm. Western Europe is especially affected by global warming, with temperatures increasing 30% faster than the global average.""")


            elif category == "2":
                # Display prediction information
                st.write("Our model has detected that the claim is denying human responsibility in climate change")
                st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjhqeGN6NzIwenFxeGUzY2E5b2c2Ym54bmg1eXFrcnd4N25leXBtZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ANbD1CCdA3iI8/giphy.gif", caption="Category 2", width=300)
                # Display model information
                st.write(f"Analysis confidence score : {F1score}%")
                st.write(f"According to IPCC scientists, human activities are responsible for 95% of global warming. This is due to fossil fuels such as oil, coal, or natural gas, deforestation, and certain industrial and agricultural processes.")
                st.image("https://reseauactionclimat.org/wp-content/uploads/2023/01/giec-flgure-rid1-gif-699x566.gif")

            elif category == "3":
                # Display prediction information
                st.write("Our model has detected that the claim is minimizing or denying negative impacts of climate change.")
                st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzRnbmNkYW0xbTAxamtyNDNrN2tzYWZvZDN6M3VndzJjcHY0NHpuMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wr7oA0rSjnWuiLJOY5/giphy.gif", caption="Category 3", width=300)
                # Display model information
                st.write(f"Analysis confidence score : {F1score}%")
                st.write("Global warming leads to an increase in extreme events : droughts, floods, sea level rise and threatened biodiversity… By 2100, we can expect 10 times as many heatwave days as there are currently.")

            elif category == "4":
                # Display prediction information
                st.write("Our model has detected that the claim asserts that climate solutions are unnecessary—or even harmful.")
                st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2Iwc2g3dThqeHU2dTUzOGc3ZHhzczdqbXFmcXVvaGVlcjNic3Z6ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ui4VjMUBGXhwgdwUnK/giphy.gif", caption="Category 4", width=300)
                # Display model information
                st.write(f"Analysis confidence score: {F1score}%")
                st.write("To meet the Paris Agreement—which targets a global warming limit of +2°C—we must limit emissions to 2 tons of CO2 per capita. Today, the French average is 10 tons per capita.")
                st.write("Not only are climate solutions necessary, but we need to do even more!")

            elif category == "5":
                # Display prediction information
                st.write("Our model has detected that the claim questions the validity of climate science.")
                st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXlqc3l6b3J6d3p1b2JnNWRibTdrbzZ0NHZwMnY1cDBzYnRvZGZpdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/11vQbiTMSDx0o8/giphy.gif", caption="Category 5", width=300)
                # Display model information
                st.write(f"Analysis confidence score: {F1score}%")
                st.write("But the consensus is clear: 97% of climate experts agree that global warming is primarily caused by human activities.")


            elif category == "6":
                # Display prediction information
                st.write("Our model has detected that the claim is attacking climate scientists and activists.")
                st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3hoaTUzemo4bmpwa2Jmdmxjb2hja3g2Y2lpMmcyamRzdHZ5cTJ3ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ghuvaCOI6GOoTX0RmH/giphy.gif", caption="Category 6", width=300)
                # Display model information
                st.write(f"Analysis confidence score : {F1score}%")
                st.write("Here's the reality: IPCC scientists don’t conduct original research or issue recommendations—they compile and synthesize existing climate science from tens of thousands of studies.")
                st.write("Their reports, seen as the most comprehensive snapshot of the subject, are the result of a rigorous, transparent review process, with all sources available online.")


            elif category == "7":
                # Display prediction information
                st.write("Our model has flagged this claim as promoting fossil fuels as essential for economic growth, prosperity, and maintaining our standard of living.")
                st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHA4dmVzbDYwN3g0YXg5ZWI3eHdreGl0NWU0cDlta3Z0eDdwbHd0bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/9M5jK4GXmD5o1irGrF/giphy.gif", caption="Category 7", width=300)
                # Display model information
                st.write(f"Analysis confidence score: {F1score}%")
                st.write("But in reality, clean energy contributed about US$320 billion to the global economy last year, making up 10% of global GDP growth.")
            else:
                st.write("Unknown category.")

        else:
            st.error("Please enter some text before submitting")
