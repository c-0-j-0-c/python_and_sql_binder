from ipylab import JupyterFrontEnd,Panel
from ipywidgets import Output, Tab, HTML, Accordion, Text, IntSlider

def display_right_panel(app, tblInfo,tblAttr,ddl):
    right_panel = Panel()
    right_panel.title.label = "DB Info"
    
    

    tablesDsp = HTML("<pre>{0}</pre>".format("\n".join(tblInfo)))
    
    #accordion = Accordion(children=[IntSlider(),Text()], titles=('Slider', 'Text'))
#accordion

    text = " ".join(tblAttr)
    a_titles = [i.split("^")[0] for i in (text.split("&")[:-1])]
    content = [i.split("^")[1] for i in (text.split("&")[:-1])]

    a_children = [HTML("<pre>{0}</pre>".format(j)) for j in content]
    tblAttrDsp = Accordion(children = a_children, titles=a_titles)
    for i,txt in enumerate(a_titles):
        tblAttrDsp.set_title(i, txt)
    
    
    #tblAttrDsp= HTML((" ".join(tblAttr)))
    DDLDsp = HTML("<pre>{0}</pre>".format("\n".join(ddl)))
    out = [tablesDsp, tblAttrDsp, DDLDsp]

    tab_titles = ['Tables', 'All Table Attributes', 'DDL of Tables']
    tab = Tab()
    tab.children = out
    for i in range(len(tab.children)):
        tab.set_title(i, tab_titles[i])

    right_panel.children = [tab]
    app.shell.add(right_panel, 'main', { 'mode': 'split-right' })