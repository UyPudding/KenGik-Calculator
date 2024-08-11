import streamlit as st   # pip install streamlit
from math import*
from math import radians as Deg
from fractions import Fraction
import time


st.set_page_config(
    page_title="KenGik Calculator - Advanced Edition",
    page_icon="🧮"
)


## Sidebar ##
with st.sidebar:   # Change theme color
    st.html('<h1 style="text-align:center;font-size:40px;">Edition</h1>')
    st.link_button(label='Basic',url='https://kengik-calculator-basic.streamlit.app/',use_container_width=True)
    st.link_button(label='Advanced',url='https://kengik-calculator-advanced.streamlit.app/',use_container_width=True)
    st.markdown('You are using: **Advanced Edition**')
    st.divider()
    st.html('<h1 style="text-align:center;font-size:40px;">Theme</h1>')
    theme_color=st.color_picker(label='Pick a Theme Color',value='#1467f0',help='Change Theme Color')
    st.markdown(f'''<p>• Default Color: <b>#1467F0</b></p>
                <p>• Current Color: <b>{theme_color.upper()}</b></p>''',
                unsafe_allow_html=True)
    
    st.divider()
    st.markdown('[![Streamlit](https://img.shields.io/badge/Made%20with%20-Streamlit-red)](https://streamlit.io/)')
    st.markdown(f'<b>Before use this Calculator, please read the <a href="#Note" style="color:{theme_color};">NOTE!</a></b>',unsafe_allow_html=True)
    st.markdown('💡:green[**TIP:**] If the calculator return result then click [AC] to Reset.')



# CSS Style
st.html(f"""
<style>
        div[data-testid='column'] {{
        width: -moz-fit-content;
        width: 60px !important;
        text-align: center;
        float: center;
        flex: unset;
        }}

        div.stButton>button[kind='secondary']{{
        border: 1px solid grey;
        width:40px;
        font-size:3px;
        color:black;
        }}

        div.stButton>button[kind='secondary']:hover{{
        border:1px solid grey;
        color:black;
        }}

        div.stButton>button[kind='secondary']:active{{
        border:1px solid grey;
        color:black;
        background-color:white;
        }}

        div.stButton>button[kind='primary']{{
        border: 1px solid {theme_color};
        width:60px;
        background-color: {theme_color};
        color:white;
        }}

        div.stButton>button[kind='primary']:hover{{
        border: 1px solid {theme_color};
        color:white;
        }}

        div.stButton>button[kind='primary']:active{{
        border:1px solid {theme_color};
        background-color:{theme_color};
        color:white;
        }}
</style>""")



## Session State ##
if 'input' not in st.session_state:           # Display equation and result
    st.session_state.input=''
if 'disable_button' not in st.session_state:  # Disable buttons when returned result
    st.session_state.disable_button=False
if 'angle_change' not in st.session_state:    # Change angle unit
    st.session_state.angle_change='Radians'
if 'fractions' not in st.session_state:       # Return result as fraction
    st.session_state.fractions=False



## Functions ##
def add_7():  # Add 7 to equation
    st.session_state.input+='7'
def add_4():  # Add 4 to equation
    st.session_state.input+='4'
def add_1():  # Add 1 to equation
    st.session_state.input+='1'
def add_percent():  # Add percent symbol to equation
    st.session_state.input+='%'
def add_8():  # Add 8 to equation
    st.session_state.input+='8'
def add_5():  # Add 5 to equation
    st.session_state.input+='5'
def add_2():  # Add 2 to equation
    st.session_state.input+='2'
def add_0():  # Add 0 to equation
    st.session_state.input+='0'
def add_9():  # Add 9 to equation
    st.session_state.input+='9'
def add_6():  # Add 6 to equation
    st.session_state.input+='6'
def add_3():  # Add 3 to equation
    st.session_state.input+='3'
def add_dot():  # Add dot to equation
    st.session_state.input+='.'
def add_plus():      # Add plus symbol to equation
    st.session_state.input+='+'
def add_minus():     # Add minus symbol to equation
    st.session_state.input+='-'
def add_multiply():  # Add multiply symbol to equation
    st.session_state.input+='×'
def add_divide():  # Add divide symbol to equation
    st.session_state.input+='÷'
def add_root():  # Add square root to equation
    st.session_state.input+='√('
def add_exponent():  # Add exponent symbol to equation
    st.session_state.input+='^'
