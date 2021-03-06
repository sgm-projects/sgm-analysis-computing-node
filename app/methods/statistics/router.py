from typing import Optional
from starlette import status
from fastapi import APIRouter
from fastapi import Request

from app.core.schema import TaskPostResult, MethodInfo
from app.core.queue import create_task
from .schema import SummaryTaskParams, HistorgamTaskParams, BoxplotTaskParams
from .tasks import run_summary, run_histogram, run_boxplot
from app.methods.methods import METHODS


router = APIRouter()

@router.post(
    "/summary",
    status_code=status.HTTP_201_CREATED,
    response_model=TaskPostResult
)
def summary_post(params: SummaryTaskParams, request: Request):
    res = create_task(run_summary, params.dict())
    res['url'] = request.url_for('get_result', job_id=res['job_id'])
    return TaskPostResult(**res)

@router.get(
    "/summary"
)
def summary_get():
    return METHODS['summary']

@router.post(
    "/histogram",
    status_code=status.HTTP_201_CREATED,
    response_model=TaskPostResult
)
def histogram_post(params: HistorgamTaskParams, request: Request):
    res = create_task(run_histogram, params.dict())
    res['url'] = request.url_for('get_result', job_id=res['job_id'])
    return TaskPostResult(**res)

@router.get(
    "/histogram"
)
def histogram_get():
    return METHODS['histogram']

@router.post(
    "/boxplot",
    status_code=status.HTTP_201_CREATED,
    response_model=TaskPostResult
)
def boxplot_post(params: BoxplotTaskParams, request: Request):
    res = create_task(run_boxplot, params.dict())
    res['url'] = request.url_for('get_result', job_id=res['job_id'])
    return TaskPostResult(**res)

@router.get(
    "/boxplot"
)
def boxplot_get():
    return METHODS['boxplot']