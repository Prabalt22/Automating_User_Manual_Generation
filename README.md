# Automating User Manual Generation

## Project Overview

**Automating User Manual Generation** is a Python-based desktop application developed during my internship at **Viprush Technology**.

The project was created to reduce the manual effort involved in preparing user manuals and software guidance documents for clients. Normally, after completing a software project, developers need to manually capture screenshots, add cursor indicators, write titles and descriptions, format the documentation, and finally prepare the document for delivery.

This application automates a major part of that workflow. The user can operate the target software normally, while the application captures screenshots after clicks, places a cursor indicator at the click location, and allows the user to add and edit documentation content. The completed manual can then be exported as a **PDF or Word document**.

The project took approximately **3 months** to complete.

---

## Problem Statement

Creating user manuals manually can be repetitive and time-consuming, especially when a document contains many screenshots and step-by-step instructions.

The main manual activities included:

- Taking screenshots for different steps.
- Identifying and indicating where the user clicked.
- Adding titles and descriptions for screenshots.
- Formatting the documentation.
- Organizing screenshots and generated files.
- Preparing the final document in a shareable format.

The objective of this project was to automate these repetitive tasks and make the documentation process faster and easier.

---

## Objective

The main objective was to automate as much of the user manual creation process as possible.

The project was estimated to reduce manual documentation effort by approximately **40%** based on the amount of repetitive screenshot and annotation work automated.

> **Note:** The 40% figure is an estimated reduction based on the workflow rather than a measurement obtained using a formal productivity model.

---

## Key Features

### 1. Create Document

The **Create Document** option starts the user manual creation workflow.

The application allows the user to:

- Select a folder name for the documentation.
- Use the current date and time as the default folder name.
- Select the software/application for which the manual needs to be created.
- Start the automated screenshot capture process.

### 2. Active Window Detection

The application detects running applications/windows and displays them for selection.

The user can select the target application or software window for which the manual is being created.

This functionality uses **PyGetWindow**.

### 3. Automatic Screenshot Capture

Once a target window is selected, the capture process begins.

When the user clicks on the selected application's UI:

1. The capture window temporarily minimizes.
2. A screenshot is automatically taken.
3. The application identifies the click location.
4. A cursor image is placed at the click position.
5. The capture window appears again.
6. The user can enter a title and description for the captured step.

This removes the need to manually take and annotate screenshots for every step.

### 4. Title and Description

After each screenshot is captured, the user can provide:

- Step title
- Step description

This information is used to explain the purpose of each screenshot in the final user manual.

### 5. Final Document Editor

After screenshot capture is completed, the application provides a final editing window.

The user can:

- Edit titles.
- Edit descriptions.
- Review captured screenshots.
- Apply basic text formatting.
- Use **Bold**, **Italic**, and **Underline** formatting.

### 6. Settings

The application includes a settings module where the user can configure:

- Cursor image size.
- Cursor type/image.
- Screenshot and document storage directory.
- Title block colour.

This allows the generated documentation to be customized according to the user's requirements.

### 7. PDF and Word Export

The completed manual can be exported into:

- **PDF**
- **Microsoft Word (.docx)**

The project uses `reportlab` for PDF generation and `python-docx` for Word document generation.

---

## Application Workflow

The overall workflow of the application is:

```text
Start
  ↓
Open Application
  ↓
Main Window
  ↓
┌───────────────────────┐
│ 1. Create Document    │
│ 2. Settings           │
└───────────────────────┘
        ↓
   If Settings
        ↓
Configure:
- Page size
- Cursor type
- Save directory
- Title block colour
        ↓
      Back to Main
        ↓
   Create Document
        ↓
Select Folder Name
(Default: Current Date & Time)
        ↓
Show Running Applications
        ↓
Select Target Window / Software
        ↓
Start Capture Process
        ↓
      [Loop]
        ↓
User clicks on target UI
        ↓
Capture window minimizes
        ↓
Screenshot is taken
        ↓
Cursor indicator is added
        ↓
Capture window appears again
        ↓
Add Title & Description
        ↓
Repeat for next step
        ↓
Capture Complete
        ↓
Final Editor Window
        ↓
Edit:
- Title
- Description
- Bold / Italic / Underline
        ↓
Export Document
        ↓
PDF / Word
        ↓
End
```

