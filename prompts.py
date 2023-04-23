
PROMPT = """
For the following list of Spanish phrases, perform the following actions:

1. Generate a CSV with the input text in column 1 and an English translation in column 2

While respecting the following constraints:

1. Wrap the contents of first and second columns in double quotes.
2. For any input text that contains only a verb infinitive, generate rows for conjugations in each of the following tenses: present, preterite, imperfect, future, conditional, present perfect, past perfect, future perfect, conditional perfect, present subjunctive, imperfect subjunctive, present perfect subjunctive, and past perfect subunctive. For each tense, create a separate row for first person singular (I), second person singular (you), first person plural (we), and third person plural (they). For the preterite tense, also include the third person singular (he/she).

For example, the input text “cantar” should generate all of the following rows:

“Canto”,“I sing”
“Cantas,“You sing”
“Cantamos”,“We sing”
“Cantan”,”They sing”
“Canté”,”I sang”
“Cantaste”,“You sang”
“Cantó”,“He/she sang”
“Cantamos”,“We sang”
“Cantaron”,”They sang”	
“Cataba”, “I used to sing”
“Cantabas”,”You used to sing”
“Cantábamos”,”We used to sing”
“Cantaban”,”They used to sing”
“Cantaré”,”I will sing”
“Cantarás,You will sing”
“Cantaremos”,”We will sing”
“Cantarán”,”They will sing”
“Cantaría”,”I would sing”
“Cantarías”,”You would sing”
“Cantaríamos”,”We would sing”
“Cantarían”,”They would sing”
“Cantarían”,”They would sing”
“He cantado”,”I have sung”
“Has cantado”,”You have sung”
“Hemos cantado”,”We have sung”
“Han cantado”,”They have sung”
“Había cantado”,”I had sung”
“Habías cantado”,”You had sung”
“Habíamos cantado”,”she had sung”
“Había cantado”,”I had sung”
“Habías cantado”,”You had sung”
“Habíamos cantado”,”We had sung”
“Habían cantado”,”They had sung”
“Habré cantado”,”I will have sung”
“Habrás cantado”,”You will have sung”
“Habremos cantado”,”We will have sung”
“Habrán cantado”,”They will have sung”
“Habría cantado”,”I would have sung”
“Habrías cantado”,”You would have sung”
“Habríamos cantado”,”We would have sung”
“Habrían cantado”,”They would have sung”
“Habrían cantado”,”They would have sung”
“Cante”,”I sing (subjunctive)”
“Cantes”,”You sing (subjunctive)”
“Cantemos”,”We sing (subjunctive)”
“Canten”,”They sing (subjunctive)”
“Cantara”,”I used to sing (subjunctive)”
“Cantaras”,”You used to sing (subjunctive)”
“Cantaramos”,”We used to sing (subjunctive)”
“Cantaran”, “They used to sing (subjunctive)”
“Haya cantado”, “I have sung (subjunctive)”
“Hayas cantado”, “You have sung (subjunctive)”
“Hayamos cantado”, “We have sung (subjunctive)”
“Hayan cantado”, “They have sung (subjunctive)”
“Huberia cantado”, “I had sung (subjunctive)”
“Huberias cantado”, “You had sung (subjunctive)”
“Huberias cantado”, “You had sung (subjunctive)”
“Huberiamos cantado”, “We had sung (subjunctive)”
“Huberian cantado”, “They had sung (subjunctive)”

While the input text "A finales de" should generate only the following row:

"A finales de", "At the end of"

Input list:

"""