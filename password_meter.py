import streamlit as st
import re
st.set_page_config(page_title="PASSWORD STRENGTH METER" , page_icon="🛡️")

st.title ("🔑 PASSWORD STRENGTH CHECKER")

st. markdown("""
## WELCOME TO ULTIMATE PASSWORD STRENGTH METER!
Use this simple tool for protection of your accounts by enhancing your password strength  
    We will help in creating **STRONG PASSWORD**🔐 """)

password = st.text_input("ENTER YOUR PASSWORD" , type="password")

def check_password_strength(password):
    feedback =[]
    score = 0

    if len(password)>= 8:
        score += 1
    else:
      feedback.append ("➤ Make it at least 8 characters long ⭕. " )

    if re.search (r"[A-Z]" , password):
        score += 1
    else :
         feedback.append ("➤ Add uppercase letters ⭕.")

    if re.search (r"[a-z]" , password):
        score += 1
    else:
      feedback.append ("➤ Add lowercase letters ⭕." )  

    if re.search (r"\d" , password) :
        score += 1
    else:
        feedback.append("➤ Include at least one digit (0-9) ⭕.")       

    if re.search(r"[!@#$%^&*]" , password):
        score += 1
    else :
        feedback.append ( "➤ Use a special character (!@#$%^&*)⭕.") 

    return score , feedback


def get_score_level(score):
    if score == 5:
        return "strong"
    elif score >= 3:
        return "moderate"
    else:
        return "weak"
    

if password :
    score, suggestions = check_password_strength(password)
    strength = get_score_level(score)

    st.success(f"\n🛡️ Password Strength: {strength} ({score}/5)")

    if strength == "Strong":
      st.markdown("✅ Great job! Your password is strong and secure.")
    else:
      st.markdown("🔧 Suggestions to improve your password:")
      for tip in suggestions:
        st.write(tip)

else:
    st.info("PLEASE ENTER YOUR PASSWORD")        
