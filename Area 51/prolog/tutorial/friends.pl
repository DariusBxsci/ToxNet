
likes(wallace, cheese).
likes(grommit, cheese).
likes(wendolene, sheep).
friend(X, Y) :- \+(X = Y), likes(X, Z), likes(Y, Z).



%% %Need this if building from within Sublime Text
%% main :- likes(wallace,sheep),
%% 		writef('%t\n',[X]).
