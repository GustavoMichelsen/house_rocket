import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')

@st.cache(allow_output_mutation=True)
def import_data(path):
    data = pd.read_csv(path)
    return data

def m2(data):
    data['m2'] = round(data['sqft_living'] * 0.092903, 2)
    return data

def data_resale(data, df_range, df_renovated, df_basement):
    price = (data[(data['m2_range'] == df_range) & (data['condition'] >= 4)]['price'].mean()) * 0.7
    data = data[(data['m2_range'] == df_range) & (data['condition'] >= 4) & (data['price'] <= price)]
    if df_renovated == 'sim':
        data = data[data['yr_renovated'] > 0]
    elif df_renovated == 'não':
        data = data[data['yr_renovated'] == 0]
    if df_basement == 'sim':
        data = data[data['sqft_basement'] > 0]
    elif df_basement == 'não':
        data = data[data['sqft_basement'] == 0]
    data = data[(data['condition'] >= 4)].sort_values('price').reset_index()
    return data

def data_renovated(data, df_range, df_renovated, df_basement):
    price = (data[(data['m2_range'] == df_range) & (data['condition'] <= 2)]['price'].mean()) * 0.65
    data = data[(data['m2_range'] == df_range) & (data['condition'] <= 2) & (data['price'] <= price)]
    if df_renovated == 'sim':
        data = data[data['yr_renovated'] > 0]
    elif df_renovated == 'não':
        data = data[data['yr_renovated'] == 0]
    if df_basement == 'sim':
        data = data[data['sqft_basement'] > 0]
    elif df_basement == 'não':
        data = data[data['sqft_basement'] == 0]
    data = data[(data['condition'] <= 2)].sort_values('price').reset_index()
    return data


def recommendation(data, data2=False, r_range=1):
    if isinstance(data2, bool):
        mean_price = data['price'].mean()
        data = data.head(5)
        data['target'] = mean_price
        data['profit'] = round(data['target'] - data['price'], 2)
    else:
        mean_price = data2[(data2['m2_range'] == r_range) & (data2['condition'] >= 4)]['price'].mean()
        data = data.head(5)
        data['target'] = mean_price
        data['budget'] = round((data['price'] * 1.2) - data['price'], 2)
        data['profit'] = round(data['target'] - data['price'] - data['budget'], 2)
    return data

def mapa(data):
    mapa = px.scatter_mapbox(data,
                             lat='lat',
                             lon='long',
                             color_continuous_scale=px.colors.cyclical.IceFire,
                             color='zipcode',
                             size='price'
                             )
    mapa.update_layout(mapbox_style='open-street-map')
    mapa.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0}, coloraxis_showscale=False)
    return mapa

def head():
    st.title('House Rocket - An Imaginary Company')
    return None

def resale_houses(data):
    st.header('Casas para revenda')

    with st.expander("Clique para ver as Casas para Revenda."):
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            r_range = st.slider('Selecione o tamanho da casa',
                                int(data[data['condition'] >= 4]['m2_range'].min()),
                                int(data[data['condition'] >= 4]['m2_range'].max()),
                                3)
            st.text('Tamanho da casa de {} a {} metros quadrados.'.format(r_range * 50, (r_range * 50) + 50))
        with col2:
            r_basement = st.radio('Casas com porão', ['todos', 'sim', 'não'], horizontal=True)
        with col3:
            r_renovated = st.radio('Casas que foram reformadas', ['todos', 'sim', 'não'], horizontal=True)

        df_resale = data_resale(data, r_range, r_renovated, r_basement)

        col1, col2 = st.columns([1.1, 1.7])

        with col1:
            st.subheader('Top 5 casas para revenda')
            df_head = recommendation(df_resale)
            st.dataframe(
                df_head[['id', 'bedrooms', 'bathrooms', 'm2', 'price', 'profit']].style.format({'bathrooms': '{:.0f}',
                                                                                                'm2': '{:.0f}',
                                                                                                'price': '{:.2f}',
                                                                                                'profit': '{:.2f}'}))
            st.text('O preço médio para o tamanho da casa: ${}'.format(round(df_resale['price'].mean(), 2)))
            recommendation_only = st.checkbox('Mostrar apenas recomendações no mapa.')

        if recommendation_only == True:
            fig = mapa(df_head)
        else:
            fig = mapa(df_resale)
        with col2:
            st.plotly_chart(fig)
    return None

def renovation_houses(data):
    st.header('Casas para Reforma e Venda')
    with st.expander("Clique para ver as Casas para Reforma e Venda."):
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            ren_range = st.slider('Selecione o tamanho da casa',
                                  int(data[data['condition'] <= 2]['m2_range'].min()),
                                  int(data[data['condition'] <= 2]['m2_range'].max()),
                                  3)
            st.text('Tamanho da casa de {} a {} metros quadrados.'.format(ren_range * 50, (ren_range * 50) + 50))
        with col2:
            ren_basement = st.radio('Casas com porão.', ['todos', 'sim', 'não'], horizontal=True)
        with col3:
            ren_renovated = st.radio('Casas que foram reformadas.', ['todos', 'sim', 'não'], horizontal=True)

        df_renovated = data_renovated(data, ren_range, ren_renovated, ren_basement)

        col1, col2 = st.columns([1.1, 1.7])

        with col1:
            st.subheader('Top 5 casas para Reforma.')
            df_head_renovated = recommendation(df_renovated, data, ren_range)
            st.dataframe(
                df_head_renovated[['id', 'bedrooms', 'bathrooms', 'm2', 'price', 'budget', 'profit']].style.format(
                    {'bathrooms': '{:.0f}',
                     'm2': '{:.0f}',
                     'price': '{:.2f}',
                     'budget': '{:.2f}',
                     'profit': '{:.2f}'}))
            st.text('O preço médio para o tamanho da casa: ${}'.format(round(df_renovated['price'].mean(), 2)))
            recommendation_only_ren = st.checkbox('Mostrar apenas recomendações no mapa')

        if recommendation_only_ren == True:
            fig = mapa(df_head_renovated)
        else:
            fig = mapa(df_renovated)
        with col2:
            st.plotly_chart(fig)
    return None

if __name__ == "__main__":
    # Extract
    path = 'kc_house_data.csv'
    data = import_data(path)

    # Trasnformation
    data = m2(data)
    data['m2_range'] = data['m2'].apply(lambda x: int((x//50)+1))
    head()
    resale_houses(data)
    renovation_houses(data)