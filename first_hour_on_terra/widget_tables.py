def users_table(x):
    """ Create table with data in a multiline
    string as first argument x)"""
    html = f"<table>"
    for line in x.splitlines():
        for n in line.split():
            if n == 'EMAIL' or n == 'POLICIES':
                html += f"<th>{n}</th>"
            else:
                html += f"<td>{n}</td>"
        html += "<tr>"
    html += "</table>"
    # print("CREATE USERS TABLE:\n{}".format(html))
    return html

def list_workspaces(x):
    """ Create table with data in a multiline
    string as first argument x)"""
    html = f"<table>"
    for line in x.splitlines():
        for n in line.split():
            if n == 'EMAIL' or n == 'POLICIES':
                html += f"<th>{n}</th>"
            else:
                html += f"<td>{n}</td>"
        html += "<tr>"
    html += "</table>"
    # print("CREATE USERS TABLE:\n{}".format(html))
    return html