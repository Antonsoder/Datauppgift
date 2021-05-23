#Importerar alla moduler som används senare
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash_core_components as dcc

#Importerar olika datasets med hjälp av pandas
df_linje = pd.read_csv("National_Daily_Deaths.csv")
df_piechart = pd.read_csv("Gender_Data.csv")
df_icus = pd.read_csv("National_Daily_ICU_Admissions.csv")

#App variabeln för dash
app = dash.Dash(__name__)

#Skapar diagram med hjälp av plotly express och använder mig av datatyperna som definieras ovanför
fig_linje_deaths = px.line(df_linje, x="Date", y="National_Daily_Deaths", title="Antal döda/dag")
fig_linje_icus = px.line(df_icus, x="Date", y="National_Daily_ICU_Admissions", title="Antal intensivvård/dag")

#Här börjar jag använda mig utav html, detta är samm sak som body
app.layout = html.Div(children=[

    #Ett element där grafen skapas med ett id (daily_deaths) och en figure.
    dcc.Graph(
        id="daily_deaths",
        figure=fig_linje_deaths
    ),

    #Ett element där grafen skapas med ett id (daily_icus) och en figure.
    dcc.Graph(
        id="daily_icus",
        figure=fig_linje_icus
    ),

    #Ett element som skapar en dropdown menu där man kan välja mellan olika data som ändrar grafen och innehåller ett default value och ett id (value).
    dcc.Dropdown(
        id="value",
        options=[
            {'label': 'Totala fall', 'value': 'Total_Cases'},
            {'label': 'Totala intensivvårdade', 'value': 'Total_ICU_Admissions'},
            {'label': 'Totala dödsfall', 'value': 'Total_Deaths'}
        ],
        value='Total_Cases'
    ),
    #Ett element där grafen skapas med id (pie-chart)
    dcc.Graph(id="pie-chart"),


])


#Callback för att kunna ändra grafen beroende på vad man har valt i dropdown menyn alltså input och output (datan ändras).
@app.callback(dash.dependencies.Output("pie-chart", "figure"), [dash.dependencies.Input("value", "value")])

#En funktion som skapar piecharten och används i callbacken.
def Piechart(value):
    fig = px.pie(df_piechart, values=value, names="Gender", title="Kön")
    return fig

#Här körs hela appen.
if __name__ == '__main__':
    app.run_server(debug=True)