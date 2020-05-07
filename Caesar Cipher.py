#!/usr/bin/env python
# coding: utf-8

# In[2]:


def encrypt(text,num):
    encrypted_text=""
    if(num>=0):
        start_capital=ord('A')
        start_small=ord('a')
        end_capital=ord('Z')-num
        end_small=ord('z')-num
        for x in text:
            if(x.isalpha()):
                asci=ord(x)
                if((asci>=start_capital and asci<=end_capital) or (asci>=start_small and asci<=end_small)):
                    encrypted_text+=chr(asci+num)
                else:
                    encrypted_text+=chr(asci+num-26)
            else:
                encrypted_text+=x
    else:
        num=abs(num)
        start_capital=ord('A')+num
        start_small=ord('a')+num
        end_capital=ord('Z')
        end_small=ord('z')
        for x in text:
            if(x.isalpha()):
                asci=ord(x)
                if((asci>=start_capital and asci<=end_capital) or (asci>=start_small and asci<=end_small)):
                    encrypted_text+=chr(asci-num)
                else:
                    encrypted_text+=chr(asci-num+26)
            else:
                encrypted_text+=x
    return encrypted_text
text=input()
num=int(input())
print(encrypt(text,num))


# In[ ]:





# In[ ]:




