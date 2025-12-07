# Advanced Password Strength Checker

## Overview

This project is a **web-based password strength checker** built with **Python Flask** using an **MVC structure**.  
It evaluates passwords based on length, character variety, sequences, repeated characters, and common password patterns.  

**Features include:**
- **Strength rating**: Very Weak → Very Strong  
- **Feedback messages**: Tips to improve password security  
- **Styled UI**: Color-coded badges and responsive design  

This project is ideal for learning Flask, MVC design, and basic password security concepts.

---

## Features

- **Advanced scoring system:**
  - Length bonus for 8+ characters  
  - Points for uppercase, lowercase, digits, and symbols  
  - Penalties for sequences (`123`, `abc`)  
  - Penalties for repeated characters (`aaa`, `111`)  
  - Checks against common passwords  

- **Feedback messages**:
  - Suggests improvements such as adding symbols, digits, or uppercase letters  

- **Styled UI**:
  - Responsive design  
  - Color-coded badges for strength  

---

## Folder Structure
├─ controller/
│ └─ password_controller.py # Flask app & routes
├─ model/
│ └─ password_model.py # Password checking logic
├─ templates/
│ └─ password_views.html # HTML template
├─ init.py 


---

## Algorithm Details

1. **Length**
   - <5 characters → weak  
   - 5–7 characters → small bonus  
   - 8+ characters → larger bonus  

2. **Character Variety**
   - Uppercase letters → +1  
   - Lowercase letters → +1  
   - Digits → +1  
   - Symbols → +2  

3. **Penalties**
   - Sequences of 3+ characters (e.g., `123`, `abc`) → -1 point  
   - Repeated characters 3+ times (e.g., `aaa`) → -1 point  
   - Common passwords (e.g., `123456`, `password`) → auto Very Weak  

4. **Strength Score → Label**

| Score | Strength       |
|-------|---------------|
| 0–2   | Very Weak      |
| 3–4   | Weak           |
| 5–6   | Medium         |
| 7–8   | Strong         |
| 9–10  | Very Strong    |

---

## Installation & Run

### Clone the repository
```bash
git clone <your-repo-url>
cd Passwordchecker

pip install flask

Run the app
python -m controller.password_controller
Use -m to run the controller as a module so Flask can locate the templates.
