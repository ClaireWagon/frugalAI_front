import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="FrugalAI",
    page_icon="🌍",
)

st.sidebar.success("Select a page above")

st.title("Frugal AI")
st.write("The world's greatest tool to fight climate change misinformation")

#input field
with st.form("frugal"):
    user_input = st.text_input("Copy-paste here the article you want to analyze:", placeholder="Copy-paste here...")

# Every form must have a submit button
    submitted = st.form_submit_button("GO!")

    if submitted:
        if user_input:
            #api call
            #st.write("Calling API with: {user_input}")
            #response = requests.get(f" ##myendpoint")
            #apiresult = response.json()

            apiresult = {
            "category": ["0"],  # Predict
            "gCo2eq": ["4"],     # JSON
            "model_name": ["Test"],  # JSON
            "accuracy": ["test"],    # JSON
            "F1": ["test"]
            }

            #convert to dataframe
            df = pd.DataFrame(apiresult)

             # Get the category value
            category = df['category'][0]

            # Display different text based on the category value
            if category == "0":
                st.write("The article does not contain any climate misinformation")
                st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2t6YW16NW5rZGRndHZuYmtyamhkdzNuaHl6aHh5M284enIzOXdxMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/121YQW1OQhqGLS/giphy.gif", caption="Category 0", width=300)
            elif category == "1":
                st.write("This article implies that climate change doesn't exist")
                st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3dscG90aTBtdXB0Y2EwbGlzcGZ5MWR3dTYyZWRyZGt4d2RmMmM3bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TJawtKM6OCKkvwCIqX/giphy.gif", caption="Category 1", width=300)
            elif category == "2":
                st.write("This article denies any claim that humans don't have anything to do with climate change")
                st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjhqeGN6NzIwenFxeGUzY2E5b2c2Ym54bmg1eXFrcnd4N25leXBtZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ANbD1CCdA3iI8/giphy.gif", caption="Category 2", width=300)
            elif category == "3":
                st.write("This article claims that climate change is no big deal")
                st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzRnbmNkYW0xbTAxamtyNDNrN2tzYWZvZDN6M3VndzJjcHY0NHpuMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wr7oA0rSjnWuiLJOY5/giphy.gif", caption="Category 3", width=300)
            elif category == "4":
                st.write("This article rejects any possible solution")
                st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2Iwc2g3dThqeHU2dTUzOGc3ZHhzczdqbXFmcXVvaGVlcjNic3Z6ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ui4VjMUBGXhwgdwUnK/giphy.gif", caption="Category 4", width=300)
            elif category == "5":
                st.write("This article undermines the science behind climate change claims")
                st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXlqc3l6b3J6d3p1b2JnNWRibTdrbzZ0NHZwMnY1cDBzYnRvZGZpdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/11vQbiTMSDx0o8/giphy.gif", caption="Category 5", width=300)
            elif category == "6":
                st.write("This article claims that people who fight for climate change are hiding their ulterior motives")
                st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3hoaTUzemo4bmpwa2Jmdmxjb2hja3g2Y2lpMmcyamRzdHZ5cTJ3ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ghuvaCOI6GOoTX0RmH/giphy.gif", caption="Category 6", width=300)
            elif category == "7":
                st.write("This article defends the thesis that we should keen using fossil fuels")
                st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHA4dmVzbDYwN3g0YXg5ZWI3eHdreGl0NWU0cDlta3Z0eDdwbHd0bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/9M5jK4GXmD5o1irGrF/giphy.gif", caption="Category 7", width=300)
            else:
                st.write("Unknown category.")

            model_name = df['model_name'][0]
            co2 = df['gCo2eq'][0]
            accuracy = df['accuracy'][0]

            st.write(f"This model is based on the model {model_name} which consumed {co2} for its training. This model outputs a prediction with an accuracy of {accuracy}.")
            st.write("Accuracy tells you how often the machine's guesses are correct. For example, if the machine correctly identifies 90 out of 100 emails as spam or not spam, then its accuracy is 90%.")
            st.write("It's like a scorecard that shows how many times the model got it right out of all the times it made a guess.")

            #display the dataframe
            #st.dataframe(df)

        else:
            st.error("Please enter some text before submitting")
