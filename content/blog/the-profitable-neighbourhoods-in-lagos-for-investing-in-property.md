Title: The profitable Neighbourhoods in lagos for investing in property.
Date: 2017-07-21 
Authors: Osinimu
Summary: Best Neighbourhoods in Lagos for investing in property.                              



    

### Are you thinking about buying a property in Lagos State, Nigeria and then renting it out? Then you should stick around to find out the best neighbourhoods to consider.

Actually, how do we go about deciding which Lagos neighbourhood is the least or most profitable? Home to over 14 million people, Lagos is on its way to becoming the [seventh largest urban area in the world by 2020](http://www.citymayors.com/statistics/urban_2020_1.html). This is right after recently obtaining the mega city status. In a society where owning property is regarded as a massive achievement, until you own a property you’re not viewed as one who has accomplished much. Real estate is quite the big deal around these parts.

Property prices in the nation’s former capital are constantly on the rise along with property owners incessantly increasing rent prices. With the massive expansion ongoing in Lagos, property in the suburbs could soon be at home in commercial neighbourhoods instead.

There’s an outcry over a housing problem in Lagos but the bane of this problem isn’t that there are no houses. Actually there are empty houses all over the city; with some staying vacant over a year without being rented out. This is quite the headache for someone looking to invest in Lagos real estate.

Some housing projects remain unoccupied because they are pricey in some neighbourhoods notably Lekki, VI, Ikoyi and Yaba. Nonetheless, developers/investors continue to put up more housing projects. To help navigate through the property market in Lagos, let’s identify which neighbourhoods offer more property investment value.

The ideal neighbourhood for investing in properties would have:

1.  High rental price
2.  Low sale price

#### Web Scraping tolet.com.ng

I decided to collect house pricing data in Lagos for both rental and for sale properties after looking at three major websites; [Property24](https://www.property24.com/), [Privateproperty](https://www.privateproperty.com.ng/)and [Tolet](https://www.tolet.com.ng/). Compared to the other websites, Tolet search results reveal more information, with the format of each listing being consistent which is splendid for web scraping. (This analysis is based on active listings on tolet.com.ng as at 23/08/2017).

I web scraped tolet.com.ng using the python scrapy library, then created two spiders, one each for rent and sale properties. I then made a list of 40 Lagos neighbourhoods and categorised each listing address into one of these neighbourhoods.

Certain neighbourhoods were categorised into one e.g Magodo Phases 1 and 2, Shangisha was categorised into Ikosi and also Lekki Phases 1 and 2 into Lekki.

![List of neighborrhoods in Lagos](/images/neigh.PNG)

#### Cleaning and Manipulating the data

For the listings in both the sale and rent datasets, the price columns contained unwanted text like; “\_/ year”, “ / sqm” , and “ / day”. \_Such text was discarded.

A new column for categorising each listing’s address into a singular neighborhood was created. This was called “Neighborhood”. The neighborhood of each listing was obtained by matching the list of neighbourhoods created earlier against corresponding listing addresses, and outputting the first match as the values for the neighbourhood column.

#### Finding the Least/Most investable neighbourhoods in Lagos

After cleaning up the data it was time for some analysis. Needing a way to evaluate each neighbourhood, I had to compare the rental and sale prices. So for each neighbourhood I calculated the average price for properties, up for rent and for sale.

![avg price for rent and sale](/images/avg_prices.png)

calculate average price for both rental and sale properties

Let’s have a look at the dataset before we start weighing the rental and sale prices. I observed from the data set that some neighbourhoods have very few listings or almost none at all. Epe and Ijora both had just 1 listing each, while Ifako-Ijaiye had 3.

![dataset lookup](/images/sas.png)

Average prices for sale and rent properties.

The low number of listings can introduce imbalance and also lead to incorrect results. Hence I excluded neighbourhoods with less than or equal to five listings to guarantee the quality of the data.

![Visualizing the number of listings](/images/download.png)

Visualizing the number of listings

Some Instances of neighbourhoods with more than 5 listings are; Ajah with an average sale and rent price of 108,854,718.358 Naira and 1,041,328.82 Naira respectively, Apapa with an average sale and rent price of 26303458333.333 Naira and 16702858.065 Naira respectively.

![Neighbourhoods with more than 5 listings](/images/husey.png)

Neighbourhoods with more than 5 listings.

We can look for a linear relationship between the average sale price and the average rent price; if it costs more to buy, it should cost more to rent.

I would also be considering the outliers in this linear regression. Outliers are data points that do not follow the general trend of the rest of the data. There are two types of outliers in our plot below:

1.  Outliers that are located above the regression line with abnormally high sale price (Orile, Apapa)
2.  Outliers that are located below the regression line with abnormally low sale price (Ikoyi)

Type 2 outliers are more likely to be profitable and Type 1 outliers are less likely to be profitable.

![Linear regression plot of rent prices ~ sale prices](/images/reg-code.png)

Linear regression plot of rent prices ~ sale prices

![Linear regression plot of rent prices ~ sale prices](/images/linear-regression.png)

Visualization of the linear relationship between average rent and sale price.

Examining the plot above, we can see points above and below the regression line. Outliers are the extreme cases in these circumstances. The points above the regression line have a higher average sale value than the fitted values, signifying that they are less likely to be profitable. On the other hand, the point below the regression line has a higher average rental price than the fitted values hinting at the tendency of being profitable.

Compared to other apartments with over ₦10,000,000 average rental price, Ikoyi has the lowest average sale price of ₦867,429,147,alluding to its profitability given rental price is over ₦10,000,000. However it is not clarified that Ikoyi is the most profitable neighbourhood when compared to the other neighbourhoods below the regression line.

For instance Ejigbo with an average sale price of ₦32,647,058.824 and an average rent price of ₦1,325,000 is far more profitable than Ikoyi with an average sale price of ₦867,429,147 and an average rent price of ₦11,131,547 Naira. Even though Ejigbo is not an outlier.

To precisely ascertain the profitabilities, I computed the ratio of average rent price over average sale price and plotted the distribution of the ratios.

![Distribution of the ratio of average rent price to average sale price
](/images/ratio-dist.png)

Distribution of the ratio of average rent price to average sale price

From this analysis, the top 5 least profitable neighbourhoods are listed, with the results matching the linear regression analysis.

![Top 5 leat Profitable Neighbourhoods in Lagos
](/images/least-profitable.png)

Top 5 least Profitable Neighbourhoods in Lagos

The top 5 most profitable neighbourhoods are shown beneath, with Ikorodu and Ejigbo leading the way. We can see here that Ikoyi isn’t even in the top 5.

![Top 5  Profitable Neighbourhoods in Lagos
](/images/top-profitable.png)

Top 5 Profitable Neighbourhoods in Lagos

The properties in these neighbourhoods have a low sale price and a high rental price. So if you’re contemplating investing in some real estate, buying properties from these neighbourhoods and putting them up for rent would be worth your while.

#### Challenges

While it would be nice to claim this entire exercise was a breeze, it would be dishonest to leave out the challenges I faced. As with any meaningful endeavour in life, there were a few mitigating factors to deal with. The bigger issues included:

*   Navigating round the poorly planned city addresses. Street names have ambiguous formats like; “Awolowo Way,” “Obafemi Awolowo Way” or “Chief Obafemi Awolowo Way,” and it’s confusing to know which exactly is which. This issue led me to group the the listings into the most common/general neighbourhoods.
*   I intended to compare the rent and sale properties by getting their price averages and dividing that by their sizes(per square meters). Tragically, a dearth of information on the sizes of listed houses, on the websites referenced earlier forced my hand . I had to settle for just the average prices as the benchmark for comparing the rent and sale properties.

This analysis doesn’t account for taxes, mortgage, insurance payments, and other fees. It can be improved upon by going ahead to predict house prices using machine learning, if a more detailed dataset is made available. The dataset for future exploration would include characteristics such as; size per square meter of a property, unemployment rate, school rating, distance to major employment centres, accessibility to highways, and etc.

However, I found such data difficult to access.The availability of such statistics in public domain would provide much more insight into how these factors all affect property prices..

This information could be very useful for future investments and research.

The full code for this analysis can be found here: [https://github.com/osisieke/tolet-housing-price-analysis/](https://github.com/osisieke/tolet-housing-price-analysis/)