def add_parenthese():  # Add begin parenthese to equation
    st.session_state.input+='('
def add_parenthese2():  # Add close parenthese to equation
    st.session_state.input+=')'
def delete():  # delete one character from equation
    st.session_state.input=st.session_state.input[:-1]
def add_sin(): # Add sine function to equation
    if st.session_state.angle_change=='Degrees':  
        st.session_state.input+='sin(Deg('   # Add degree sine function
    else:
        st.session_state.input+='sin('       # Add radian sine function
def add_cos(): # Add cosine function to equation
    if st.session_state.angle_change=='Degrees':
        st.session_state.input+='cos(Deg('   # Add degree cosine function
    else:
        st.session_state.input+='cos('       # Add radian cosine function
def add_tan(): # Add tangent function to equation
    if st.session_state.angle_change=='Degrees':
        st.session_state.input+='tan(Deg('   # Add degree tangent function
    else:
        st.session_state.input+='tan('       # Add radian tangent function
def clear_all():  # Clear all characters in equation
    st.session_state.pop('input')
    st.session_state.disable_button=False
def add_pi():     # Add pi symbol to equation
    st.session_state.input+='π'
def add_log():    # Add logarithm function to equation
    st.session_state.input+='log('
def add_abs():    # Add absolute function to equation
    st.session_state.input+='abs('
def add_factorial():  # Add factorial function to equation
    st.session_state.input+='n!('
def add_fraction():   # Add fraction to equation
    st.session_state.input+='(1/'
def add_e():  # Add euler symbol to equation
    st.session_state.input+='e'

def calculate():  # Calculate system
    # Replace all math operators with programming math operators
    st.session_state.input=st.session_state.input.replace('×','*')
    st.session_state.input=st.session_state.input.replace('÷','/')
    st.session_state.input=st.session_state.input.replace('√(','sqrt(')
    st.session_state.input=st.session_state.input.replace('^','**')
    st.session_state.input=st.session_state.input.replace('π','pi')
    st.session_state.input=st.session_state.input.replace('n!(','factorial(')

    time.sleep(0.2)

    try:
        st.session_state.input=eval(st.session_state.input)  # Calculate 
        st.session_state.input="%g"%(float(st.session_state.input))  # Avoid floating point error

        if st.session_state.fractions:  # If Result as Fraction is enabled
            st.session_state.input="%s"%(Fraction(float(st.session_state.input)).limit_denominator(10))

    except ZeroDivisionError:  # Handling ZeroDivisionError
        st.session_state.input='Math ERROR - Click [AC] to Reset'
    except:  # Handling all remaining exceptions
        st.session_state.input='Syntax ERROR - Click [AC] to Reset'
    st.session_state.disable_button=True  # Disable all button when returned result (except [AC] button)



st.markdown(f'<h1 style="color:{theme_color};text-align:center;font-size:52px;"><b>KenGik Calculator</b></h1>',unsafe_allow_html=True)

# Disclaimer
st.html(f"""
<details>
<summary><strong>Disclaimer</strong></summary>
<pre>This is <b>Advanced Edition of</b> <span style="color:{theme_color}"><b>KenGik Calculator</b></span> aka Scientific Calculator.\
The Edition is <b>Main Calculator of KenGik</b> for <i>complex</i> Calculation!
<b>-> Please read the <a href='#Note' style='color:{theme_color};'>NOTE!</a></b></pre>
</details>""")

container=st.container(border=True)  # Create container
container.write(f"<span style='font-size:12px;text-align:left;color:{theme_color};'><b>KenGik Calculator</b></span>",unsafe_allow_html=True)
container.write(f"<p align='left'><span style='font-size:40px;'>{st.session_state.input}</span></p>",unsafe_allow_html=True)
container.divider()


## 8 Columns for sorting button
col1,col2,col3,col4,col5,col6,col7,col8=container.columns([1,1,1,1,1,1,1,1])
with col1:
   st.button(label='7',on_click=add_7,disabled=st.session_state.disable_button)
   st.button(label='4',on_click=add_4,disabled=st.session_state.disable_button)
   st.button(label='1',on_click=add_1,disabled=st.session_state.disable_button)
   st.button(label='%',on_click=add_percent,disabled=st.session_state.disable_button)

