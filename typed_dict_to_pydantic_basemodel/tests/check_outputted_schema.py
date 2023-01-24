from typed_dict_to_pydantic_basemodel.export_to_BaseModel import export_json_schema
from typed_dict_to_pydantic_basemodel.page_type_dicts import BulkDatum, BulkEvents

export_json_schema(BulkDatum)
export_json_schema(BulkEvents)