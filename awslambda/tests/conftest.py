# cd /awslambda
# python -m pytest [-vv -s]

import json
import os
import pytest
from pathlib import Path

test_path = Path.cwd()

try:
    os.unlink(test_path.joinpath("api/models"))
except:
    pass
os.symlink(test_path.joinpath("models"), test_path.joinpath("api/models"))

try:
    os.unlink(test_path.joinpath("api/library"))
except:
    pass
os.symlink(test_path.joinpath("library"), test_path.joinpath("api/library"))

### Connections
@pytest.fixture()
def connections_event():
    return {"pathParameters": {"organization_id": "1"}}


@pytest.fixture()
def connection_single_event():
    return {"pathParameters": {"organization_id": "1", "connection_id": "1"}}


@pytest.fixture()
def sample_connections_response():
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": '[{"uid": 1, "organization": 1, "name": "SF", "created_datetime": "2019-03-09 20:42:03", "created_by": 1, "type": "A", "connection_info": "{conn string}"}, {"uid": 2, "organization": 1, "name": "CW", "created_datetime": "2019-03-10 04:42:03", "created_by": 1, "type": "B", "connection_info": "{conn string}"}, {"uid": 6, "organization": 1, "name": "Secure Download", "created_datetime": "2019-03-23 20:42:03", "created_by": 0, "type": "F", "connection_info": "0"}]',
    }


@pytest.fixture()
def sample_connection_single_response():
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": '{"uid": 1, "organization": 1, "name": "SF", "created_datetime": "2019-03-09 20:42:03", "created_by": 1, "type": "A", "connection_info": "{conn string}"}',
    }


@pytest.fixture()
def sample_connection_list():
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": '[{"uid": 1, "name": "SF"}, {"uid": 2, "name": "CW"}, {"uid": 6, "name": "Secure Download"}]'
    }


### Transfers
@pytest.fixture()
def transfers_event():
    return {"pathParameters": {"organization_id": "1"}}


@pytest.fixture()
def transfer_single_event():
    return {"pathParameters": {"organization_id": "1", "transfer_id": "1"}}


@pytest.fixture()
def sample_transfers_response():
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": '[{"uid": 1, "name": "CW to SF", "organization": "OLI", "created_datetime": "2019-03-20 20:42:03", "source": "CW", "source_mapping": "CW to HUD", "destination": "SF", "destination_mapping": "SF to HUD", "active": "TRUE", "start_datetime": "2019-03-13 20:42:03", "frequency": "1 day"}, {"uid": 2, "name": "SF to CW", "organization": "OLI", "created_datetime": "2019-03-13 20:42:03", "source": "SF", "source_mapping": "SF to HUD", "destination": "CW", "destination_mapping": "CW to HUD", "active": "FALSE", "start_datetime": "2019-03-13 20:42:03", "frequency": "1 hour"}]',
    }


@pytest.fixture()
def sample_transfer_single_response():
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": '{"uid": 1, "name": "CW to SF", "organization": "OLI", "created_datetime": "2019-03-20 20:42:03", "source": "CW", "source_mapping": "CW to HUD", "destination": "SF", "destination_mapping": "SF to HUD", "active": "TRUE", "start_datetime": "2019-03-13 20:42:03", "frequency": "1 day"}',
    }


@pytest.fixture()
def sample_transfer_single_create_event():
    return {
                "pathParameters": {"organization_id": "1"},
                "body": '{"name": "CW to SF", "organization": 10, "created_by": 1, "source": 2, "source_mapping": 2, "destination": 1, "destination_mapping": 1, "active": 1, "start_datetime": "2019-03-13 20:42:03", "frequency": "1 day"}'
            }


@pytest.fixture()
def sample_transfer_single_create_response():
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": '{"uid": 1}'
    }

@pytest.fixture()
def sample_frequencies_list_response():
    return {
        'statusCode': 200, 
        'headers': {'Access-Control-Allow-Origin': '*'}, 
        'body': '[{"name": "1 hour", "value": 1}, {"name": "1 day", "value": 2}]'
    }


### Histories
@pytest.fixture()
def histories_event():
    return {"pathParameters": {"organization_id": "1"}}


@pytest.fixture()
def history_single_event():
    return {"pathParameters": {"organization_id": "1", "history_id": "2"}}


