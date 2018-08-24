


has_sympathomimetic_syndrome(patient) :- has_sign(patient,tachycardia),
										 has_sign(patient,mydriasis),
										 has_sign(patient,absent_bowel_sounds),
										 has_sign(patient,agitation).