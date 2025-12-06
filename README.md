# **🐍 Python CLI Quiz App**

A simple, customizable Command-Line Interface (CLI) application built in Python for running self-study quizzes. It supports various question formats, including True/False, Identification, Multiple Choice, and complex Enumeration checks.

## **🚀 Features**

* **Customizable Quizzes:** Questions are loaded from a single, easy-to-edit questions.txt file.  
* **Multiple Formats:** Supports Standard (Identification/MCQ), True/False, and Enumeration.  
* **Enumeration Modes:** Check answers in strict sequence or in any random order.  
* **Randomized Order:** Questions are shuffled every time you run the quiz.  
* **Colorized Output:** Uses colorama for better readability and feedback in the terminal.

## **🛠️ Setup Guide**

### **1\. Prerequisites**

You must have **Python 3** installed on your system.

### **2\. Installation**

1. **Clone the Repository (or save the files):**
   ```bash
   git clone \[YOUR\_REPO\_URL\]  
   cd cli-quiz-app
   ```
3. Install Dependencies:  
   This app requires the colorama library for colorful text output.
```bash
   pip install colorama
```

5. Ensure Files are Present:  
   Make sure you have both the Python script (quiz\_app.py or similar) and your content file (questions.txt) in the same directory.

## **✍️ Quiz Content File (questions.txt)**

The application is entirely driven by the content of your questions.txt file.

### **Formatting Rules (Mandatory)**

1. Each question must be separated from the next by a **BLANK LINE**.  
2. Each entry must have the **Answer** and the **Question** separated by a space-hyphen-space: \-.  
   \[CORRECT ANSWER\] \- \[QUESTION TEXT\]

### **Examples of Supported Formats**

| Format | Answer Example | Question Text Example | questions.txt Entry |
| :---- | :---- | :---- | :---- |
| **Identification** | Algorithm | A set of well-defined steps to solve a particular problem in a finite amount of time. | Algorithm \- A set of well-defined steps to solve a particular problem in a finite amount of time. |
| **True/False** | TRUE | A list in Python is immutable. | TRUE \- A list in Python is immutable. |
| **Multiple Choice** | C. Object | Which is NOT a Python data type? A. Integer B. String C. Object D. Boolean | C. Object \- Which is NOT a Python data type? A. Integer B. String C. Object D. Boolean |

### **Enumeration Formats**

Use a comma-separated list for the answer and add one of the following tags to the end of the question text to define the enumeration mode:

| Tag | Behavior | Example questions.txt Entry |
| :---- | :---- | :---- |
| **\[enum\]** | Order does NOT matter (default). | Red, Green, Blue \- Name the primary colors. \[enum\] |
| **\[enum:random\]** | Order does NOT matter. | Input, Process, Output \- Name the parts of the cycle. \[enum:random\] |
| **\[enum:sequence\]** | **Order MUST be correct.** | Plan, Code, Test, Deploy \- List the four steps of the SDLC in order. \[enum:sequence\] |

## **▶️ Running the Quiz**

1. **Open your terminal** and navigate to the project directory.  
2. **Execute the script:**  
   python quiz\_app.py

The quiz will begin immediately, shuffling the questions and prompting you for answers. After completion, you will see your final score and a review of all incorrect answers.
