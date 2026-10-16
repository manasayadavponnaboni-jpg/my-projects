import streamlit as st
st.title("🎓Online Quiz Portal")
name=st.text_input("student name")
rollno=st.text_input("Roll Number")
subject=st.radio("Select Subject",
                     ["Python","English","Maths"],index=None,
                     horizontal=True)
st.divider()
if subject=="Python":
        st.subheader("🐍Python Quiz")
        q1=st.radio(
            "1.Which symbol is used for comments",
            ["//","*","$","#"],
            index=None
             )
        q2=st.radio(
                    "2.Which Function is used to read the data from user?",
                    ["print()","display()","read()","input()"],
                    index=None
                     )
        q3=st.radio(
                    "3.function keyword  in python?",
                    ["fun","def","import","define"],
                    index=None
                     )
        q4=st.radio(
            "4. Which data type stores True or False?",
            ["int", "float", "str", "bool"],
            index=None
        )

        q5 = st.radio(
            "5. Which symbol is used for exponentiation?",
            ["^", "**", "//", "%%"],
            index=None
        )

        q6 = st.radio(
            "6. Which keyword is used to create a loop?",
            ["for", "loop", "repeat", "iterate"],
            index=None
        )

        q7 = st.radio(
            "7. Which of these is a Python list?",
            ["(1,2,3)", "[1,2,3]", "{1,2,3}", "<1,2,3>"],
            index=None
        )

        q8 = st.radio(
            "8. Which function gives the length of a list?",
            ["size()", "length()", "len()", "count()"],
            index=None
        )

        q9 = st.radio(
            "9. Which keyword is used for a condition?",
            ["if", "when", "check", "condition"],
            index=None
        )

        q10 = st.radio(
            "10. Python is a __.",
            [
                "Programming Language",
                "Markup Language",
                "Database",
                "Operating System"
            ],
            index=None
        )
        answers = [
                q1 == "#",
                q2 == "input()",
                q3 == "def",
                q4 == "bool",
                q5 == "**",
                q6 == "for",
                q7 == "[1,2,3]",
                q8 == "len()",
                q9 == "if",
                q10 == "Programming Language"
            ]
       
elif subject == "English":

         st.header("📖 English Quiz")

         q1 = st.radio(
            "1. Choose the correct article: _ apple",
            ["A", "An", "The", "No article"],
            index=None
        )

         q2 = st.radio(
            "2. What is the plural of Child?",
            ["Childs", "Children", "Childes", "Childrens"],
            index=None
        )

         q3 = st.radio(
            "3. Choose the correct sentence.",
            [
                "She go to school.",
                "She goes to school.",
                "She going school.",
                "She gone school."
            ],
            index=None
        )

         q4 = st.radio(
            "4. Opposite of Happy is:",
            ["Joyful", "Sad", "Excited", "Glad"],
            index=None
        )

         q5 = st.radio(
            "5. Synonym of Big is:",
            ["Small", "Tiny", "Large", "Short"],
            index=None
        )

         q6 = st.radio(
            "6. Past tense of Go is:",
            ["Goed", "Gone", "Went", "Going"],
            index=None
        )

         q7 = st.radio(
            "7. Which is a noun?",
            ["Run", "Beautiful", "School", "Quickly"],
            index=None
        )

         q8 = st.radio(
            "8. Which word is an adjective?",
            ["Beautiful", "Run", "Slowly", "Eat"],
            index=None
        )

         q9 = st.radio(
            "9. Choose the correct spelling.",
            ["Beautifull", "Beutiful", "Beautiful", "Beautifal"],
            index=None
        )

         q10 = st.radio(
            "10. What is the opposite of Hot?",
            ["Warm", "Cold", "Heat", "Fire"],
            index=None
        )

         answers = [
                q1 == "An",
                q2 == "Children",
                q3 == "She goes to school.",
                q4 == "Sad",
                q5 == "Large",
                q6 == "Went",
                q7 == "School",
                q8 == "Beautiful",
                q9 == "Beautiful",
                q10 == "Cold"
            ]

         
elif subject == "Maths":

     st.header("➗ Maths Quiz")

     q1 = st.radio(
            "1. What is 10 + 20?",
            ["20", "30", "40", "50"],
            index=None
        )

     q2 = st.radio(
            "2. What is 5 × 6?",
            ["20", "25", "30", "35"],
            index=None
        )

     q3 = st.radio(
            "3. What is 100 ÷ 10?",
            ["5", "10", "15", "20"],
            index=None
        )

     q4 = st.radio(
            "4. What is the square of 5?",
            ["10", "15", "20", "25"],
            index=None
        )

     q5 = st.radio(
            "5. What is 15 - 7?",
            ["6", "7", "8", "9"],
            index=None
        )

     q6 = st.radio(
            "6. What is 12 × 2?",
            ["20", "22", "24", "26"],
            index=None
        )

     q7 = st.radio(
            "7. What is 50 ÷ 5?",
            ["5", "10", "15", "20"],
            index=None
        )

     q8 = st.radio(
            "8. What is 9²?",
            ["18", "27", "81", "90"],
            index=None
        )

     q9 = st.radio(
            "9. What is 25 + 25?",
            ["40", "45", "50", "55"],
            index=None
        )

     q10 = st.radio(
            "10. What is 100 - 45?",
            ["45", "50", "55", "65"],
            index=None
        )
     answers = [

       q1 == "30",
       q2 == "30",
       q3 == "10",
       q4 == "25",
       q5 == "8",
       q6 == "24",
       q7 == "10",
       q8 == "81",
       q9 == "50",
       q10 == "55"
            ]
 
if st.button("Submit Quiz"):
                
                score=sum(answers)
                st.success("Your Result")
                st.write(f"Student name:{name}")
                st.write(f"Roll Number:{rollno}")
                st.write(f"Selected Subject:{subject}")
                st.metric("your score",
                          f"{score}/10s")
                if score==10:
                    st.balloons()
                    st.success("Excellent")
                else:
                    st.warning("Keep Practicing!")
