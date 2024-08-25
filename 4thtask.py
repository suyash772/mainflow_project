import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


df= pd.read_csv('D:/download/USvideos.csv')
pd.set_option('display.max_columns', 50)
print(df.head())
print()
print("*"*200)

print(df.shape)
print("*"*200)
print()

df= df.drop_duplicates()
print(df.shape)
print("*"*200)

print(df.describe())
print("*"*200)

print(df.info())
print("*"*200)

remove_columns = ['thumbnail_link','description']
df= df.drop(columns=remove_columns)
print(df.info)
print(df.shape)

print("*"*200)
print()

import datetime

df["trending_date"]=df["trending_date"].apply(lambda x: datetime.datetime.strptime(x, "%y.%d.%m"))
print(df.head(3))
print("*"*200)

df['publish_time'] = pd.to_datetime(df['publish_time'])
print(df.head(3))
print("*"*200)

df['publish_month']=df['publish_time'].dt.month
df['publish_day']= df['publish_time'].dt.day
df['publish_hour']=df['publish_time'].dt.hour
print(df.head(3))
print("*"*200)

print(sorted(df["category_id"].unique()))
[1,2,10,15,17,19,20,22,23,24,25,26,27,28,29,30,43]

df['category_name']=np.nan
df.loc[df['category_id']==1,'category_name']='film and animals'
df.loc[df['category_id']==2,'category_name']='autos and vehicals'
df.loc[df['category_id']==10,'category_name']='music'
df.loc[df['category_id']==15,'category_name']='pets and animals'
df.loc[df['category_id']==17,'category_name']='sports'
df.loc[df['category_id']==19,'category_name']='travels and events'
df.loc[df['category_id']==20,'category_name']='gaming'
df.loc[df['category_id']==22,'category_name']='people and blogs'
df.loc[df['category_id']==23,'category_name']='comedy'
df.loc[df['category_id']==24,'category_name']='entertainment'
df.loc[df['category_id']==25, 'category_name']='news and politics'
df.loc[df['category_id']==26,'category_name']='how to and style'
df.loc[df['category_id']==27,'category_name']='education'
df.loc[df['category_id']==28,'category_name']='science and technology'
df.loc[df['category_id']==29,'category_name']='non profit activities'
df.loc[df['category_id']==30,'category_name']='movies'
df.loc[df['category_id']==43,'category_name']='shows'

print(df.head())
print("*"*200)
print()

df['year']=df['publish_time'].dt.year
yearly_counts= df.groupby('year')['video_id'].count()

#create a bar chart
yearly_counts.plot(kind='bar',xlabel='Year',ylabel='Total publish count',title='Total publish video per year')
plt.show()

#group by year and sum the views for each year
yearly_views= df.groupby('year')['views'].sum()

#create a bar chart
yearly_views.plot(kind='bar',xlabel='Year',ylabel=' total Views',title='Total views per year')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

#group the date by 'category name' and calulate the sum of 'views' in each category
category_views= df.groupby('category_name')['views'].sum().reset_index()

#sort the category by views in descending order
top_catgories= category_views.sort_values(by='views', ascending=False).head(5)

#create a bar chart to vissualize top 5 category
plt.bar(top_catgories['category_name'], top_catgories['views'])
plt.xlabel('Category name',fontsize=15)
plt.ylabel('total Views',fontsize=15)
plt.title('Top 5  category',fontsize=15)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,6))
sns.countplot(x='category_name', data=df,order=df['category_name'].value_counts().index)
plt.xticks(rotation=90)
plt.title('video count by category')
plt.show()

#count of number of videos published per hour
videos_per_hour= df['publish_hour'].value_counts().sort_index()

#create a bar plot
plt.figure(figsize=(12,6))
sns.barplot(x=videos_per_hour.index, y=videos_per_hour.values,palette='rocket')
plt.title('Number of Videos published per hour')
plt.xticks(rotation=45)
plt.xlabel('hour of day')
plt.ylabel('number of videos')
plt.show()

#line plot
df['publish_time']=pd.to_datetime(df['publish_time'])
df['publish_date']=df['publish_time'].dt.date
videos_count_by_date= df.groupby('publish_date').size()
plt.figure(figsize=(12,6))
sns.lineplot(data=videos_count_by_date)
plt.title("videos publish over time")
plt.xlabel('publish date')
plt.ylabel('number of videos')
plt.xticks(rotation=45)
plt.show()


#scatter plot between 'views' and 'likes'
sns.scatterplot(data=df,x='views',y='likes')
plt.title("views vs likes")
plt.xlabel('views')
plt.ylabel('likes')
plt.show()

plt.figure(figsize = (14,8))
plt.subplots_adjust(wspace = 0.2, hspace = 0.4, top = 0.9)
plt.subplot(2,1,1)

g = sns.countplot(x="comments_disabled", data=df)
g.set_title("Comments_Disabled", fontsize=16)
plt.subplot(2,2,2)

g1 = sns.countplot(x='ratings_disabled', data=df)
g1.set_title("Ratings_Disabled", fontsize=16)
plt.subplot(2,2,3)

g2 = sns.countplot(x='video_error_or_removed', data=df)
g2.set_title("Video_Error_or_removed", fontsize=16)
plt.show()