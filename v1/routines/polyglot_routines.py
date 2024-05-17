from v1.templates.polyglot import ImmersiveTemplate
from v1.utils import get_randon_id

import genanki
import pytube
import re

"""
    This contains the following Routines:
        - ImmersiveRoutine
"""

### For easy reading, search in this
### file the routine that you want
### with ctrl+f (or somenthing like)

class ImmersiveRoutine:
    def __init__(self):
        self.template = ImmersiveTemplate()
    
    async def run(self, file):

        if sorted(file['content'].columns) != sorted(self.template.input_required_fields):
            raise FileFormatError(f"Invalid columns format in {file['name']}")

        if file['content']['phrase'].null_count() > 0:
            raise FileFormatError(f"Phrase column can't have null values")

        deck = genanki.Deck(
            get_randon_id(),
            file['name']
        )

        medias = []
        model = self.template.make_template()
        for row in file['content'].to_dicts():
            audio_name = row['phrase'][:30]
            note = genanki.Note(
                model=model,
                fields=[
                    f'[sound:{audio_name}-1.mp3]',
                    f'[sound:{audio_name}-2.mp3]',
                    f'[sound:{audio_name}-3.mp3]',
                    row['phrase'],
                    row['translation'] or str(),
                    row['meaning'] or str()
                ]
            )

            deck.add_note(note)

        package = genanki.Package(deck)

        if medias:
            package.media_files = medias
        
        package.write_to_file(f"{file['name']}.apkg")


