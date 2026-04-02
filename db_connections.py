import pyodbc

CONNECTIONS = {
    "atv400": {
        "system": "10.201.6.11",
        "user": "MESDBA",
        "password": "mesdba102",
        
        # nếu cần chỉ định library mặc định thì mở dòng dưới
        # "default_library": "PRODLIB",
    },
    "atv401": {
        "system": "10.201.6.21",
        "user": "MESPGMR",
        "password": "GLORYAH",
        # "default_library": "PRODLIB",
    },
}

DRIVER_NAME = "iSeries Access ODBC Driver"


def get_connection(name: str):
    if name not in CONNECTIONS:
        raise ValueError(f"Unknown connection: {name}")

    cfg = CONNECTIONS[name]

    conn_str = (
        f"DRIVER={{{DRIVER_NAME}}};"
        f"SYSTEM={cfg['system']};"
        f"UID={cfg['user']};"
        f"PWD={cfg['password']};"
        "Prompt=0;"
        "Naming=1;"
        "DefaultLibraries=EMLIB;"
        "ForceTranslate=1;"

    )

    # nếu muốn dùng default library
    if "default_library" in cfg:
        conn_str += f"DefaultLibraries={cfg['default_library']};"

    conn = pyodbc.connect(conn_str)

    print(f"Connected to {name} ✅")
    return conn
