import tkinter as tk
from tkinter import ttk
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\Documents\Profile\SkillsPage\build\assets\frame0")
window = tk.Tk()
window.title("Multiple Selection Combobox")

window.geometry("700x450")
window.configure(bg = "#173054")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def on_configure(event):
    # update scroll region to encompass the full canvas
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_drag_start(event):
    widget = event.widget
    item = widget.find_closest(event.x, event.y)
    item_text = widget.itemcget(item, "text")
    widget.drag_data = {"item": item, "x": event.x, "y": event.y, "text": item_text}

def on_drag_motion(event):
    widget = event.widget
    x, y = event.x, event.y
    widget.move(widget.drag_data["item"], x - widget.drag_data["x"], y - widget.drag_data["y"])
    widget.drag_data["x"] = x
    widget.drag_data["y"] = y

def on_drag_end(event):
    widget = event.widget
    item = widget.find_closest(event.x, event.y)
    item_text = widget.drag_data["text"]
    selected_listbox.insert(tk.END, item_text)
    del widget.drag_data
def update_list(event):
    category = category_combobox.get()
    if category == "Programming Languages":
        update_canvas(programming_languages)
    elif category == "Frameworks and Libraries":
        update_canvas(frameworks_and_libraries)
    elif category == "Mobile Development":
        update_canvas(mobile_development)
    elif category == "Web Development":
        update_canvas(web_development)
    elif category == "UI/UX Design":
        update_canvas(ui_ux_design)
    elif category == "Game Development":
        update_canvas(game_development)
    elif category == "Software Engineering":
        update_canvas(software_engineering)
    elif category == "Cloud Computing":
        update_canvas(cloud_computing)
    elif category == "Security":
        update_canvas(security)
    elif category == "Data Science and Analytics":
        update_canvas(data_science_and_analytics)
    elif category == "Database Management":
        update_canvas(database_management)
    elif category == "Development Tools":
        update_canvas(development_tools)
    elif category == "Blockchain":
        update_canvas(blockchain)
    elif category == "Internet of Things (IoT)":
        update_canvas(Iot)
    elif category == "AI and Robotics":
        update_canvas(AI_and_Robotics)
    elif category == "Virtual Reality and Augmented Reality (VR/AR)":
        update_canvas(VR_AR)
    elif category == "Graphics Design":
        update_canvas(graphics_design)
    elif category == "User Interface":
        update_canvas(user_interface)
    elif category == "Project Management":
        update_canvas(project_management)
    elif category == "Business Skills":
        update_canvas(business_skills)
    elif category == "Regulatory Compliance":
        update_canvas(regulatory_compliance)
    elif category == "Sustainability":
        update_canvas(sustainability)
    elif category == "Networking":
        update_canvas(networking)
    elif category == "Systems":
        update_canvas(systems)
    elif category == "Real Estate":
        update_canvas(realestate)
    elif category == "Communication":
        update_canvas(communication)
    elif category == "Management and Leadership":
        update_canvas(management_and_leadership)
    elif category == "Personal Development":
        update_canvas(personal_development)
    elif category == "Legal and Ethical":
        update_canvas(legal_and_ethical)
    elif category == "Technical Proficiency":
        update_canvas(Technical_proficiency)
    elif category == "Digital Collaboration":
        update_canvas(Digital_collaboration)

def update_canvas(items):
    canvas.delete("all")
    y_offset = 10
    for item in items:
        canvas.create_text(10, y_offset, anchor="w", text=item, font=("Helvetica", 12))
        y_offset += 25
    canvas.config(scrollregion=canvas.bbox("all"))

