# anki-chatgpt

Generate a csv file that you can use to import into Anki to create flashcards for learning Spanish.

This script uses OpenAI to generate translations. When it encounters a verb infinitive it will automatically translate it into roughly 53 conjugations corresponding to all of the following tenses (see `prompts.py`): `present, preterite, imperfect, future, conditional, present perfect, past perfect, future perfect, conditional perfect, present subjunctive, imperfect subjunctive, present perfect subjunctive, and past perfect subunctive. For each tense, create a separate row for first person singular (I), second person singular (you), first person plural (we), and third person plural (they). For the preterite tense, also include the third person singular (he/she).`

## Usage

First clone the project
```
git clone https://github.com/kharmabum/anki-chatgpt
cd anki-chatgpt
```

Then create a virtual environment and install the dependencies
```
python3 -m venv myenv
source ./myenv/bin/activate
pip install -r requirements.txt
```

Then add an `input.txt` file with the text you want to translate (see `test_input.txt` for an example):
```
touch input.txt 
# add your spanish text to input.txt
```

Get an API key from OpenAPI (ask for me help if you need it), then run the script
```
OPENAI_API_KEY={YOUR_KEY} python3 main.py
```

This will create a `output.csv` file that you can import into Anki.

## Notes 

- Either set the default value of OPENAI_TEST_RUN to False in the code or set it manually before calling the script. If you set it to True, the script will only run on the first 100 characters of the input file. This determines whether or not `input.txt` or `test_input.txt` is read from.
- You don't need to deduplicate your `input.txt`, the script handles that for you (it will also sort the input and rewrite it to the file).