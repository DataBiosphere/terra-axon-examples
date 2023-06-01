import json
import ipywidgets as widgets

input_style = {
    'description_width':'initial'
}

input_layout = widgets.Layout(
    width='50%',
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

def users_table(stdout):
    """ Create table from JSON string
    """
    html = f"""<table style='margin: 0 auto,text-align: left'>"""
    json_data = json.loads(stdout)
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

class TextInputWidget(object):
    def __init__(self, ph, desc):
        self.description = desc
        self.placeholder = ph
        self.widget = widgets.Text(
            placeholder=self.placeholder,
            description=self.description,
            layout=input_layout,
            style=input_style)

    def get(self):
        return self.widget


class DropdownInputWidget(object):
    def __init__(self, options, value, description):
        self.options = options
        self.value = value
        self.description = description
        self.widget = widgets.Dropdown(
            options=self.options,
            value=self.value,
            disabled=False,
            description=self.description,
            layout=input_layout,
            style=input_style
        )

    def get(self):
        return self.widget
    
class StyledButton(object):
    def __init__(self,desc,tooltip,icon):
        self.description = desc
        self.tooltip = tooltip
        self.icon = icon
        self.button = widgets.Button(
                description=self.description,
                disabled=False,
                layout = widgets.Layout(width='50%'),
                display='flex',
                align_items='stretch',
                button_style='',
                tooltip=self.tooltip,
                icon=self.icon,
                style=widgets.ButtonStyle(button_color = '#D8D2EB')
        )
    def get(self):
        return self.button