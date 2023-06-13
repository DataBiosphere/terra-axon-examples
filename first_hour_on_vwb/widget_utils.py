from google.cloud import bigquery
import json
import ipywidgets as widgets
from dataclasses import dataclass, field
from typing import List

input_style = {
    'description_width': 'initial'
}

input_layout = widgets.Layout(
    width='75%',
    align_items='flex-start'
)

output_style = {
    'description_width': 'initial',
}

vbox_layout = widgets.Layout(
    border='solid 2px',
    padding='10px',
    display='flex',
    flex_flow='column',
    align_items='flex-start',
    width='75%'
)

def list_groups(json_string):
    """ List VWB groups in which user is a member in HTML table form.
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

def list_group_members(json_string):
    """ List members of a VWB group in HTML table form.
    """
    html = f"""<table style='margin: 0 auto,text-align: left'>"""
    json_data = json.loads(json_string)
    html += "<th>EMAIL</th>"
    html += "<th>POLICIES</th>"
    for row in json_data:
        html += "<tr>"
        html += f"<td>{row['email']}</td>"
        html += f"<td>{row['policies'][0]}</td>"
    html += "</table>"
    return html

def get_schema_html(schema_lst):
    """ Return an HTML table listing schema fields."""
    html = f"""<table style='margin: 0 auto,text-align: left'>"""
    html += "<th>NAME</th>"
    html += "<th>TYPE</th>"
    html += "<th>DESCRIPTION</th>"
    html += "<th>DEFAULT</th>"
    for s_field in schema_lst:
        html += "<tr>"
        html += f"<td>{s_field.name}</td>"
        html += f"<td>{s_field.field_type}</td>"        
        html += f"<td>{s_field.description}</td>"  
        html += f"<td>{s_field.default_value_expression}</td>"
        html += "</tr>"
    html += "</table>"
    return html

def get_tables_in_dataset(dataset_id):
    # Construct a BigQuery client object.
    client = bigquery.Client()
    tables = client.list_tables(dataset_id)
    print("Tables contained in '{}':".format(dataset_id))
    for table in tables:
        print("{}.{}.{}".format(table.project, table.dataset_id, table.table_id))
    return tables

def list_bq_tables(json_string):
    """ List BQ resources for current workspace.
    """
    bq_resource_names = []
    json_data = json.loads(json_string)
    for row in json_data:
        if row['resourceType'] == 'BQ_TABLE':
            bq_resource_names.append(row['name'])
    return bq_resource_names
        

@dataclass
class TextInputWidget:
    """A styled text widget with layout."""
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
        '''Return widget.'''
        return self.text_widget


@dataclass
class DropdownInputWidget:
    """A styled dropdown widget with layout.
    """
    options: List = field(default_factory=lambda: [])
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
        '''Return widget.'''
        return self.dropdown_widget


@dataclass
class StyledButton():
    """ A styled button widget with layout.
    """
    description: str
    tooltip: str
    icon: str
    button: widgets.Button = None

    def __post_init__(self):
        self.button = widgets.Button(
            description=self.description,
            disabled=False,
            layout=widgets.Layout(width='75%'),
            display='flex',
            align_items='stretch',
            button_style='',
            tooltip=self.tooltip,
            icon=self.icon,
            style=widgets.ButtonStyle(button_color='#D8D2EB')
        )

    def get(self):
        '''Return widget.'''
        return self.button


class ShowOptionalCheckbox():
    """ Creates a styled checkbox widget with description.
    """

    def __init__(self):
        self.checkbox = widgets.Checkbox(
            False,
            description="Show optional parameters",
            indent=False,
            style={'background': '#D8D2EB'}
        )

    def get(self):
        '''Return widget.'''
        return self.checkbox