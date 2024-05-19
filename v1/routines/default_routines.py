from v1.templates.default import BasicTypeTemplate
from v1.utils import get_randon_id

import genanki
"""
    This contains the following Routines:
        - BasicTypeRoutine
"""

### For easy reading, search in this
### file the routine that you want
### with ctrl+f (or somenthing like)

class BasicTypeRoutine:
    def __init__(self):
        self.template = BasicTypeTemplate()
    
    async def run(self, file):

        if sorted(file['content'].columns) != sorted(self.template.input_required_fields):
            raise FileFormatError(f"Invalid columns format in {file['name']}")

        deck = genanki.Deck(
            get_randon_id(),
            file['name']
        )

        medias = []
        model = self.template.make_template()
        for row in file['content'].to_dicts():
            note = genanki.Note(
                model=model,
                fields=[
                    row['front'],
                    row['back']
                ]
            )

            deck.add_note(note)

        package = genanki.Package(deck_or_decks=deck, media_files=media)

        package.write_to_file(f"{file['name']}.apkg")


