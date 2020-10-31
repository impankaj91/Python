def rem_word(spell,words):
    st=this.replace(words,"[Warning:Restricted Word]")
    return st.strip()
    
this=input("Enter Your Full String : ")
word=input("Enter Word Want to Remove :")
print(f"Hey ,Your New Stuff is {rem_word(this,word)}")