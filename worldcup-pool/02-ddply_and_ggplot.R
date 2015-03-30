require(ggplot2)
require(plyr)

setwd('C:/learnpython/plots/worldcup-pool')

df <- read.csv("munged.csv")

df2 <- ddply(df, .(Owner), transform, pts = cumsum(Pts))

g <- ggplot(df2, aes(x = day_num, y = pts, color = Owner)) + theme_classic(base_size=18)
g + geom_step(size=2, alpha = 0.5) + 
    labs(x = 'Tournament Day', y = "Cumulative Points", title = '2015 ICC Cricket World Cup Pool') +
    guides(colour = guide_legend(override.aes = list(alpha = 1))) +
    scale_x_continuous(breaks = seq(0,43,5)) + scale_y_continuous(breaks = seq(0,31,5)) +
    annotate("rect", xmin=0, xmax=30,ymin=0,ymax=28, alpha=.2, fill='lightgray') +
    annotate("text", x=10, y=20, label='Group Stage', size=7)