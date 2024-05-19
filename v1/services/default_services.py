from v1.routines.default_routines import BasicTypeRoutine
from v1.utils.errors import FileFormatError

from fastapi import APIRouter, UploadFile, File
from typing import Annotated

import polars as pl

router = APIRouter(
    prefix='/default'
)

### Routines are instantiate outside services scope to
### prevent new routines constructions in each request.
### Be careful with unnecessary cache in construct methods,
### it may be a security risk or a trigger for bugs.
basic_type_routine = BasicTypeRoutine()

@router.post("/basic_type")
async def basic_type_service(file: UploadFile):
    """
    Call the routine for Basic with type
    default deck's generation 

    - **file**: Csv file stream
    """

    file = {
        'name': '.'.join(file.filename.split('.')[:-1]),
        'type': file.filename.split('.')[-1],
        'content': pl.read_csv(file.file)
    }

    anki_deck = await basic_type_routine.run(file)

    return {"filename": f"{file['name']}.{file['type']}"}