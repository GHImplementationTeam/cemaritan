# functions for actually making the database calls
from typing import Any, List, Tuple

from models import Connection, DataMapping, Organization, Transfer, User


def get_rows_by_organization(
    table_name: str, connection, organization_id: int
) -> List[List[Tuple[str, Any]]]:
    """Returns list of tuples where each tuple is a row in the database
    
    Parameters
    ----------
    table_name : 
        Name of table in DB
    connection
        Connection to DB
    organization_id
        Id of Organization
    
    Returns
    -------
    List[Tuple[str, Any]]
        List of 2-tuples representing each row of the response of the query
        Example: 
        [
            [
                ("uid", 1),
                ("organization", 1),
                ("name", "SF"),
                ("createddate", "2019-03-09 20:42:03"),
                ("createdby", 1),
                ("type", "A"),
                ("connectioninfo", "{conn string}")
            ],
            [
                ("uid", 2),
                ("organization", 1),
                ("name", "CW"),
                ("createddate", "2019-03-10 04:42:03"),
                ("createdby", 1),
                ("type", "B"),
                ("connectioninfo", "{conn string}")
            ]
        ]

    """
    query = f"select * from {table_name} where {table_name}.organization = (select organization from users where users.UID = {organization_id})"
    r = connection.query(query)
    return r


def delete_row_by_uid(connection, table_name: str, uid: int):
    """Delete row in ``table_name`` by ``uid``
    
    Parameters
    ----------
    connection
        Connection to database
    table_name : str
        Name of table
    uid : int
        UID of row to delete
    
    Returns
    -------
    bool
        Indicating success or failure of deletion
    """

    try:
        query = f"DELETE from {table_name} where {table_name}.UID={uid}"
        connection.query(query)
    except:
        return False
    return True


def get_connections(connection, organization_id: int):
    """Get connections for ``organization_id``
    
    Parameters
    ----------
    connection
        Connection to database
    organization_id : int
        Organization Id
    
    Returns
    -------
    List[models.Connection]
        List of Connection objects

    """

    orgs = get_rows_by_organization(
        table_name="connections", connection=connection, organization_id=organization_id
    )
    return [Connection(tup) for tup in orgs]


def get_histories(connection, organization_id: int):
    """Get histories for ``organization_id``
    
    Parameters
    ----------
    connection
        Connection to database
    organization_id : int
        Organization Id
    
    Returns
    -------
    List[models.History]
        List of History objects

    """

    orgs = get_rows_by_organization(
        table_name="history", connection=connection, organization_id=organization_id
    )
    return [Connection(tup) for tup in orgs]


def get_transfers(connection, organization_id: int):
    """Get transfers for ``organization_id``
    
    Parameters
    ----------
    connection
        Connection to database
    organization_id : int
        Organization Id
    
    Returns
    -------
    List[models.Transfer]
        List of Transfer objects

    """
    transfers = get_rows_by_organization(
        table_name="transfers", connection=connection, organization_id=organization_id
    )
    return [Transfer(tup) for tup in transfers]


def get_users(connection, organization_id: int):
    """Get users for ``organization_id``
    
    Parameters
    ----------
    connection
        Connection to database
    organization_id : int
        Organization Id
    
    Returns
    -------
    List[models.User]
        List of User objects

    """
    users = get_rows_by_organization(
        table_name="users", connection=connection, organization_id=organization_id
    )
    return [User(tup) for tup in users]


def get_data_mappings(connection, organization_id: int):
    """Get data mappings for ``organization_id``
    
    Parameters
    ----------
    connection
        Connection to database
    organization_id : int
        Organization Id
    
    Returns
    -------
    List[models.DataMapping]
        List of DataMapping objects

    """
    data_mappings = get_rows_by_organization(
        table_name="datamappings",
        connection=connection,
        organization_id=organization_id,
    )
    return [DataMapping(tup) for tup in data_mappings]


def get_organization(connection, organization_id: int):
    """Get organization with ``organization_id``
    
    Parameters
    ----------
    connection
        Connection to database
    organization_id : int
        Organization Id
    
    Returns
    -------
    models.Organization
        Organization object

    """
    query = f"select * from organizations where organizations.uid = '{organization_id}'"
    rows = connection.query(query)
    org = rows[0]  # should be only one org
    return Organization(org)


def get_organizations(connection):
    """Get all organizations
    
    Parameters
    ----------
    connection
        Connection to database
    organization_id : int
        Organization Id
    
    Returns
    -------
    List[models.Organization]
        List of Organization objects

    """
    query = f"select * from organizations"
    rows = connection.query(query)
    return [Organization(tup) for tup in rows]


