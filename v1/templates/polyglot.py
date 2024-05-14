v1.templates import BaseTemplate

import genanki

"""
    This contains the following templates:
        - ImmersiveTemplate
"""

### For easy reading, search in this file
### the template that you want like ctrl+f 

class ImmersiveTemplate(BaseTemplate):
    def __init__(self,):
        self.name = "Immersive template"
        self.fields = [
            {'name': 'Audio'},
            {'name': 'Audio2'},
            {'name': 'Audio3'},
            {'name': 'Verso'},
            {'name': 'Tradução'},
            {'name': 'Significado'},
        ]
        self.default_template = {
            'qfmt': """
                {{Audio}}
                {{Audio2}}
                {{Audio3}}
                {{type:Verso}}
            """,
            'afmt': self.card_header + """
                {{Audio}}
                {{Audio2}}
                {{Audio3}}
                <hr id=answer>
                {{type:Verso}}
                <br>
                <div style='font-family: Arial; font-size: 20px;'>{{Tradução}}</div>
                <br>
                <div style='font-family: Arial; font-size: 20px;'>{{Significado}}</div>
            """,
        }
    
