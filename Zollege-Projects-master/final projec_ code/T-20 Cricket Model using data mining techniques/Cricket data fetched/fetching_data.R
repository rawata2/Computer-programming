#gathering the data

#set working directory 
setwd("C:/Users/kuldeep/Desktop/Desktop KuldeepCollege/code for fetching data")

# open library 
library(XML)
library(htmltab)

#EPSN crick website URL
url1<- "http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=3;id=2005;type=year"
url2<- "http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=3;id=2006;type=year"
url3<- "http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=3;id=2007;type=year"
url4<- "http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=3;id=2008;type=year"
url5<- "http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=3;id=2009;type=year"
url6<- "http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=3;id=2010;type=year"
url7<- "http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=3;id=2011;type=year"
url8<- "http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=3;id=2012;type=year"
url9<- "http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=3;id=2013;type=year"
url10<- "http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=3;id=2014;type=year"
url11<- "http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=3;id=2015;type=year"
url12<- "http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=3;id=2016;type=year"
url13<- "http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=3;id=2017;type=year"
url14<- "http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=3;id=2018;type=year"

# reading the data from the web page
year2005<- readHTMLTable(url1, which = 1)
year2006<- readHTMLTable(url2, which = 1)
year2007<- readHTMLTable(url3, which = 1)
year2008<- readHTMLTable(url4, which = 1)
year2009<- readHTMLTable(url5, which = 1)
year2010<- readHTMLTable(url6, which = 1)
year2011<- readHTMLTable(url7, which = 1)
year2012<- readHTMLTable(url8, which = 1)
year2013<- readHTMLTable(url9, which = 1)
year2014<- readHTMLTable(url10, which = 1)
year2015<- readHTMLTable(url11, which = 1)
year2016<- readHTMLTable(url12, which = 1)
year2017<- readHTMLTable(url13, which = 1)
year2018<- readHTMLTable(url14, which = 1)

#combining all the data 
all <- rbind(year2005,year2006,year2007,year2008,year2009,year2010,year2011,year2012,year2013,year2014,year2015,year2016,year2017,year2018)
print(all)
#saving as a csv file
write.csv(all,"t20_team_match_since_2005.csv")


# Indian team player data
itp<- "http://stats.espncricinfo.com/ci/engine/records/batting/highest_career_batting_average.html?class=3;id=6;type=team"
players <- readHTMLTable(itp, which = 1)
print(players)
write.csv(players,"indian_team_player.csv")

# Margin of victory
mv<- "http://stats.espncricinfo.com/ci/content/records/283283.html"
mv1 <- readHTMLTable(mv, which = 1)
write.csv(mv,"Largest_margin_of_victory(by runs).csv")

#runs in T20
mr<- "http://stats.espncricinfo.com/ci/content/records/282827.html"
mrt <- readHTMLTable(mr, which = 1)
write.csv(mrt,"Most_runs_inT20.csv")

#most runs in career
mwc<- "http://stats.espncricinfo.com/ci/content/records/284262.html"
mwct <- readHTMLTable(mwc, which = 1)
write.csv(mwct,"Most_wicket_taken_by bowler.csv")

# batting
bat<- "http://stats.espncricinfo.com/ci/content/records/282902.html"
bat1 <- readHTMLTable(bat, which = 1)
write.csv(bat1,"T20Is - Batting.csv")

# Bowling
bowl<- "http://stats.espncricinfo.com/ci/content/records/283194.html"
bowl1 <- readHTMLTable(bowl, which = 1)
write.csv(bowl1,"T20Is - Bowling.csv")

#fielding
field<- "http://stats.espncricinfo.com/ci/content/records/283641.html"
field1 <- readHTMLTable(field, which = 1)
write.csv(field1,"T20Is - Fielding.csv")

#ICC rankings
icc<- "http://www.firstpost.com/firstcricket/t20-ranking/"
icc1 <- readHTMLTable(icc, which = 1)
write.csv(icc1 ,"T20Is - ICC Rankings.csv")

#patnership
pat<- "http://stats.espncricinfo.com/ci/content/records/283622.html"
pat1 <- readHTMLTable(pat, which = 1)
write.csv(pat1,"T20Is - Partnerships.csv")

# All data was gathered from cricket website ESPNCricinfo.com
# All data gathered from the following links : 
# http://stats.espncricinfo.com/ci/engine/records/index.html?class=3
# http://www.firstpost.com/firstcricket/t20-ranking/
# http://stats.espncricinfo.com/ci/content/records/335433.html
# http://stats.espncricinfo.com/ci/content/records/283291.html
# http://stats.espncricinfo.com/ci/content/records/283301.html
# Please note some data is also scarped using google scrapper.from ESPNCrickInfo.com
# https://chrome.google.com/webstore/detail/scraper/mbigbapnjcgaffohmbkdlecaccepngjd