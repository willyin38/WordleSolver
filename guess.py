
lines = []
with open('wordlist.txt') as f:
    lines = [line.rstrip() for line in f]




def guess(word):

    guesses = 0
    guess = ""
    first_word = "stare"
    letter_values = {a:979/27, b:281/27, c:477/27, d:393/27, e:1233/27, f:230/27, g:311/27, h:389/27, i:671/27, j:27/27, k:210/27, l:719/27, m:316/27, n:575/27, o:754/27, p:367/27, q:29/27, r:899/27, s:669/27, t:729/27, u:467/27, v:153/27, w:195/27, x:37/27, y:425/27, z:40/27}
    letter_count = {}
    weight = 0
    wordlist = lines[:]
    max_score = 0
    score = 0
    copy = wordlist.copy()
    nth_word = 0

    for x in range(5):
        
        if word[x] == first_word[x]:

            for i in range(len(copy)):
                if len(copy[i]) == 5 and first_word[x] != copy[i][x]:
                    wordlist.remove(copy[i])
        
        elif first_word[x] in word:
            
            for i in range(len(copy)):
                if len(copy[i]) == 5 and first_word[x] == copy[i][x]:
                    wordlist.remove(copy[i])
                
            for i in range(len(copy)):
                if len(copy[i]) == 5 and first_word[x] not in copy[i]:
                    wordlist.remove(copy[i])
        
        else:

            for i in range(len(copy)):
                if len(copy[i]) == 5 and first_word[x] in copy[i]:
                    wordlist.remove(copy[i])
    guesses += 1
    for x in wordlist:
        for i in x:
            letter_count[i] = 1 + letter_count.get(i, 0)
        
    for x in wordlist:
        score = 0

        for i in range(len(x)):

            score += letter_values[x[i]]
            
            if x.count(x[i]) == 1:
                score += 750
                
            if x[i] != x[i-1]:
                score += letter_count[x[i]]
    if score > max_score:
        guess = x
    max_score = max(max_score, score)
    copy = wordlist.copy()
    letter_count = {}

    while guess != word: 
        nth_word = guess

        for x in range(5):
        
            if word[x] == first_word[x]:

                for i in range(len(copy)):
                    if len(copy[i]) == 5 and first_word[x] != copy[i][x]:
                        wordlist.remove(copy[i])
            
            elif first_word[x] in word:
                
                for i in range(len(copy)):
                    if len(copy[i]) == 5 and first_word[x] == copy[i][x]:
                        wordlist.remove(copy[i])
                    
                for i in range(len(copy)):
                    if len(copy[i]) == 5 and first_word[x] not in copy[i]:
                        wordlist.remove(copy[i])
            
            else:

                for i in range(len(copy)):
                    if len(copy[i]) == 5 and first_word[x] in copy[i]:
                        wordlist.remove(copy[i])
            












