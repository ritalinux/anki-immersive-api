from v1.routines.polyglot_routines import ImmersiveRoutine
from v1.utils.errors import FileFormatError

from fastapi import APIRouter, UploadFile
from typing import Annotated

import polars as pl

router = APIRouter(
    prefix='/polyglot'
)

### Routines are instantiate outside services scope to
### prevent new routines constructions in each request.
### Be careful with unnecessary cache in construct methods,
### it may be a security risk or a trigger for bugs.
immersive_routine = ImmersiveRoutine()

@router.post("/immersive")
async def immersive_service(file: UploadFile):
    """
    Call the routine for immersive
    polyglot deck's generation 

    - **file**: Csv file stream
    """

    file = {
        'name': '.'.join(file.filename.split('.')[:-1]),
        'type': file.filename.split('.')[-1],
        'content': pl.read_csv(file.file)
    }

    anki_deck = await immersive_routine.run(file)

    return {"filename": f"{file['name']}.{file['type']}"}