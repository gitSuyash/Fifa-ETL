# Fifa ETL & Analysis

#### In this repository I've demonstrated how to extract data from different API's, transform it in a meaningful data and finally load it an interpretable form to gain further knowledge from it.

##### Walkthrough:

1. Extract data present in 5 different API's:
    * ```Teams```:"https://montanaflynn-fifa-world-cup.p.rapidapi.com/teams"
    * ```Goals```:"https://montanaflynn-fifa-world-cup.p.rapidapi.com/goals"
    * ```Players```:"https://montanaflynn-fifa-world-cup.p.rapidapi.com/persons"
    * ```Games```:"https://montanaflynn-fifa-world-cup.p.rapidapi.com/games"
    * ```Rounds```:"https://montanaflynn-fifa-world-cup.p.rapidapi.com/rounds"
    
    Note: A key is required to access these API's which can be obtained from ```RapidAPI```
    
2. Transform the json data present into a csv format along with necessary features:
    * Data present is not directly in the format of json, list or dictionary
    * It is of type string(str)
    * Write the functions that extract dictionary part the strings and finally return a DataFrame.
   
3. Load the required data from all 5 sources in a single DataFrame and save it as ```data.csv```
4. Perform analysis on ```data.csv```
