import streamlit as st
import numpy  as np
import pandas as pd
from PIL import Image
import time



st.title ('streamlit elementary level')
st.write ('picture image')
#st.sidebar.write ('picture image')


st.write('progress bar')
'Start'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
  latest_iteration.text(f'Iteration{i + 1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'Done'
expander1= st.expander('question1')
expander1.write('Answer to 1')

expander2= st.expander('question1')
expander2.write('Answer to 2')


#left_column,right_column = st.columns(2)
#button= left_column.button('display column in the left')

#if button:
#  right_column.write('write your contents')

condition = st.sidebar.slider('Your condition', 0, 100, 50)
text= st.sidebar.text_input('please type your hobby')

'Your hobby is ', text
'Your condition is ', condition


option= st.selectbox('enter a number',
    list(range(1,11))
             )
'Your fond of number is ', option



#if st.checkbox('show image'):
#  img = Image.open('sample-free-layout.jpg')
#  st.image(img, caption='freelayout', use_column_width=True)

dfmap = pd.DataFrame(
  np.random.rand(100,2)/[50,50] + [35.69, 139.70],
  columns=['lat','lon']
  )
st.map(dfmap)

df = pd.DataFrame(
  np.random.rand(20,3),
  columns=['a', 'b', 'c'] 
)

#st.dataframe(df)
st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)

#df = pd.DataFrame({
#  '1列目':[1, 2, 3, 4] ,
#  '2列目':[10, 20, 300, 40] 
#}) 
#st.dataframe(df.style.highlight_max(axis=0), width=200, height=00)
st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項
    
```python
import streamlit as st
import numpy  as np
import pandas as pd
```
"""
    