from v1.templates import BaseTemplate

import genanki

"""
    This contains the following templates:
        - ImmersiveTemplate
"""

### For easy reading, search in this
### file the routine that you want
### with ctrl+f (or somenthing like)

class ImmersiveTemplate(BaseTemplate):
    def __init__(self, css=None, card_header=None):
        super().__init__(css, card_header)

        self.name = "Immersive template"
        self.input_required_fields = [
            'phrase', 'translation',
            'meaning', 'header', 'css'
        ]
        self.output_front_fields = ['audio', 'audio2', 'audio3', 'input']
        self.output_back_fields = ['audio', 'audio2', 'audio3', 'input', 'translation', 'meaning']
        self.default_template['qfmt'] = """
            {{audio}}
            {{audio2}}
            {{audio3}}
            {{type:input}}
        """
        self.default_template['afmt'] = """
            {{audio}}
            {{audio2}}
            {{audio3}}
            <hr id=answer>
            {{type:input}}
            <br>
            <h3>Traducao</h3>
            <div style='font-family: Arial; font-size: 20px;'>{{translation}}</div>
            <br>
            <h3>Significado</h3>
            <div style='font-family: Arial; font-size: 20px;'>{{meaning}}</div>
        """
