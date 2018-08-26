likes(wallace, cheese).
likes(grommit, cheese).
likes(wendolene, sheep).
hates(wendolene, cheese).

friend(X, Y) :- \+(X = Y), likes(X, Z), likes(Y, Z).
enemy(X, Y) :- \+(X = Y), hates(X, Z), likes(Y, Z).
