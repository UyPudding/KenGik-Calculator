import streamlit as st   # pip install streamlit


st.set_page_config(
    page_title='KenGik Calculator - Basic Edition',
    page_icon='🧮'
)


# Convert radio value to operation
operation_dict={"Add (+)":"+","Subtract (-)":"-","Multiply (×)":"×","Divide (÷)":"÷"}


## Session State ##
if 'result' not in st.session_state:
    st.session_state.result=0
if 'previous_result' not in st.session_state:
    st.session_state.previous_result=['None']
if 'first_num' not in st.session_state:
    st.session_state.first_num=0
if 'second_num' not in st.session_state:
    st.session_state.second_num=0
if 'operations' not in st.session_state:
    st.session_state.operations='Add (+)'
if 'disable_calculate' not in st.session_state:
    st.session_state.disable_calculate=False


## Function ##
def calculate():  # For calculating
    try:  # Calculate system when Auto-Calculate is disabled
       if operation=="Add (+)":
           st.session_state.result=st.session_state.first_num+st.session_state.second_num
       elif operation=="Subtract (-)":
           st.session_state.result=st.session_state.first_num-st.session_state.second_num
       elif operation=="Multiply (×)":
           st.session_state.result=st.session_state.first_num*st.session_state.second_num
       elif operation=="Divide (÷)":
           st.session_state.result=st.session_state.first_num/st.session_state.second_num

       if 'None' in st.session_state.previous_result:
           st.session_state.previous_result.clear()
        
       if len(st.session_state.previous_result)>4:  # Limit quantity of previous results
           st.session_state.previous_result.clear()
           st.session_state.previous_result.append(str(st.session_state.result))
       else:
           st.session_state.previous_result.append('%g'%(float(st.session_state.result)))  # %g to Avoid floating point error

    except ZeroDivisionError as e:  # Avoid ZeroDivisionError
        st.session_state.result='#DIV/0!'
        st.toast(body=f'{e}!'.capitalize(),icon='❌')


def reset_all():  # Clear everything
    st.session_state.pop('first_num')
    st.session_state.pop('second_num')
    st.session_state.pop('result')
    st.session_state.previous_result.clear();st.session_state.previous_result.append('None')
    st.toast(body='Reset Successfully!',icon='✅')


# For Auto-Calculate feature
def auto_calculator():  # Disable Calculate button
    if not auto_calculate:
        st.session_state.disable_calculate=True
    else:
        st.session_state.disable_calculate=False


if st.session_state.disable_calculate:  # Auto-Calculate system
    try:
       if st.session_state.operations=="Add (+)":
           st.session_state.result=st.session_state.first_num+st.session_state.second_num
       elif st.session_state.operations=="Subtract (-)":
           st.session_state.result=st.session_state.first_num-st.session_state.second_num
       elif st.session_state.operations=="Multiply (×)":
           st.session_state.result=st.session_state.first_num*st.session_state.second_num
       elif st.session_state.operations=="Divide (÷)":
           st.session_state.result=st.session_state.first_num/st.session_state.second_num

    except ZeroDivisionError as e:
        st.session_state.result='#DIV/0!'
        st.toast(body=f'{e}!'.capitalize(),icon='❌')


# Sidebar
with st.sidebar:  # Change theme color
    st.html('<h1 style="text-align:center;font-size:40px;">Edition</h1>')
    st.link_button(label='Basic',url='https://docs.streamlit.io/develop/api-reference/widgets/st.link_button',use_container_width=True)
    st.link_button(label='Advanced',url='https://docs.streamlit.io/develop/api-reference/widgets/st.link_button',use_container_width=True)
    st.markdown('You are using: **Basic Edition**')
    st.divider()
    st.html('<h1 style="text-align:center;font-size:40px;">Theme</h1>')
    theme_color=st.color_picker(label='Pick a Theme Color',value='#1467f0',help='Change Theme Color')
    st.markdown(f'''<p>• Default Color: <b>#1467F0</b></p>
                <p>• Current Color: <b>{theme_color.upper()}</b></p>''',
                unsafe_allow_html=True)

    st.divider()
    st.markdown('[![Streamlit](https://img.shields.io/badge/Made%20with%20-Streamlit-red)](https://streamlit.io/)')


# CSS styling button
st.html(f"""
<style>
            div.stButton>button:hover{{
            border: 1px solid {theme_color};
            color: {theme_color};
            }}
            div.stButton>button:active{{
            background-color: {theme_color};
            color: white;
            }}
</style>""")


st.markdown(f'<h1 style="color:{theme_color};text-align:center;font-size:52px;"><b>KenGik Calculator</b></h1>',unsafe_allow_html=True)


# Disclaimer
st.html(f"""
<details>
<summary><strong>Disclaimer</strong></summary>
<pre>This is <b>Basic Edition of</b> <span style="color:{theme_color}"><b>KenGik Calculator</b></span>. You can use this for <i>simple</i> and <i>quick</i> Calculation!</pre>
</details>""")


st.html(f'<h5 style="font-size:18.5px"><span style="color:{theme_color};">First</span> Number</h5>')

# First number input
first_number=st.number_input(label="t",step=0.1,help='Enter an first number',label_visibility='collapsed',
                             format='%1.1f',placeholder="Enter an First Number",key='first_num')

st.html(f'<h5 style="font-size:18.5px"><span style="color:{theme_color}">Second</span> Number</h5>')

# Second number input
second_number=st.number_input(label="t",step=0.1,help='Enter an second number',label_visibility='collapsed',
                              format='%1.1f',placeholder="Enter an Second Number",key='second_num')


st.write("<h5 style='font-size:18.5px;'>Operation</h5>",unsafe_allow_html=True)
st.html('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>')  # Horizontal st.radio

# Operations radio button
operation=st.radio(label='Select an operation',options=["Add (+)","Subtract (-)","Multiply (×)","Divide (÷)"],key='operations')

st.write('<h5 style="font-size:18.5px">Calculation</h5>',unsafe_allow_html=True)
if st.session_state.result!='#DIV/0!':  # If not divide by zero
   st.markdown('<span style="color:%s"><b>Equation:</b></span> &nbsp; \
                %g %s %g = **%g**'%(theme_color,st.session_state.first_num,operation_dict[st.session_state.operations],st.session_state.second_num,float(st.session_state.result)),
                unsafe_allow_html=True)
else:  # if divide by zero
    st.markdown('<span style="color:%s"><b>Equation:</b></span> &nbsp; \
                %g %s %g = **%s**'%(theme_color,st.session_state.first_num,operation_dict[st.session_state.operations],st.session_state.second_num,st.session_state.result),
                unsafe_allow_html=True)



submit=st.button(label='Calculate',use_container_width=True,on_click=calculate,
                 disabled=st.session_state.disable_calculate)  # Calculate button

reset=st.button(label='Reset',use_container_width=True,on_click=reset_all)  # Reset button

st.markdown(f'<span style="color:{theme_color}"><b>Previous Results:</b></span> &nbsp; {"  ;  ".join(st.session_state.previous_result)}',
                unsafe_allow_html=True)  # Display 4 previous results

# Auto-Calculate button
auto_calculate=st.checkbox(label='**Auto-Calculate**',on_change=auto_calculator)  
st.write('''<p style="color:#8c8c8c">When Auto-Calculate is enabled, the calculation will automatically calculate and return results.
         This feature will not keep previous results.</p>''',unsafe_allow_html=True)
