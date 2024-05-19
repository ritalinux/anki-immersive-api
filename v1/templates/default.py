from v1.templates import BaseTemplate

"""
    This contains the following templates:
        - BasicTypeTemplate
"""

### For easy reading, search in this
### file the routine that you want
### with ctrl+f (or somenthing like)

class BasicTypeTemplate(BaseTemplate):
    def __new__(cls):
        self = super().__new__(cls)

        self.name = "Basic type template"
        self.input_required_fields = ['front', 'back']
        self.output_front_fields = ['front', 'back']
        self.output_back_fields = ['front', 'back']
        self.default_template['qfmt'] = """
            {{front}}
            {{type:back}}
        """
        self.default_template['afmt'] = """
            {{front}}
            <hr id=answer>
            {{type:back}}
        """
        return self