# Define available items
programming_languages = ["C#", "Java", "JavaScript"," Python", "PHP", "Kotlin", "Swift", "C++", "Bash", "R", "SQL"]
frameworks_and_libraries = ["NET", "Unity", "TensorFlow", "Keras", "React Native"," Xamarin", "Angular", "Node.js", "React", "Flask", "D3.js", "OpenCV"]
mobile_development = ["Android Development", "iOS Development (Swift, Kotlin)", "React Native", "Xamarin", "Mobile Development Best Practices", "Flutter", "HealthKit", "CareKit"]
web_development = ["HTML", "CSS", "JavaScript", "SEO Tools", "Web Development", "Web Scraping", "Web Crawling", "HTML5", "CSS3", "Drupal", "WordPress"]
ui_ux_design = ["Sketch", "Figma", "Adobe XD", "User Interface Design", "User Experience Design", "UI/UX Design"]
game_development = ["Unity", "Game Design Principles"]
software_engineering = ["Software Maintenance", "Enterprise Architecture", "Algorithm Design", "Application Development", "System Integration", "Application Design"]
cloud_computing = ["AWS", "Azure", "Cloud Computing Fundamentals", "Serverless Architecture", "Cloud Storage Solutions"]
security = ["Cybersecurity", "Encryption", "SSL", "Payment Processing APIs", "Network Security", "Ethical Hacking", "Data Security", "Information Security", "Authentication", "Biometric Identification"]
data_science_and_analytics = ["Machine Learning", "Data Analysis", "Big Data Analytics", "Data Analytics", "Data Visualization", "Data Science", "Statistical Analysis", "Predictive Modeling", "Fraud Detection Algorithms", "Health Informatics", "Quantitative Analysis", "Financial Modeling", "Statistics"]
database_management = ["Database Management", "MySQL", "MongoDB", "Oracle", "SQL Optimization", "Database Management", "Performance Tuning"]
development_tools = ["Docker", "Kubernetes", "Selenium", "Test Automation Frameworks", "Version Control", "CI/CD Pipelines"]
blockchain =["Solidity", "Ethereum", "Smart Contracts", "Blockchain Concepts", "DApp Development"]
Iot =["IoT Platforms", "IoT Integration", "Sensor Networks", "Arduino", "Raspberry Pi"]
AI_and_Robotics = ["AI Principles", "Machine Learning Algorithms", "Robotics", "Embedded Systems", "AI Concepts", "Computer Vision", "Image Processing", "Speech Recognition Libraries", "NLP Techniques", "Chatbot Frameworks"]
VR_AR = ["VR SDKs"]
graphics_design = ["Adobe Suite", "Blender", "Maya", "3D Graphics"]
user_interface =["Sketch", "Figma", "Adobe XD"]
project_management = ["Project Management Methodologies", "Agile", "Scrum", "Analytical Skills", "Team Collaboration", "Leadership"]
business_skills = ["Market Research", "Customer Behavior Analysis", "Market Analysis", "Strategic Planning", "Business Strategy", "Operational Efficiency", "Financial Planning", "Fundraising Strategies", "Competitive Intelligence", "Strategic Analysis", "Product Development", "Creativity"]
regulatory_compliance = ["Legal Knowledge", "Ethical Decision Making", "Regulatory Compliance", "Environmental Law", "Data Protection Policies", "Banking and Finance Knowledge"]
sustainability = ["Sustainability Planning", "Environmental Science", "Sustainability Strategies"]
networking = ["Networking", "Socket Programming", "Multi-thread Programming"]
systems = ["Satellite Systems", "Communication Theory", "Signal Processing", "Circuit Analysis", "Circuit Design", "Soldering", "Energy Systems", "Mechanical Analysis"]
realestate = ["Real Estate Knowledge"]
communication =["Interpersonal Communication", "Active Listening", "Customer Service", "Empathy", "Communication Skills"]
management_and_leadership = ["Organizational Development", "Leadership", "Employee Motivation Techniques", "Feedback Mechanisms", "Constructive Criticism", "Team Management", "Change Management"]
personal_development = ["Time Management", "Stress Management", "Self-Discipline", "Self-Motivation Techniques", "Continuous Learning", "Adaptability"]
legal_and_ethical = ["Legal Knowledge", "Ethical Decision Making"]
Technical_proficiency = ["Technical Skills", "Technical Adaptability"]
Digital_collaboration = ["Digital Collaboration Tools"]
# Create category dropdown
categories = ["Programming Languages","Frameworks and libraries","Mobile Development","Web Development","UI/UX Design","Game Development","Software Engineering","Cloud Computing","Security","Data Science and Analytics","Database Management","Development Tools","Blockchain","IoT","AI and Robotics","VR/AR","Graphic Design","User Interface Design","Project Management","Business Skills","Regulatory and Compliance"," Sustainability","Networking","Systems","Real Estate","Communication","Management and Leadership","Personal Development","Legal and Ethical","Technical Proficiency","Digital Collaboration"]
'''
canvas = tk.Canvas(
    window,
    bg = "#173054",
    height = 450,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    350.0,
    225.0,
    image=image_image_1
)
canvas.create_text(
    162.0,
    34.0,
    anchor="nw",
    text="Choose Your Skill :",
    fill="#FFFFFF",
    font=("LibreCaslonText Regular", 17 * -1)
)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    472.5,
    44.5,
    image=entry_image_1
)'''

category_combobox = ttk.Combobox(window, values=categories)
category_combobox.place(x=351, y=30, width=244, height=30)
category_combobox.bind("<<ComboboxSelected>>", update_list)


# Frame for available options
#available_frame = ttk.LabelFrame(window, text="Available Options")
#available_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

canvas_frame = ttk.Frame(window,width=303.0,
    height=253.0)
canvas_frame.place(
    x=26.0,
    y=103.0,
    
    )

# Add a canvas to the frame
canvas = tk.Canvas(window, bg="white", highlightthickness=0)
canvas.place(x=26, y=103, height=253, width=300)

# Add a vertical scrollbar to the canvas frame
vsb = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
vsb.pack(side="right", fill="y")
canvas.config(yscrollcommand=vsb.set)

# Bind the scrollbar to the canvas
canvas.bind("<Configure>", on_configure)
canvas.bind("<Button-1>", on_drag_start)
canvas.bind("<B1-Motion>", on_drag_motion)
canvas.bind("<ButtonRelease-1>", on_drag_end)

# Create a listbox frame
listbox_frame = ttk.Frame(window, width=303, height=253)
listbox_frame.place(x=374, y=103)

# Create the listbox
selected_listbox = tk.Listbox(listbox_frame, selectmode=tk.MULTIPLE)
selected_listbox.place(x=0, y=0,width=303, height=253)

# Add a vertical scrollbar to the listbox frame
vsb_listbox = tk.Scrollbar(selected_listbox, orient="vertical", command=selected_listbox.yview)
vsb_listbox.place(x=374, y=103)
selected_listbox.config(yscrollcommand=vsb_listbox.set)
'''canvas.create_text(
    47.0,
    85.0,
    anchor="nw",
    text="Available options:-",
    fill="#FFFFFF",
    font=("LibreCaslonText Regular", 13 * -1)
)

canvas.create_text(
    392.0,
    84.0,
    anchor="nw",
    text="Selected options:-",
    fill="#FFFFFF",
    font=("LibreCaslonText Regular", 13 * -1)
)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=287.0,
    y=385.0,
    width=126.0,
    height=36.0
)'''

window.mainloop()