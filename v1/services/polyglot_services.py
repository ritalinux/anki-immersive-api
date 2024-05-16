from v1.routines.polyglot_routines import ImmersiveRoutine
from v1.utils.errors import FileFormatError

from fastapi import APIRouter, UploadFile
from typing import Annotated

import polars as pl

router = APIRouter(
    prefix='/polyglot'
)

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

    routine = ImmersiveRoutine()
    anki_deck = await routine.run(file)

    return {"filename": f"{file['name']}.{file['type']}"}