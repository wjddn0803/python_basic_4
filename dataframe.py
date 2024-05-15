# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    df = pd.read_csv("gapminder.tsv", sep="\t") # 데이터프레임으로 반환
    return df

def plot_matplotlib():
    st.ti("**Bar Plot** with Seaborn")
    df = load_data() # 데이터 불러오기->데이터프레임 구조 변환
    fig, ax = plt.subplots() # 시각화
    
    # Using Seaborn's barplot function
    sns.barplot(x=df['year'], y=df['lifeExp'], data=df, ax=ax)
    
    # Labeling axes and title
    ax.set_xlabel("year")
    ax.set_ylabel("lifeExp")
    ax.set_title("Year vs. lifeExp")
        
    st.pyplot(fig) # streamlit에 그리기

def main():
    st.title("Data Display st.dataframe()")
    st.checkbox("Use container width", value=False, key = 'use_container_width')
    
    df = load_data()
    st.dataframe(df, use_container_width=True)

    #pandas style
    st.dataframe(df.iloc[:5,2:].style.highlight_max(axis=0))

    plot_matplotlib()
    
    
if __name__ == "__main__":
    main()