with col2:
    st.button(label='8',on_click=add_8,disabled=st.session_state.disable_button)
    st.button(label='5',on_click=add_5,disabled=st.session_state.disable_button)
    st.button(label='2',on_click=add_2,disabled=st.session_state.disable_button)
    st.button(label='0',on_click=add_0,disabled=st.session_state.disable_button)

with col3:
    st.button(label='9',on_click=add_9,disabled=st.session_state.disable_button)
    st.button(label='6',on_click=add_6,disabled=st.session_state.disable_button)
    st.button(label='3',on_click=add_3,disabled=st.session_state.disable_button)
    st.button(label='.',on_click=add_dot,disabled=st.session_state.disable_button)

with col4:
    st.button(label='**+**',on_click=add_plus,disabled=st.session_state.disable_button)
    st.button(label='**-**',on_click=add_minus,disabled=st.session_state.disable_button)
    st.button(label='×',on_click=add_multiply,disabled=st.session_state.disable_button)
    st.button(label='÷',on_click=add_divide,disabled=st.session_state.disable_button)

with col5:
    st.button(label='√',on_click=add_root,disabled=st.session_state.disable_button)
    st.button(label='xʸ',on_click=add_exponent,disabled=st.session_state.disable_button)
    st.button(label='(',on_click=add_parenthese,disabled=st.session_state.disable_button)
    st.button(label=')',on_click=add_parenthese2,disabled=st.session_state.disable_button)

with col6:
    st.button(label='DEL',type='primary',on_click=delete,disabled=st.session_state.disable_button)
    st.button(label='sin',type='primary',on_click=add_sin,disabled=st.session_state.disable_button)
    st.button(label='cos',type='primary',on_click=add_cos,disabled=st.session_state.disable_button)
    st.button(label='tan',type='primary',on_click=add_tan,disabled=st.session_state.disable_button)

with col7:
    st.button(label='AC',type='primary',on_click=clear_all)
    st.button(label='π',type='primary',on_click=add_pi,disabled=st.session_state.disable_button)
    st.button(label='log',type='primary',on_click=add_log,disabled=st.session_state.disable_button)
    st.button(label='Abs',type='primary',on_click=add_abs,disabled=st.session_state.disable_button)
    
with col8:
    st.button(label='n!',type='primary',on_click=add_factorial,disabled=st.session_state.disable_button)
    st.button(label='1/x',type='primary',on_click=add_fraction,disabled=st.session_state.disable_button)
    st.button(label='e',type='primary',on_click=add_e,disabled=st.session_state.disable_button)
    st.button(label='=',type='primary',on_click=calculate,disabled=st.session_state.disable_button)


st.html('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>')  # Horizontal st radio

angle=st.radio(label='**Angle Unit**',options=['Radians','Degrees'],
               key='angle_change',help='**Default:** Radians')  # Angle unit radio button

# Result as Fraction checkbox
fraction=st.checkbox(label='**Result as Fraction**',help='Set the Result as Fraction as default',key='fractions')


# Note 
st.html(
f'''
<details>
<summary><span id='Note' style="color:{theme_color};">ℹ️ <b>NOTE</b></span></summary>
<pre><b>1. x^y:</b> Exponent - <b>x^2 = x²</b><br>
<b>2. n!(x):</b> Factorial - <b>n!(3) = 3!</b> = 6<br>
<b>3. abs(x):</b> Absolute - <b>abs(-2) = |-2|</b> = 2<br>
<b>4. sin(x):</b> Sine with x Radians - <b>sin(30) = sin(30 rad)</b> = -0.98803162409
   <b>sin(Deg(x)):</b> Sine with x Degrees - <b>sin(Deg(30)) = sin(30°)</b> = 0.5<br>
<b>5. cos(x):</b> Cosine with x Radians - <b>cos(90) = cos(90 rad)</b> = -0.44807361612
   <b>cos(Deg(x)):</b> Cosine with x Degrees - <b>cos(Deg(90)) = cos(90°)</b> = 0<br>
<b>6. tan(x):</b> Tangent with x Radians - <b>tan(45) = tan(45 rad)</b> = 1.61977519054
   <b>tan(Deg(x)):</b> Tangent with x Degrees - <b>tan(Deg(45)) = tan(45°)</b> = 1<br>
<span style="color:#840cbc;"><b><i>❗Important:</i></b></span> <b>2×π = 6.28318530718</b>
             <b>2π = Syntax ERROR</b></pre>
</details>'''
)
