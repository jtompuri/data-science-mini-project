import pandas as pd
import json

records = []
with open('Kansanedustajien_puheet.ndjson', 'r', encoding='utf-8') as f:
    for line in f:
        records.append(json.loads(line))

data = pd.json_normalize(records)

#Dropping empty columns
empty_columns = [col for col in data.columns if data[col].isna().all()]
data = data.drop(columns=empty_columns)
other_dropped_coloumns = ["puheenvuoro.historiallinen", "type", "puheenvuoro.tunnus.fi", "puheenvuoro.tunnus.sv", "puheenvuoro.poytakirjanasiankohta.sv.eduskuntatunnus",
       "puheenvuoro.poytakirjanasiankohta.sv.kohtanumero", "puheenvuoro.poytakirjanasiankohta.sv.nimeketeksti", "puheenvuoro.asiakirjaviitteet.fi", "puheenvuoro.asiakirjaviitteet.sv",
       "puheenvuoro.puheenjohtajanRepliikki.puheenjohtaja", "puheenvuoro.puheenjohtajanRepliikki.repliikki", "puheenvuoro.puheenjohtajanRepliikki.asiakohtaAsiakirjaViitteet"]

#Dropp other irrelevant columns. Only value for column "puheenvuoro.historiallinen" is "False"
data = data.drop(columns=other_dropped_coloumns)

#Creating a support table for content analysis of selected columns
column_content_analysis = data[["puheenvuoro.tila", "puheenvuoro.puheenvuorotyyppikoodi", "puheenvuoro.puheenvuorotyyppinimi", "puheenvuoro.valtiopaiva"]]

with open('dropped_columns.txt', 'w') as f:
    f.write("Following columns were empty and therefore dropped out:"+"\n")
    for col in empty_columns:
        f.write(col + '\n')
    f.write("\n")
    f.write("Following columns were not seen relevant and therefore dropped out:")
    for col in other_dropped_coloumns:
            f.write(col + '\n')

with open('column_content_analysis.txt', 'w') as f:
    f.write("Content of some selected columns left in"+"\n")
    f.write("\n")
    for column in column_content_analysis.columns:
        f.write("Column:" + column)
        f.write(data[column].value_counts().to_string())
        f.write("\n")
        f.write("\n")

data.to_json("cleaned_data.ndjson", orient="records", lines=True, force_ascii=False)