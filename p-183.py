from tkinter import *
import requests
import json

root=Tk()
root.title("My country App")
root.geometry("200x200")
root.configure(background="white")

city_name_label=Label(root, text="City Name",font=("Helvetica", 18,'bold'),bg="white")
city_name_label.place(relx=0.5,rely=0.15,anchor=CENTER)
city_entry=Entry(root)
city_entry.place(relx=0.5,rely=0.35,anchor=CENTER)
country_name_label=Label(root, text="Country Name",font=("Helvetica", 18,'bold'),bg="white")
country_name_label.place(relx=0.5,rely=0.45,anchor=CENTER)
region_name_label=Label(root, text="Region Name",font=("Helvetica", 18,'bold'),bg="white")
region_name_label.place(relx=0.5,rely=0.55,anchor=CENTER)
language_name_label=Label(root, text="Language Name",font=("Helvetica", 18,'bold'),bg="white")
language_name_label.place(relx=0.5,rely=0.65,anchor=CENTER)
population_name_label=Label(root, text="population Name",font=("Helvetica", 18,'bold'),bg="white")
population_name_label.place(relx=0.5,rely=0.75,anchor=CENTER)
Area_name_label=Label(root, text="Area Name",font=("Helvetica", 18,'bold'),bg="white")
Area_name_label.place(relx=0.5,rely=0.85,anchor=CENTER)

def city():
    api_request = requests.get("https://restcountries.com/v2/capital/"+city_entry.get())
    
    api_output_json = json.loads(api_request.content)
    
    country=api_output_json[0]['name']['common']
    reigon=api_output_json[0]['region']
    language=api_output_json[0]['language']
    population=api_output_json[0]['population']
    area=api_output_json[0]['area']
    country_name_label["text"]= "Country"+country
    region_name_label["text"]= "Region"+region
    language_name_label["text"]= "Language"+language
    population_name_label["text"]= "Population"+population
    Area_name_label["text"]= "Area"+area
    
search=Button(root,text="Search",command=city) 
search.place(relx=0.5,rely=0.95,anchor=CENTER)   

root.mainloop()