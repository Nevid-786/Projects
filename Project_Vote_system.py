#lets take the votes are
from collections import Counter
votes = ['Alice', 'Bob', 'Alice', 'Alice', 'Bob', 'Charlie']
Votes_count=Counter(votes)
Highest_votes=Votes_count.most_common(1)    #[('Alice', 3)] returned a list of tupple now to acces only alice 
print(f'Winner:{Highest_votes[0][0]}')                        #first access the first element in list Highest_Votes then alice in tupple