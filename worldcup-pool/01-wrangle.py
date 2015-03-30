import pandas as pd
df = pd.read_csv("CWC Schedule.csv")

def left(subj):
    marker = subj.find("VS")
    if marker != -1:
        a = subj[0:marker-1]
        return a
    
def right(subj):
    marker = subj.find("VS")
    if marker != -1:
        b = subj[marker+3:len(subj)]
        return b

df['teamA'] = df.Subject.apply(left)
df['teamB'] = df.Subject.map(right)
df['AWin'] = [2,2,2,2,2,2,0,0,2,0,1,0,2,2,2,2,2,0,2,2,2,0,2,0,2,2,2,2,2,2,2,2,0,2,0,2,2,0,2,2,0,0,3,3,3,3,3,3,4]
df['winner'] = df.teamA
df.winner[df.AWin == 0] = df.teamB

melted = pd.melt(df, id_vars = ['winner', 'Start Date'], value_vars = 'AWin', var_name = 'Owner', value_name = 'Pts')
melted.Pts[melted.Pts == 0] = 2

tie = pd.Series(['Bangladesh', '21/02/2015', 'AWin', 1], index = ['winner', 'Start Date', 'Owner', 'Pts'])
last = pd.DataFrame({
                    'winner': ['Australia','New Zealand','India','South Africa'],
                    'Start Date': ['29/03/2015']*4,
                    'Owner': ['Ashley', 'David', 'Jeff', 'Raghav'],
                    'Pts': [0]*4})

melted2 = melted.append(tie, ignore_index = True)
melted2 = melted2.append(last, ignore_index = True)
melted2.winner.loc[42:48] = ['South Africa', 'Australia', 'India', 'New Zealand', 'New Zealand', 'Australia', 'Australia']

participants = {
                'Australia' : 'Ashley',
                'India': 'Jeff',
                'South Africa' : 'Raghav',
                'New Zealand' : 'David',
                'Pakistan' : 'David',
                'England' : 'Raghav',
                'Sri Lanka' : 'Jeff',
                'West Indies' : 'Ashley',
                'Ireland' : 'Ashley',
                'Bangladesh' : 'Jeff',
                'Scotland' : 'Raghav',
                'Zimbabwe' : 'David',
                'Afghanistan' : 'David',
                'UAE' : 'Raghav'
                }

melted2['Owner'] = melted2.winner.map(participants)

import datetime as dt

dt_list = []
dtstr_list = []
for i, j in melted2['Start Date'].iteritems():
    dtl = dt.datetime.strptime(j, '%d/%m/%Y')
    dts = dt.datetime.strftime(dtl, '%m/%d/%Y')
    dtstr_list.append(dts)
    
    begin = dt.datetime(2015, 2, 14)
    diff = dtl - begin
    dt_list.append(diff.days)
    

melted2['start_date'] = dtstr_list
melted2['day_num'] = dt_list

melted2.sort('day_num')
df3 = melted2.groupby(['Owner', 'day_num', 'start_date']).sum() # need to cumsum by Owner, maybe MultiIndex can help
df3.to_csv('munged.csv') # continued in R