def create_organization(connection, name: str, created_date: str):
    """Create organization in database
    
    Parameters
    ----------
    connection
        Connection to database
    name : str
        Name of database
    created_date : str
        Date created

    """
    query = f"INSERT INTO Organizations (Name, CreatedDate) VALUES ('{name}', '{created_date}')"
    connection.query(query)


def create_data_mapping(connection, user_id: int, name: str, mapping_info: str):
    """Create data mapping in database
    
    Parameters
    ----------
    connection
        Connection to database
    name : str
        Name of database
    created_date : str
        Date created

    """
    query = f"INSERT INTO DataMappings (Organization, Name, MappingInfo) VALUES ((select Organization from Users where Users.UID = {user_id}), '{name}', '{mapping_info}');"
    connection.query(query)


def create_connection(
    connection,
    user_id: int,
    name: str,
    created_date: str,
    created_by: int,
    connection_type: str,
    connection_info: str,
):
    """Create connection in database
        
        Parameters
        ----------
        connection
            Connection to database
        name : str
            Name of database
        created_date : str
            Date created

        """
    query = f"INSERT INTO Connections (Organization, Name, CreatedDate, CreatedBy, Type, ConnectionInfo) VALUES ((select Organization from Users where Users.UID = {user_id}), '{name}', '{created_date}', '{created_by}', '{connection_type}', '{connection_info}');"
    connection.query(query)


def create_user(connection, organization_id: int, name: str, created_date: str):
    """Create user in database
    
    Parameters
    ----------
    connection
        Connection to database
    organization_id : int
        Organization to crete user in
    name : str
        Name of user
    created_date : str
        Date Created
    
    """

    query = f"INSERT INTO Users (Organization, Name, CreatedDate) VALUES ('{organization_id}', '{name}', '{created_date}');"
    connection.query(query)


def create_transfer(
    connection,
    user_id: int,
    name: str,
    created_date: str,
    created_by: int,
    organization_id: int,
    source: int,
    source_mapping: int,
    destination: int,
    destination_mapping: int,
    start_date_time: str,
    frequency: str,
    record_filter: str,
    active: bool,
):
    """Create transfer in database
    
    Parameters
    ----------
    connection
        Connection to database
    user_id : int
        User creating transfer
    name : str
        Name of transfer
    created_date : str
        Date transfer was created 
    created_by : int
        User creating transfer
    organization_id : int
        Organization user belongs to
    source : int
        Id of Connection source
    source_mapping : int
        Mapping of source system
    destination : int
        Id of destination Connection
    destination_mapping : int
        Mapping of destination system
    start_date_time : str
        Date to start transfer
    frequency : str
        Frequency of transfer
    record_filter : str
        Filter records parameters
    active : bool
        Is connection currently active
    
    """

    query = f"INSERT INTO Transfers (Organization, Name, CreatedDate, CreatedBy, Source, SourceMapping, Destination, DestinationMapping, StartDateTime, Frequency, RecordFilter, Active) VALUES ((select Organization from Users where Users.UID = {user_id}), '{name}', '{created_date}', '{created_by}', '{source}', '{source_mapping}', '{destination}', '{destination_mapping}', '{start_date_time}', '{frequency}', '{record_filter}', '{active}');"
    connection.query(query)


def delete_user(connection, user_id: int):
    """Delete user with ``user_id`` in database
    
    Parameters
    ----------
    connection
        Connection to database
    user_id : int
        Id of user
    
    """
    return delete_row_by_uid(connection, "Users", user_id)


def delete_organization(connection, organization_id: int):
    """Delete organization with ``organization_id`` in database
    
    Parameters
    ----------
    connection
        Connection to database
    organization_id : int
        Id of organization
    
    """
    return delete_row_by_uid(connection, "Organizations", organization_id)


def delete_data_mapping(connection, data_mapping_id: int):
    """Delete data_mapping with ``data_mapping_id`` in database
    
    Parameters
    ----------
    connection
        Connection to database
    data_mapping_id : int
        Id of data_mapping
    
    """
    return delete_row_by_uid(connection, "DataMappings", data_mapping_id)


def delete_connection(connection, connection_id: int):
    """Delete connection with ``connection_id`` in database
    
    Parameters
    ----------
    connection
        Connection to database
    connection_id : int
        Id of connection
    
    """
    return delete_row_by_uid(connection, "Connections", connection_id)


def delete_transfer(connection, transfer_id: int):
    """Delete transfer with ``transfer_id`` in database
    
    Parameters
    ----------
    connection
        Connection to database
    transfer_id : int
        Id of transfer
    
    """
    return delete_row_by_uid(connection, "Transfers", transfer_id)