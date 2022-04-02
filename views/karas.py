import fastapi
from fastapi import Form
from fastapi_chameleon import template

router = fastapi.APIRouter()

@router.get("/karas")
@template(template_file='karas.pt')
async def read_data_form_prezydent():
    return  {"message":"karas"}
