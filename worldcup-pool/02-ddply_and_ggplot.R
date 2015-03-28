require(ggplot2)
require(plyr)

setwd('C:/learnpython/hacks')

df <- read.csv("munged.csv")

df2 <- ddply(df, .(Owner), transform, pts = cumsum(Pts))

g <- ggplot(df2, aes(x = day_num, y = pts, color = Owner)) + theme_classic(base_size=18)
g + geom_line(size=2, alpha = .5) + labs(x = 'Tournament Day', y = "Cumulative Points", title = '2015 ICC Cricket World Cup Pool')