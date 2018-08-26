
HR_BP_High(X) :- \+HR_BP_Low(X).
Body_Temp_High(X) :- \+Body_Temp_Low(X).
Pupils_Dilated(X) :- \+Pupils_Contracted(X).

Anticholinergic(X) :- HR_BP_High(X), Body_Temp_High(X), Pupils_Dilated(X).
Opiod(X) :- HR_BP_Low(X), Body_Temp_Low(X), Pupils_Contracted(X).