@pytest.fixture()
def sample_histories_response():
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": '[{"uid": 2, "type": "Transfer", "action": null, "datetime": "2019-03-20 20:42:03", "name": null, "details": null, "source_uid": 0, "organization": 1}, {"uid": 3, "type": "Transfer", "action": null, "datetime": "2019-03-20 20:42:03", "createdbyuser": 1, "name": null, "details": null, "source_uid": 0, "organization": 1}, {"uid": 4, "type": "Transfer", "action": "Action B", "datetime": "2019-03-20 20:42:03", "createdbyuser": 1, "name": null, "details": null, "source_uid": 0, "organization": 1}]',
    }


@pytest.fixture()
def sample_history_single_response():
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": '{"uid": 2, "type": "Transfer", "action": null, "datetime": "2019-03-20 20:42:03", "name": null, "details": null, "source_uid": 0, "organization": 1}',
    }


### Mappings
@pytest.fixture()
def mappings_event():
    return {"pathParameters": {"organization_id": "1"}}


@pytest.fixture()
def mapping_single_event():
    return {"pathParameters": {"organization_id": "1", "mapping_id": "1"}}


@pytest.fixture()
def sample_mappings_response():
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": '[{"uid": 1, "organization": 1, "name": "SF to HUD", "mapping_info": "{}", "start_format": "csv", "end_format": "json", "num_of_transfers": 1}, {"uid": 2, "organization": 1, "name": "CW to HUD", "mapping_info": "{}", "start_format": "csv", "end_format": "json", "num_of_transfers": 2}]',
    }


@pytest.fixture()
def sample_mapping_single_response():
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": '{"uid": 1, "organization": 1, "name": "SF to HUD", "mapping_info": "{}", "start_format": "csv", "end_format": "json", "num_of_transfers": 1}',
    }


### Users
@pytest.fixture()
def users_event():
    return {"pathParameters": {"organization_id": "1"}}


@pytest.fixture()
def user_single_event():
    return {"pathParameters": {"organization_id": "1", "user_id": "1"}}


@pytest.fixture()
def sample_users_response():
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": '[{"uid": 1, "name": "Matt", "created_datetime": "2019-03-10 10:42:03", "organization": 1}]',
    }


@pytest.fixture()
def sample_user_single_response():
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": '{"uid": 1, "name": "Matt", "created_datetime": "2019-03-10 10:42:03", "organization": 1}',
    }


### Organizations
@pytest.fixture()
def organizations_event():
    return {"pathParameters": {"organization_id": "1"}}


@pytest.fixture()
def organization_single_event():
    return {"pathParameters": {"organization_id": "1", "organization_id": "1"}}


@pytest.fixture()
def sample_organizations_response():
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": '[{"uid": 1, "name": "OLI", "created_datetime": "2019-03-13 20:42:03"}, {"uid": 2, "name": "SPC", "created_datetime": "2019-03-15 01:03:03"}, {"uid": 3, "name": "OLI 2", "created_datetime": "2019-03-18 20:42:03"}]',
    }


@pytest.fixture()
def sample_organization_single_response():
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": '{"uid": 1, "name": "OLI", "created_datetime": "2019-03-13 20:42:03"}',
    }


### Downloads
@pytest.fixture()
def downloads_event():
    return {"pathParameters": {"organization_id": "1"}}


@pytest.fixture()
def download_single_event():
    return {"pathParameters": {"organization_id": "1", "download_id": "1"}}


@pytest.fixture()
def sample_downloads_response():
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": '[{"uid": 1, "name": "Download 1", "transfer_name": "CW to SF", "history_uid": 1, "expiration_datetime": "2019-03-09 20:42:03", "organization": 1, "file_location_info": "file_location_info_1"}]',
    }


@pytest.fixture()
def sample_download_single_response():
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": '{"uid": 1, "name": "Download 1", "transfer_name": "CW to SF", "history_uid": 1, "expiration_datetime": "2019-03-09 20:42:03", "organization": 1, "file_location_info": "file_location_info_1"}'
    }


@pytest.fixture()
def sample_download_link_response():
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": '{"download_link": "fake_link_for_file_location_info_1"}'
    }


# Upload
@pytest.fixture()
def upload_event():
    return {"pathParameters": {"organization_id": "1"}}

@pytest.fixture()
def sample_upload_response():
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": '{"message": "File uploaded"}'
    }

try:
    os.unlink(test_path.joinpath("api/models"))
except:
    pass

try:
    os.unlink(test_path.joinpath("api/library"))
except:
    pass


