import genanki
import utils

class ImmersiveTemplate:
    def __init__(self, css=None, custom_header=None):
        self.name = "Immersive template"
        self.card_header = custom_header or ""
        self.css = css or """
            .card {
                font-family: arial;
                font-size: 20px;
                text-align: center;
                color: black;
                background-color: white;
            }
        """
        self.fields = [
            {'name': 'Audio'},
            {'name': 'Audio2'},
            {'name': 'Audio3'},
            {'name': 'Verso'},
            {'name': 'Tradução'},
            {'name': 'Significado'},
        ]
        self.default_template = {
            'name': 'Card 1',
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
    
    def make_template(self):
        return genanki.Model(
            utils.get_randon_id(),
            self.name,
            css=self.css,
            fields=self.fields,
            templates=[self.default_template]
        )