---

## Technologies Used

### Programming Language

- **Python**

### UI Development

- **Flet**

Flet was used to develop the desktop application's user interface and handle user interactions.

### Libraries

- **Pynput** – Used for mouse interaction and click event handling.
- **PyGetWindow** – Used for detecting and selecting running application windows.
- **Pillow (PIL)** – Used for image processing and screenshot-related operations.
- **python-docx** – Used for generating Word documents.
- **ReportLab** – Used for generating PDF documents.
- **Threading** – Used to support background operations during the capture workflow.
- **Time** – Used for timing and folder naming operations.

### Development Tools

- **Visual Studio Code**
- **GitHub**

### Database

- **SQLite**

SQLite was used for storing project-related data where required.

### Design / Planning

- **Draw.io** – Used to understand and design the project flow/architecture.

---

## Architecture

The project follows a simple **2-layer architecture**.

### 1. Frontend Layer

The frontend layer is responsible for:

- User interface components.
- User interactions.
- Settings screens.
- Document creation screens.
- Screenshot review and editing.

The UI was developed using **Flet**.

### 2. Backend Layer

The backend layer handles:

- Application/business logic.
- Screenshot processing.
- Mouse/click handling.
- Active window management.
- Data operations.
- Document generation.
- PDF and Word export.

This separation helped keep the application organized and easier to maintain.

---


## How to Run the Project

### 1. Clone or Download the Project

Download or clone this repository to your local machine.

### 2. Open the Project Directory

Open PowerShell or Command Prompt and navigate to the project folder:

```powershell
cd path\to\User_Manuel
```

### 3. Create and Activate the Virtual Environment

If a virtual environment is already included:

```powershell
.\venv\Scripts\Activate.ps1
```

If you need to create one:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 4. Install Required Dependencies

Install the required Python packages:

```powershell
pip install -r requirements.txt
```

### 5. Run the Application

After activating the virtual environment, run:

```powershell
flet run .\main.py
```

The application should now start.

> **Note:** Make sure the virtual environment is activated before running the project.

## Project Structure Concept

```text
Application
│
├── UI / Frontend
│   ├── Main Window
│   ├── Create Document
│   ├── Settings
│   └── Final Editor
│
├── Business Logic
│   ├── Screenshot Capture
│   ├── Mouse Click Handling
│   ├── Active Window Detection
│   ├── Cursor Placement
│   └── Document Processing
│
├── Data
│   └── SQLite
│
└── Export
    ├── PDF
    └── Word
```

---

## Challenges Faced

### 1. Screenshot and Click Coordinate Accuracy

One of the main technical challenges was correctly capturing the screenshot and placing the cursor at the exact click position.

Initially, the click coordinates did not align correctly with the screenshot. I solved this by understanding the coordinate difference and applying basic mathematical calculations to correct the position.

### 2. Learning Python

At the beginning of the project, I was relatively new to Python. However, my programming fundamentals were clear, which helped me learn the required Python concepts quickly.

### 3. Object-Oriented Programming

The project was developed using an OOP-based approach. I had to improve my understanding of:

- Classes and objects.
- Instance creation.
- Inheritance.
- Class interaction.
- Application flow.

### 4. Project Architecture

Since this was my first solo project, I initially had limited experience designing application architecture.

To understand and plan the application flow, I created a flow diagram using Draw.io and gradually structured the project around the required workflow.

### 5. Cursor Placement Approach

Initially, I attempted to draw the cursor directly over the screenshot. When that approach did not produce the desired result, I changed the implementation and used a cursor image/icon positioned over the screenshot instead.

This helped me achieve the required visual result more reliably.

