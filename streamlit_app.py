import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title('My Parents new healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocdo and tost')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_fruit_list)


# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(my_fruit_list)
#################################################################################

#Create the repetable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)  ##/watermelon")
     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
     return fruityvice_normalized
    
###### New Section to disply fruityvice api response ################
streamlit.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')####,'Kiwi')    
    if not fruit_choice :
       streamlit.error("Please select fruit to get information.")
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)       
except URLError as e:
     streamlit.error()
  
##Don't run anythong past while we trubleshoot
#streamlit.stop()

##my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
##streamlit.text("Hello from Snowflake:")

streamlit.header("The Fruit load list contains:")
#snoflake related functions 
def get_fruit_load_list():
     with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from fruit_load_list") 
         return my_cur.fetchall()

#Add a button to load the fruit 
if streamlit.button('Get Fruit Load List')
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     my_data_rows = get_fruit_load_list()
     streamlit.dataframe(my_data_rows)


##to load all rows 
##my_data_rows = my_cur.fetchall()
##streamlit.text("Hello from Snowflake:")
##streamlit.header("Fruit load list contains:")
##streamlit.dataframe(my_data_rows)

add_my_frit = streamlit.text_input('What fruit would you like to add ?','jackfruit')
streamlit.write('The user entered ', add_my_frit)
my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
