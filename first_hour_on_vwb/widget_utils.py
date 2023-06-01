import json
import ipywidgets as widgets
from dataclasses import dataclass,field
from typing import List

input_style = {
    'description_width':'initial'
}

input_layout = widgets.Layout(
    width='75%',
    align_items='flex-start'
)

output_style = {
    'description_width':'initial',
}

vbox_layout = widgets.Layout(
    border='solid 2px',
    padding='10px',
    display='flex',
    flex_flow='column',
    align_items='flex-start',
    width='75%'
)

def users_table(json_string):
    """ Create HTML table from JSON string
    """
    html = f"""<table style='margin: 0 auto,text-align: left'>"""
    json_data = json.loads(json_string)
    html += "<th>NAME</th>"
    html += "<th>EMAIL</th>"
    html += "<th>MEMBERS</th>"
    html += "<th>POLICIES</th>"
    for row in json_data:
        html += "<tr>"
        html += f"<td>{row['name']}</td>"
        html += f"<td>{row['email']}</td>"
        html += f"<td>{row['numMembers']}</td>"
        html += f"<td>{row['currentUserPolicies'][0]}</td>"
    html += "</table>"
    return html

@dataclass
class TextInputWidget:
    placeholder: str
    description: str
    text_widget: widgets.Text = None

    def __post_init__(self):
        self.text_widget = widgets.Text(
            placeholder=self.placeholder,
            description=self.description,
            layout=input_layout,
            style=input_style
        )

    def get(self):
        return self.text_widget

@dataclass
class DropdownInputWidget:
    options: List = field(default_factory=lambda:[])
    value: str = ''
    description: str = ''
    dropdown_widget: widgets.Dropdown = None
        
    def __post_init__(self):
        self.dropdown_widget = widgets.Dropdown(
            options=self.options,
            value=self.value,
            disabled=False,
            description=self.description,
            layout=input_layout,
            style=input_style
        )

    def get(self):
        return self.dropdown_widget
    
@dataclass
class StyledButton():
    description: str
    tooltip: str
    icon: str
    button: widgets.Button = None
    
    def __post_init__(self):
        self.button = widgets.Button(
            description=self.description,
            disabled=False,
            layout = widgets.Layout(width='75%'),
            display='flex',
            align_items='stretch',
            button_style='',
            tooltip=self.tooltip,
            icon=self.icon,
            style=widgets.ButtonStyle(button_color = '#D8D2EB')
        )
    
    def get(self):
        return self.button