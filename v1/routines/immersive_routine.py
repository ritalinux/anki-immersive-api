from v1.templates.polyglot import ImmersiveTemplate
import v1.utils import get_randon_id

import requests
import genanki
import pytube
import re

class ImmersiveRoutine:
    def __init__(self, deck_name, file_output, prhase):
        self.deck = genanki.Deck(
            get_randon_id(),
            deck_name
        )
        self.file_output = file_output
        self.prhase = prhase
        self.medias = []

    def get_yt_ids(self, prhase):
        resp = requests.get("")
    
    def run(self):
        model = ImmersiveTemplate()

        
        note = genanki.Note(
            model=model.make_template(),
            fields=[
                f'[sound:{}.mp3]',
                f'[sound:{}.mp3]',
                f'[sound:{}.mp3]',
                'oioioi',
                '',
                ''
            ]
        )

        self.deck.add_note(note)

        package = genanki.Package(self.deck)

        if self.medias:
            package.media_files = self.medias
        
        package.write_to_file(f'{self.file_output}.apkg')

