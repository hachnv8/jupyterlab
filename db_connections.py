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
    if name == "atv400":
        # Hardcode trực tiếp cho hệ thống atv400
        conn_str = (
            f"DRIVER={{{DRIVER_NAME}}};"
            "SYSTEM=10.201.6.11;"
            "UID=MESDBA;"
            "PWD=mesdba102;"
            "Prompt=0;"
            "SIGNON=4;"
            "Naming=1;"
            "DefaultLibraries=EMLIB;"
            "ForceTranslate=1;"
        )
    elif name == "atv401":
        # Hardcode trực tiếp cho hệ thống atv401
        conn_str = (
            f"DRIVER={{{DRIVER_NAME}}};"
            "SYSTEM=10.201.6.21;"
            "UID=MESPGMR;"
            "PWD=GLORYAH;"
            "Prompt=0;"
            "SIGNON=4;"
            "Naming=1;"
            "DefaultLibraries=EMLIB;"
            "ForceTranslate=1;"
        )
    else:
        raise ValueError(f"Unknown connection: {name}")

    conn = pyodbc.connect(conn_str)
    print(f"Connected to {name} (Hardcoded) ✅")
    return conn
