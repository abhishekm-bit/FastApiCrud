import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-3-flash-preview")

def generate(context, user_input, level, duration):
    prompt = f"""
You are a senior EdTech curriculum designer.

Your task is to generate a **high-quality professional course syllabus**.

================ STRICT CONSTRAINTS =================
1. Course Level MUST be exactly: {level}
2. Course Duration MUST be exactly: {duration}
3. DO NOT modify, extend, or reinterpret level or duration.
4. Follow the level strictly:
   - Beginner → basic concepts only
   - Intermediate → moderate depth
   - Advanced → industry-level depth
5. Structure syllabus based on duration:
   - If 1 Month → 4 weeks
   - If 3 Months → 12 weeks
   - If 6 Months → monthly plan
====================================================

Use the reference data below ONLY as supporting context.
Do NOT copy blindly. Use it to improve accuracy.

---------------- REFERENCE DATA ----------------
{context}
------------------------------------------------

Generate syllabus for:

Course Name: {user_input}
Level: {level}
Duration: {duration}

================ OUTPUT FORMAT =================

1. Course Title
2. Level
3. Duration
4. Course Objective

5. Week/Month-wise Breakdown
   - Clear titles
   - Learning objectives
   - Topics covered

6. Tools & Technologies
7. Capstone Project
8. Learning Outcomes

================================================

Quality Guidelines:
- Industry aligned
- Practical focused
- No unnecessary theory
- Clear progression from basics → advanced
- Professional tone

Now generate the syllabus.
"""


    response = model.generate_content(prompt)
    return response.text
