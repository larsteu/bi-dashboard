import dash_bootstrap_components as dbc
import dash_uploader

from dash import dcc, html


def header() -> html.Header:
    """
    Returns
    -------
    html.Header which describes the header of the Feature Usage Tab
    """

    head = html.Header(
        [
            html.Div(
                [
                    html.Button(
                        [
                            html.Img(
                                src="assets/settings-icon.svg",
                                height="43px",
                                className="settings-icon",
                            ),
                            "Settings",
                        ],
                        className="button",
                        id="open-settings-button",
                    )
                ],
                className="col-2",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            dash_uploader.Upload(
                                text="Upload Report",
                                id="dash-uploader",
                                filetypes=["csv"],
                            )
                        ]
                    ),
                    dbc.Modal(
                        [
                            dbc.ModalHeader(
                                dbc.ModalTitle("Please enter a file identifier")
                            ),
                            dbc.ModalBody(
                                dbc.Input(
                                    id="ident",
                                    placeholder="identifier",
                                    type="text",
                                    debounce=True,
                                    className="input",
                                )
                            ),
                            dbc.ModalFooter(
                                html.Button("Confirm", id="confirm", className="button")
                            ),
                        ],
                        id="modal_ident",
                        is_open=False,
                    ),
                ],
                className="col-2 center",
            ),
            html.Div(
                [
                    "Time interval: ",
                    dcc.DatePickerRange(
                        id="select-date",
                        month_format="M-D-Y-Q",
                        start_date_placeholder_text="Start",
                        end_date_placeholder_text="Ende",
                    ),
                ],
                className="time",
            ),
            html.Div(
                [
                    html.Button("Export", id="export", className="button"),
                    dcc.Download(id="exportFunc"),
                ],
                className="col-2 center",
            ),
            html.Div(
                [
                    html.Img(
                        src="assets/threedy_logo.svg",
                        height="43 px",
                        width="auto",
                        style={"verticalAlign": "top"},
                    )
                ],
                className="col-2 logo",
            ),
        ],
        className="header",
        id="header",
    )

    return head


dropdown_list = [
    "Token Consumption",
    "Concurrent Active Sessions",
    "Product Usage",
    "Cluster-ID Comparison",
    "File Comparison",
]


def body_feature():
    """
    Returns
    -------
    html.Div which represents the html body of the dashboard tab Feature Usage Frontend
    """

    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [],
                        className="left-column",
                    ),
                    html.Div(  # content: graphs + data
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dcc.Dropdown(
                                            dropdown_list,
                                            "Token Consumption",
                                            id="dropdown1",
                                            className="dropdown",
                                            clearable=False,
                                        )
                                    ),
                                    dbc.Col(
                                        dcc.Dropdown(
                                            dropdown_list,
                                            "Concurrent Active Sessions",
                                            id="dropdown2",
                                            className="dropdown",
                                            clearable=False,
                                        )
                                    ),
                                ]
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(html.Div(id="graph1", className="graph")),
                                    dbc.Col(html.Div(id="graph2", className="graph")),
                                ]
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        html.Div(
                                            id="graph_data1",
                                            className="graph_data",
                                        )
                                    ),
                                    dbc.Col(
                                        html.Div(
                                            id="graph_data2",
                                            className="graph_data",
                                        )
                                    ),
                                ],
                            ),
                        ],
                        className="content",
                        id="content",
                    ),
                    html.Div(  # info content on the right side: file data
                        [
                            html.Div("File Statistics:", className="text"),
                            dbc.Table(id="file-data-table", className="info-table"),
                            html.Td(),
                            html.Div("Select a File:", className="text"),
                            dcc.Dropdown(
                                [],
                                "",
                                id="file-select",
                                className="dropdown_small",
                                clearable=False,
                            ),
                            html.Div("Select a Cluster-ID:", className="text"),
                            dcc.Dropdown(
                                [],
                                "",
                                id="cluster_id-select",
                                className="dropdown_small",
                                clearable=False,
                            ),
                        ],
                        id="info-column",
                        className="info-column",
                    ),
                ],
                id="main",
                className="main",
            ),
        ]
    )


def tab_layout():
    """
    Returns
    -------
    html.Div which represents the html body of the complete dashboard Frontend
    """

    return html.Div(
        [
            header(),
            dcc.Tabs(
                [
                    dcc.Tab(
                        label="Feature Usage",
                        children=[body_feature()],
                        className="tab-right",
                        id="tab1",
                    ),
                    dcc.Tab(
                        label="License Usage",
                        children=[body_license()],
                        className="tab-left",
                        id="tab2",
                    ),
                ],
                id="tabs",
            ),
            pop_up_messages(),
            stores(),
        ]
    )


def body_license():
    """
    Returns
    -------
    html.Div which represents the html body of the dashboard tab License Usage Frontend
    """
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(html.Div([""], id="graph_data3", className="graph_data")),
                ]
            ),
            dcc.Store(id="filename_license", data=""),
        ]
    )


def pop_up_messages():
    """
    Returns
    -------
    html.Div which represents the html format of the pop up messages
    """
    return html.Div(
        [
            html.Div(
                [
                    html.H1(
                        "~",
                        id="progress_bar_header",
                        className="center",
                        style={"marginBottom": "3%"},
                    ),
                    html.P(
                        "~",
                        id="progress_message",
                        className="info-text",
                    ),
                    dbc.Progress(
                        id="progress_bar",
                        striped=True,
                        color="#2817e8",
                        animated=True,
                    ),
                ],
                className="progress-div",
                id="progress_div",
            ),
            html.Div(
                html.Div("Database reset completed"),
                id="reset_msg",
                className="reset_msg",
            ),
            settings(),
        ]
    )


def stores():
    return html.Div(
        [
            dcc.Store(id="filename", data=""),
        ]
    )


def settings():
    return html.Div(  # https://plotly.com/python/custom-buttons/
        [
            html.H1(["Settings"], className="settings-h1"),
            dbc.Table(
                [
                    html.Tbody(
                        [
                            html.Tr(
                                [
                                    html.Td(
                                        html.H2("Graphs", className="text"),
                                        className="settings-table-cell",
                                    ),
                                ],
                            ),
                            html.Tr(
                                [
                                    html.Td(
                                        ["Graph Style:"],
                                        className="settings-table-cell",
                                    ),
                                    html.Td(
                                        [
                                            dcc.Dropdown(
                                                ["automatic", "bar", "line"],
                                                "automatic",
                                                id="graph-type",
                                                className="settings-dropdown",
                                                clearable=False,
                                            )
                                        ],
                                        className="settings-table-cell",
                                    ),
                                ],
                            ),
                            html.Tr(
                                [
                                    html.Td(
                                        html.H2("Database", className="text"),
                                        className="settings-table-cell",
                                    ),
                                ],
                            ),
                            html.Tr(
                                [
                                    html.Td(
                                        ["Reset:"],
                                        className="settings-table-cell",
                                    ),
                                    html.Td(
                                        [
                                            html.Button(
                                                "Reset", id="reset", className="button"
                                            )
                                        ],
                                        className="settings-table-cell",
                                    ),
                                ],
                            ),
                        ]
                    )
                ],
                className="settings-table",
            ),
            html.Button(
                ["Close Settings"],
                id="close-settings-button",
                className="close-settings-button",
            ),
        ],
        className="settings-div",
        id="settings-div",
    )
