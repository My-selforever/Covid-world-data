import pandas as pd
import plotly_express as px

df = pd.read_csv('Copy+of+data+-+data.csv')
graph = px.scatter(df,x='date',y='cases',color='country')
graph.update_layout(plot_bgcolor='#000000')
graph.show()