### 6. Circular Dependencies

During development, I encountered situations where instances were being passed between classes, which created circular dependency issues.

Based on my mentor's feedback, I improved the design by applying better OOP principles and considering inheritance where appropriate.

---

## My Role

During my internship at **Viprush Technology**, I worked as a **Python Application Developer**.

My primary responsibility was developing the **Automating User Manual Generation** project.

My mentor provided the problem statement and introduced me to a similar market product, **Folge**, to help me understand the expected workflow and features.

I studied the workflow and requirements and then developed my own solution.

My responsibilities included:

- Understanding the documentation automation problem.
- Designing the application workflow.
- Developing the desktop UI using Flet.
- Implementing screenshot capture.
- Handling mouse click events.
- Detecting active application windows.
- Adding cursor indicators to screenshots.
- Implementing title and description functionality.
- Developing the final editing workflow.
- Implementing settings and customization.
- Generating PDF and Word documents.
- Testing and improving the application.
- Taking regular feedback from my mentor.

I also contributed to other real-world software projects during the internship, but this was my primary/final internship project.

---

## Learning Outcomes

### Technical Learning

This project helped me improve my understanding of:

- Python application development.
- Object-Oriented Programming.
- Flet for desktop UI development.
- Mouse and event handling.
- Screenshot and image processing.
- Active window detection.
- SQLite.
- PDF and Word document generation.
- Project structure and architecture.
- Problem-solving and debugging.

### Soft Skills

The project also improved my:

- Communication skills.
- Ability to ask for help when stuck.
- Problem-solving approach.
- Understanding of project requirements.
- Ability to receive and apply mentor feedback.
- Task planning and prioritization.
- Understanding of real-world software development.

---

## Communication and Task Management

During development, I provided regular updates to my mentor about completed tasks and ongoing work.

I also took continuous feedback throughout the project. This helped me identify problems early, improve implementation decisions, and remain aligned with the project requirements.

For task prioritization, I focused on completing important and core functionality first before moving to secondary features.

---

## Future Improvements

The following features could be added in future versions:

### 1. Previous Document Management

Allow users to access previously generated documents and edit or update them later.

### 2. Authentication

Add a login system for:

- User authentication.
- Access control.
- Better application security.

### 3. Admin Panel

An admin panel could be added to allow administrators to:

- Manage users.
- View registered users.
- Monitor user activity.
- Manage application data.

These improvements could make the application more user-friendly, secure, and scalable.

---

## Target Users

The target users are primarily:

- Small startups.
- Software development teams.
- Developers who create client documentation.
- Teams that prepare user manuals.
- Teams that create form-filling or software usage guides.

The application is particularly useful where screenshots and step-by-step documentation are repeatedly created manually.

---

## Why This Project Is Useful

The application focuses on automating a repetitive documentation workflow.

Instead of manually:

```text
Take Screenshot
      ↓
Find Click Location
      ↓
Add Cursor
      ↓
Write Title
      ↓
Write Description
      ↓
Format Content
      ↓
Prepare Document
```

the application combines much of this process into one workflow:

```text
Use Target Software
      ↓
Automatic Screenshot
      ↓
Automatic Cursor Indicator
      ↓
Add Title & Description
      ↓
Edit & Format
      ↓
Export PDF / Word
```

This makes the process more consistent and reduces repetitive manual work.

---

## Project Duration

**Approximately 3 months**

---

## Internship Context

**Organization:** Viprush Technology  
**Role:** Python Application Developer  
**Project:** Automating User Manual Generation  
**Project Type:** Desktop Application  
**Duration:** Approximately 3 months  
**Primary Language:** Python  
**UI Framework:** Flet  
**Database:** SQLite  
**Development Environment:** Visual Studio Code  
**Version Control:** GitHub

---

## Disclaimer

The project was developed as an internship project based on a real-world documentation problem. The estimated **40% reduction in manual effort** represents my assessment of the repetitive work automated by the application and was not calculated using a formal productivity measurement framework.
