# BigLittle

Algorithm to determine bigs and littles

1) Run thru frosh, if there exists a 1 to 1 relationship, match, and remove frosh from queue
    a) update the exisiting sophs pref lists, removing any frosh that were filled
2) Run thru frosh, if there exists a 1 to 2 relationship, match, and remove frosh from queue, 
    if a soph has 2 littles, remove them from queue
    a) update exisiting sophs pref lists, removing where any forsh were filled.
    b) update remaining frosh pref lists, removing any sophs that are filled
3) Run thru soph, if there exists 2 to 1 relationship, match, and remove frosh from queue,
    if a soph has 2 littles remove them from the queue
    a) update remaining sophs pref list, removing frosh who were filled.
    b) update remaing frosh pref list, removing sophs who were filled.
    
So on...
