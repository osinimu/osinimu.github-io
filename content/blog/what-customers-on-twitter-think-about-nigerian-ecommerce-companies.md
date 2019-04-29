Title: What customers on Twitter think about Nigerian ecommerce companies
Date: 2017-04-03 10:20
Authors: Osinimu
Summary: Nigeria's twitter users and their thoughs on the countrys ecommerce companies.

  
  
  


In a country bereft with inadequate data and in some instances, an alarming absence of data, while the biggest purveyors of the limited collated data, hoard it. Any form of data collation in Nigeria is seen as gold. The range of information conveyed through social media, is limitless. Often these short messages are used to share opinions and sentiments that people have about what is going on in the world around them.

Twitter constitutes a rich source of data that can be used for obtaining information about any topic imaginable. This data can be used in different use cases such as finding trends related to a specific keyword, measuring brand sentiment, and gathering feedback about new products and services. This post was inspired by [Rosebud Anwuri's post](https://theartandscienceofdata.wordpress.com/2016/10/09/what-twitter-feels-about-network-providers-in-nigeria/#more-442) on Nigerian telcos.

I decided to extract data from Twitter about Nigerian e-commerce companies and analyze what customers perceive of these brands, which can in turn help us find out how good their services are. This process is called sentiment analysis. Sentiment analysis is a type of text analytics, a process of determining the emotional tone behind a set of words, gaining an understanding of the the attitudes, opinions and emotions expressed within an online mention. Using this approach I analyzed sentiments in tweets by providing a positive or negative score based on words and Emojis (emoticons). Words like 'angry', 'vex', 'annoyed' appearing in a tweet tend to produce a negative sentiment score while words like 'love', 'like', 'amazed' would do the opposite.Unlike documents, working with informal text genres (like tweets) presents challenges for Natural language processing beyond those typically encountered when working with more traditional text genres. Tweets are short: a sentence or a headline rather than a document. The language used in tweets is very informal, with creative spelling and punctuation, misspellings, slang, new words, URLs, and genre-specific terminology and abbreviations, such as, RT for "retweet" and #hashtags.

\_ Note: it is important point out that Twitter is a very small sample of any e-commerce company's customer base. This means that what may be true for this sample might not necessarily apply to the general population.\_

I collected tweets about four nigerian e-commerce companies (konga, jumia, payporte and yudala) from the 28th June to the 6th of July using the **Twittr** package in R. The collected twitter data came with attributes such as: The tweet, the day and time it was posted, the username who posted and the amount of retweets/favorite the tweet posted. Next thing i did was to clean the tweets removing punctuations, trailing and leading spaces, URLs and other things that don't help the analysis, using the Stringr package. Unsurprisingly the bulk of the time spent was on data cleaning. While the cleaning process was on,i came across a discovery about People talking about konga but were referring to the nigerian musician while others talked about a game named donkey konga. After the tweets were cleaned up, I extracted the emoticons from the tweets and put their descriptions in the tweet data file, having noted that emoticons affords us lots of information. Using the [AFINN](https://finnaarupnielsen.wordpress.com/2011/03/16/afinn-a-new-word-list-for-sentiment-analysis/) lexicon which gives a sentiment score between -5 to 5 for several words i scored the sentiment of each tweet. I created wordclouds using the **wordcloud** package after converting the tweets to a clean corpus using the **tm** and **SnowballC** package. The code can be found [here](https://github.com/osisieke/Twitter-sentiment-analysis). The visualizations of the final data was done using **Tableau**.

Lets see some interesting things about each individual ecommerce company that we found. If you want to have a closer look at the visualizations I'll be using, that can be found [here](https://public.tableau.com/profile/christopher.ajulo#!/vizhome/Book1_21337/Dashboard1).

**Jumia**

One of the frontrunners of in the Nigerian e-commerce scene, jumia operates a model based on both business-to-consumer e-commerce and an online marketplace, which allows retailers to sell their products to customers online via Jumia's platform. With over 14 hubs and its own delivery fleet, jumia has a target population reach exceeding 75%. How much are they utilizing their resources to their advantage and their customer's? Let's have a look.

With an average sentiment score of 0.8, jumia isn't doing bad at all.

The first chart is a trend chart with the yellow line showing the number of tweets and the blue line the average sentiment score. The chart shows that the higher the tweets about jumia the higher the sentiment score. This means that most of the people tweet about jumia when they feel good about them. The second chart shows the emojis related to jumia and their frequency. 71% of the emojis used are positive emojis which reinforces that customers on twitter like jumia. The third chart shows when customers tweet the most about jumia. The peakest hour for customers tweets is by 7am. Customers tweet the most in the mornings and it dwindles as the day goes by.

The size of the words in the wordcloud shows how frequently they were used. The words are mostly positive words with words like joy, smile, discount, just, face and hope being displayed.

**Konga**

Recently konga revealed they have 184,000 active customers (approximately 1.1% of the Nigerian population) kind of disappointing right?I know. Seeing as they are arguably nigeria's biggest internet platform. Are they living up to the hype?

The average sentiment score for konga is 0.76, just below jumia's. I was'nt surprised that that they have the sencond lowest score as they get a lot of stick online. The number of tweets about konga is more consistent than its other competitors. Of all the companies konga had the most negative emojis related to them from a crying face to danger. It's hard to say which time of the day most customers tweet about konga,only that the peakest time for tweets are mostly odd hours of the day. Generally konga gets the most interactions on twitter. Their customers are talking, they just have to listen.

Looking at their wordcloud.

The most used keywords are a mixture of positive and negative words. The words that are incomplete are due to the process called [stemming](https://en.wikipedia.org/wiki/Stemming), that reduces certain words to their base or root form.

**Payporte**

The official sponsor of the recently concluded Big Brother Nigeria reality show, payporte wasn't quite known till they were the lead sponsor for the show. The awareness garnered by payporte due to its marketing strategy whilst sponsoring big brother was massive and it's still paying massive dividends.

Payporte had the highest sentiment score with 1.1. Obviously the residue from the impact made by the reality show is still trickling down into their corner, while making strides to become the third biggest player in the nigerian e-commerce scene. The number of interactions (tweets) for payporte was very consistent with how their customers felt about them on certain day. 86% of the emojis used by customers where positive. Customers tweeted about payporte mostly at noon.

Here words like love, now, will, dancer, get and like can be seen. Not a lot of keywords stand out, eh?

**Yudala**

Launched in late 2015 as Nigeria's first e-commerce player that operates both an online platform and physical retail stores, giving it an edge over established online-only players such as Jumia and Konga. Even Though the omnichannel model seems to be untested by african retailers and is yet to yield dividends for yudala, there are a lot of safe bets on it. Giving voice to the notion that traditional model in Nigeria still has relevance. Lets see how yudala fares on twitter.

Yudala has an average sentiment score of 0.5. This is to be expected as they have the lesser of twitter interactions amongst its counterparts. The highest number of tweets they had on any particular day was 5 on the 31st of May. The emojis used in tweets were only two, both having a sentiment score of 0.Customers seem to tweet mostly at 1pm and their sentiment scores also peaks at that time. Customers of yudala seem to be indifferent to them online, could their strong offline presence be the reason?

Let's look at the most frequent words used in tweets about yudala.

None of the words stand out as negative. Most of the words are generally positive ones.

**Conclusion**

*   Customers of jumia are okay with their service, while
*   konga received most of the complaints of the four, the good words about them sort of overwhelmed those complaints, giving them a balance, still giving them a lot to think about
*   A few customers related to jumia and konga's service to that of amazon.
*   payporte really milked out all they could from the Big brother show, hopefully they keep making such marketing strides.
*   Yudala being relatively new to the space have customers still undecided about them.

It took [almost 20 years](http://www.wired.com/2015/10/get-used-to-amazon-being-a-profitable-company/) before Amazon delivered one dollar of profit from ecommerce but they now have a massive balance sheet and a lot of expertise learned from its mistakes. Since neither of the nigerian ecommerce companies are profitable yet, it would be easy to say the direction for at least one of the companies would be similar to amazon. Until you know that at most there are only 600k active customers shopping online in Nigeria.

The cost of changing customer behaviours is usually high, nonetheless that is the key if any of these companies will win in this space. The ability to quickly understand consumer attitudes and react accordingly is something that organizations should look to take advantage of.

**Disclaimers:**

*   Twitter is a relatively small sample of the customer base of any ecommerce company and the people that are mostly use twitter are millennials. Even Though this might be the target market, what may be true for this sample may not necessarily apply to the population/whole customer base.
    
*   The time period for collecting these tweets is quite short ( 10 days). Maybe i'd keep collecting more tweets.
    
*   There's little possibility of a skew in the analysis due to a lot of promotional tweets (which i tried my best to filter out).
*   Since Jumia isnt isnt only in nigeria,some tweets were from countries such as kenya and egypt.

I'd like to say the analysis can be improved by using a deep learning algorithm, further analyze their delivery service and the quality of their products and also add other ecommerce platforms to the mix.

Thanks for reading.

  
  

*   [The Fine art of relationships](./the-fine-art-of-relationships.html)
*   [The profitable Neighbourhoods in lagos for investing in property.](./the-profitable-neighbourhoods-in-lagos-for-investing-in-property.html)

*   [The profitable Neighbourhoods in lagos for investing in property.](./the-profitable-neighbourhoods-in-lagos-for-investing-in-property.html)

  
  
  

[![Avatar](theme/images/fosi.jpg)](http://christopherajulo.com)

[Ajulo Christopher](http://christopherajulo.com)

  
  
  

Did you like this article? Share it with your friends!
