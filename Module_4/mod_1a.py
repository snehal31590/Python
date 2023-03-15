import pandas as pd

df = pd.DataFrame({"Name": ["Tom","Mike", "Tiffany", "Varada" , "Joel"],
                    "2018" :[1,3,4,5,3],
                    "2019" :[2,4,3,2,1],
                    "2020" : [5,2,4,4,3]})


df
# Melt method to make wide data -- to Long
df.melt(
    id_vars="Name",
    var_name="Year",
    value_name="Courses"
)

# or

df.melt(
    id_vars="Name",
    value_vars=["2018","2019","2020"],
    var_name="Year",
    value_name="Courses"
)

## Long to Wide change

df_1 = pd.DataFrame({
    "Name": ["Tom","Mike", "Tiffany", "Tom" , "Mike","Tiffany"],
    "Variable" :["Year","Year","Year","Courses","Courses","Courses"],
    "Value" :[2018,2018,2018,1,3,4]
})

df_1

df_1.pivot(
    index="Name",
    columns="Variable",
    values="Value"
 )

 # Resolve the indexing issue

df_1.pivot(
    index="Name",
    columns="Variable",
    values="Value"
 ).reset_index()


# Replace a column name

df_1.columns.name = None
df_1


