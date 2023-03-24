'''
import statements
        import pandas as pd
        import numpy as np
reading csv file into the dataframe(df is just a set of rows and columns) df is a 2d data structure mainly rows and cols
        df=pd.read_csv(path)
gathering information related to dataframe
        print(df.head())
        df.shape        display a tuple of rows and cols (row,col)
        df.info()
                        display all rows and columns
                                pd.set_option('display.max_columns()',noofcols)
                                pd.set_option('display.max_rows()',noofrows)

        df.head()       #we can get first n rows using df.head(n)
        df.tail()       #we can get last n rows using df.tail(n)

accessing elements of dataframe 
    prints the values in the column
    bracket notation
        df['columnname']  #prints a list of data called series
                            #series data is a 1d array in simple terms it is mainly rows of data it basically is a single column data
                            #dataframe if a collection of series object or combination of multiple series objects
    dot notation
        peopledf1.name  #print name column using dot notation only problem this has is it considers the columns as attributes and may
                        #mix up with other attributes that may be keywords example:- count

    accessing multiple columns at a time
        peopledf1[['name','Rollno']]  #to access multiple columns of a dataframe we cannot directly put comma and access it 
                                      #df['key1','key2'] is wrong and will give a key error ❌
                                      #correct way of accessing mutiple columns of a dataframe is by passing a list of columns in the 
                                      #bracket notation
                                      #df[[key1,key2,key3]] ✅

    printing all the columns in our dataframe with datatype
        peopledf1.columns
                        
    printing all the rows of the dataframe 
        this can be done using 2 ways 

        ****main point to note is in loc and iloc both the values in range are inclusive****
            .loc,.iloc,.at all are called as indexers as we can access values of dataframe using indices in these attributes of df 
                df.loc -> can print values according to labels or we can pass column names in the arguement.
                df.iloc -> stands for integer locations we can access columns only using integer values.

                df.loc[0]
                df.loc[[0,2]] prints 1st and 3rd row from the dataframe
                df.loc[[0,1],'name']
                df.loc[[0,1],['name','roll']] prints 1st and 2nd row and only specified columns

                df.iloc[0]
                df.iloc[[0,2]] prints 1st and 3rd row from the dataframe
                df.iloc[[0,1],[0]]
                df.iloc[[0,1],[0,2]] prints 1st and 2nd row and only specified columns

                df.loc[0:12,cols1:cols2] both 0,12,cols1,cols2 inclusive

Setting up indexes for the dataframe -> indexes are the fastest way to uniquely identify a row in the dataframe
            peopledf1.set_index('colname',inplace=True)  #here colname will be set as an index, inplace=True makes the changes permanant👀👀
                                                        #unless there is no inplace=True no permanant changes are made to the dataframe
                                          #after colname is set as index, the default indices of 0 to n-1 are replaced by the colname column
                                            #as we know that for accessing row elements we have 2 functions -> loc and iloc
                                            #loc now will access the row elements using the new index set by user that is colname
                                            #peopledf1.loc[16] ->rollno=16 row will be accessed
                                            #peopledf1.iloc[0] ->for iloc there will be no changes, here the elements will be accessed using normal
                                            #index
                                            #after changing the index the new index column wont be the part of main dataframe rather it will be 
                                            #the part of indexes now

                                            accessing specified cols by loc when custom index is set
                                            peopledf1.loc[16,'name']
                                            peopledf1.loc[16,['name','year']]

            df=pd.read_csv(path,index_col="colname") #creating index while creating the dataframe

            peopledf1.reset_index(inplace=True) #by this method we can reset the index to default index make it permanant using inplace=True
    #setting up index is also a form of data cleaning
    here we can see that the respondant column has unique values in it so that can be the index for df than default index which     
    also starts from 0 hence this will be a part of data cleaning where the default index is removed and inbuilt column index is set

    indexes make searching by labels very easy

            df.sort_index(inplace=True)  #sorting the columns and index
                                          in descending= df.sort_index(ascending=False,inplace=True)

Filter out data according to specification

    df[df[cols]==value]
    dataframe[[dataframe]==condition]]
    filt=df[df[col]==condition]
    df[filt]
    df.loc[filt,[cols]]
    filt=((df[df[cols]=condition]) &/| (df[df[cols]=condition])
                                  and/or
    df[filt]
    df.loc[filt,[cols]]

    apply opposite of filter condition
    df[~filt]
    df.loc[~filt,[cols]]

    example of single condition filtering:-
            highsal=df['ConvertedComp']>70000
            df.loc[highsal,['Country','DevType','LanguageWorkedWith','LanguageDesireNextYear']]

    example of multicondition filtering:-
            countries=['United States','India','United Kingdom','Germany','Canada']
            countryfilter=df['Country'].isin(countries) #df[ele].isin(list) can be used to match the coloumns according to list values
            df.loc[countryfilter,['Country','DevType','LanguageWorkedWith','LanguageDesireNextYear','ConvertedComp']]

            fil=df['LanguageWorkedWith'].str.contains("Python",na=False) #.str.contain(string) checks for substring in the object of dataframe
            df.loc[fil,['Country','ConvertedComp']] #remember to learn string methods in pandas

            filters basically return a series of true false values and then the loc applies this filter on individual rows 
            and prints the true ones

Changing the column names or attributes of the dataframe
            df.columns -> prints the column name of the dataframe 
            df.columns = ['name1','name2','name3'] -> this changes the column names from old names to new names
    changing the case of column names can be done using list comprehension
            df.columns=[i.upper() for i in df.columns]
            df.columns=[i.lower() for i in df.columns]
    changing column names by replacing certain elements of column name
        (" " replaced by underscore) -> 
            df.columns=[i.replace(" ","_") for i in df.columns]
    renaming specific columns in the dataframe
            df.rename(columns={'oldval':'newval',},inplace=True) ->mapping using dictionary

Updating the values of rows/ changing the values of the rows
        df.loc[index,[cols]]=[new values]
        example:-
        updating all values of a column in the dataframe
            peopledf1.loc[0]=[16,'Prathamesh Sanjay',"Patil",'TE']

        updating specific columns from the dataframe(single)
            peopledf1.loc[0,'first']='Prathamesh'

        updating specific columns from the dataframe(multiple)
            peopledf1.loc[0,['first','last']]=['Prathamesh','Patil]

        updating values of a row using filter
            filt=peopledf1['rollno']==16
            peopledf1.loc[filt,'first']='Prathamesh'
        
        changing the case of a column data
            peopledf1['first']=peopledf1['first'].str.lower() ->this can only be applied on a series data and not the dataframe


we can convert python dictionary to dataframe
dict={
    key1:[val1,val2....]
    key2:[val1,val2....]
    key3:[val1,val2....]
}
        df=pd.DataFrame(dict)  #here keys become column and values become rows

'''
